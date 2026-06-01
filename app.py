import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from data import COMPANIES, ROLES, ROLE_DETAILS
import api_service
from flask import jsonify

app = Flask(__name__)
# Secret key is required to use Flask sessions
app.secret_key = 'super_secret_key_for_placement_app'
db_name = 'placement_app.db'

def init_db():
    """ Initialize SQLite Database for Users """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            role_id TEXT,
            step INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_resumes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            resume_text TEXT,
            last_analysis TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    """ Redirect to Dashboard if logged in, otherwise Login """
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """ Handle user registration """
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # Hash password before storing in SQLite Database
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        try:
            conn = sqlite3.connect(db_name)
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
                           (username, email, hashed_password))
            conn.commit()
            conn.close()
            flash('Registration successful! Please login to continue.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Error: Username or Email already exists.', 'danger')
            return redirect(url_for('signup'))
        
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """ Handle user login authentication """
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
        user = cursor.fetchone()
        conn.close()

        # Check if user exists and password is correct
        if user and check_password_hash(user[3], password):
            session['user_id'] = user[0]
            session['username'] = user[1]
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password. Try again.', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    """ Clear user session """
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    """ Main dashboard hub """
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    # Optional: fetch a few generic real-time remote software jobs
    realtime_jobs = api_service.fetch_realtime_jobs(category='software-dev', limit=3)
    
    return render_template('dashboard.html', username=session.get('username'), realtime_jobs=realtime_jobs)

@app.route('/departments')
def departments():
    """ Show all engineering departments """
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    depts = list(COMPANIES.keys())
    return render_template('departments.html', departments=depts)

@app.route('/department/<dept>')
def department(dept):
    """ View department details and its respective companies """
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    dept = dept.upper() 
    if dept in COMPANIES:
        dept_data = COMPANIES[dept]
        return render_template('department.html', dept=dept, data=dept_data)
    else:
        flash('Requested department was not found.', 'danger')
        return redirect(url_for('dashboard'))

@app.route('/company/<company_id>')
def company(company_id):
    """ Show company profile and available roles """
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    company_details = None
    # Search for company_id within the categories
    for dept, categories in COMPANIES.items():
        for category, companies in categories.items():
            for c in companies:
                if c['id'] == company_id:
                    company_details = c
                    break

    if not company_details:
        flash('Requested company was not found.', 'danger')
        return redirect(url_for('dashboard'))
        
    roles = ROLES.get(company_id, [])
    return render_template('company.html', company=company_details, roles=roles)

@app.route('/role/<role_id>')
def role(role_id):
    """ Detail view for a specific job role to prepare for """
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    role_data = ROLE_DETAILS.get(role_id)
    if not role_data:
        flash('Requested job role was not found.', 'danger')
        return redirect(url_for('dashboard'))
        
    # Fetch completed steps for progress tracking
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('SELECT step FROM user_progress WHERE user_id = ? AND role_id = ?', (session['user_id'], role_id))
    completed_steps = [row[0] for row in cursor.fetchall()]
    conn.close()
    
    # Generate mock question dynamically
    mock_question = api_service.generate_mock_interview_question(role_data['name'])
        
    return render_template('role.html', role=role_data, role_id=role_id, completed_steps=completed_steps, mock_question=mock_question)

@app.route('/api/progress', methods=['POST'])
def update_progress():
    """ Progress endpoint """
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    data = request.get_json()
    role_id = data.get('role_id')
    step = data.get('step')
    is_completed = data.get('is_completed')
    
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    if is_completed:
        cursor.execute('INSERT OR IGNORE INTO user_progress (user_id, role_id, step) VALUES (?, ?, ?)',
                       (session['user_id'], role_id, step))
    else:
        cursor.execute('DELETE FROM user_progress WHERE user_id = ? AND role_id = ? AND step = ?',
                       (session['user_id'], role_id, step))
    conn.commit()
    conn.close()
    
    return jsonify({'success': True})

@app.route('/tools/resume', methods=['GET', 'POST'])
def resume_tool():
    """ Resume Analyzer Tool """
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    analysis = None
    if request.method == 'POST':
        resume_text = request.form.get('resume_text', '')
        target_role = request.form.get('target_role', 'Software Engineer')
        
        analysis = api_service.evaluate_resume(resume_text, target_role)
        
        # Save analysis
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO user_resumes (user_id, resume_text, last_analysis) VALUES (?, ?, ?)",
                       (session['user_id'], resume_text, str(analysis)))
        conn.commit()
        conn.close()
        
    return render_template('resume_tool.html', analysis=analysis)


if __name__ == '__main__':
    # Initialize SQLite database before starting the Flask server
    init_db()
    print("Starting Placement Preparation Web Application...")
    print("Listening on http://127.0.0.1:5000/")
    app.run(debug=True, port=5000)

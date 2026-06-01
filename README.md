# Placement Preparation Web Application

A full-stack, AI-styled web application built with Python Flask, HTML, CSS, and SQLite for students to prepare for upcoming campus placements.

## Features
- **Authentication**: Secure Login and Signup functionality using Flask Sessions and SQLite.
- **Modern Dashboard**: A sleek dark theme with a glassmorphism (AI-style) design.
- **Preparation Modules**: Resources strictly structured for Aptitude, Logical Reasoning, Coding, and Communication.
- **Department & Company Module**: Segregated company listings (Top, Mid, Mass Recruiters) based on your department.
- **Role-Based Roadmaps**: Specialized skill requirement mapping and step-by-step learning roadmaps for designated job roles.

## Project Structure
```text
placement app/
│
├── app.py                  # Main Flask application and routing logic
├── data.py                 # Structured static dictionaries mock DB for Companies & Roles
├── placement_app.db        # SQLite database handling user authentication (Auto-generated)
├── static/
│   ├── style.css           # Global stylesheet with modern CSS tokens & themes
│   └── script.js           # Client-side transitions and interactivity
└── templates/
    ├── base.html           # Main template scaffolding
    ├── login.html          # Authentication 
    ├── signup.html         # Registration
    ├── dashboard.html      # Central Hub
    ├── department.html     # Companies list via category
    ├── company.html        # Profile details & roles
    └── role.html           # Specific roadmap, skills and external links
```

## How to Run the App Locally

### 1. Prerequisites
Make sure you have Python 3.x installed on your operating system.
You will need to install **Flask** and **Werkzeug**. Open your terminal/command prompt and run:
```bash
pip install Flask Werkzeug
```

### 2. Running the Server
Navigate to the project directory in your terminal and execute:
```bash
python app.py
```
*Note: The script will automatically trigger the creation of `placement_app.db` if it does not already exist.*

### 3. Accessing the Application
Once the server initializes, you should see an output on your terminal stating that it is running on a localized domain.
Open your favorite web browser and navigate to:
```text
http://127.0.0.1:5000/
```

- Click on **Sign Up Free** to register an account.
- **Log In** to get directed to your customized dashboard.
- Select your department (e.g. ECE) to view matching companies and navigate down to the tailored roadmaps!

import urllib.request
import json
import ssl

def fetch_realtime_jobs(category="software-dev", limit=5):
    """
    Fetches real-time job postings from a public API (Remotive).
    Requires no API Key.
    """
    url = f"https://remotive.com/api/remote-jobs?category={category}&limit={limit}"
    
    # Create an unverified context for fetching
    context = ssl._create_unverified_context()
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'PlacementApp/1.0'})
        with urllib.request.urlopen(req, context=context) as response:
            data = json.loads(response.read().decode())
            return data.get('jobs', [])[:limit]
    except Exception as e:
        print(f"Failed to fetch jobs: {e}")
        return []

def evaluate_resume(resume_text, job_role):
    """
    Mock AI Service for Resume Evaluation.
    In a true production environment, hook this up to the Google Generative AI (Gemini) API.
    """
    if not resume_text:
        return {"error": "No resume text provided."}
        
    # Analyze keywords in a mock fashion based on job role
    score = 75
    improvements = []
    
    if "Python" not in resume_text and "software" in job_role.lower():
        score -= 10
        improvements.append("Consider adding specific programming languages like Python or JavaScript.")
        
    if "agile" not in resume_text.lower():
        improvements.append("Mentioning project management methodologies like Agile/Scrum can boost your profile.")
        
    return {
        "score": score,
        "feedback": "Your resume has a solid structure but could use more quantifiable achievements.",
        "improvements": improvements,
        "ai_powered": True
    }

def generate_mock_interview_question(job_role, level="Entry"):
    """
    Generates a technical behavioral mock interview question.
    """
    if "software" in job_role.lower():
        return f"({level} Level) Can you describe a time you optimized a piece of code, and what was the impact on performance?"
    elif "data" in job_role.lower():
        return f"({level} Level) Explain the difference between supervised and unsupervised learning with real-world examples."
    else:
        return f"({level} Level) Describe a challenging project you've worked on recently and how you overcame obstacles."

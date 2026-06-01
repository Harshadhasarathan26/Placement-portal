# Placement Preparation Web Application

A full-stack web application developed using Python Flask, HTML, CSS, JavaScript, and SQLite to help students prepare for campus placements. The platform provides structured preparation resources, company-specific information, and role-based learning roadmaps through a modern and user-friendly interface.

## Features

* Secure Login and Signup System using Flask Sessions and SQLite
* Interactive Dashboard with a modern UI
* Aptitude Preparation Module
* Logical Reasoning Resources
* Coding Practice Guidance
* Communication Skills Preparation
* Department-wise Company Listings
* Categorized Recruiters (Top, Mid-Level, and Mass Recruiters)
* Role-Based Learning Roadmaps
* Career-Oriented Skill Recommendations

## Technologies Used

* Python
* Flask
* HTML5
* CSS3
* JavaScript
* SQLite

## Project Structure

```text
placement-app/
│
├── app.py
├── data.py
├── placement_app.db
│
├── static/
│   ├── style.css
│   └── script.js
│
└── templates/
    ├── base.html
    ├── login.html
    ├── signup.html
    ├── dashboard.html
    ├── department.html
    ├── company.html
    └── role.html
```

## Installation

### Prerequisites

* Python 3.x
* Flask

### Install Dependencies

```bash
pip install Flask Werkzeug
```

### Run the Application

```bash
python app.py
```

## Access the Application

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## Future Enhancements

* AI-powered interview assistance
* Resume analysis and feedback
* Mock aptitude tests
* Progress tracking dashboard
* Company-wise interview experiences

## Author

Harsha D, Jeevalakshmi V

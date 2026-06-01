# data.py
# Contains dictionaries to mock JSON responses for Companies, Roles and Skills

# Dictionary containing companies grouped by department and category
COMPANIES = {
    "ECE": {
        "Top Companies": [
            {
                "id": "qualcomm",
                "name": "Qualcomm",
                "profile": "Leading global wireless telecommunications products and services company.",
                "domain": "Hardware/Telecom",
                "career_link": "https://careers.qualcomm.com/"
            },
            {
                "id": "intel",
                "name": "Intel",
                "profile": "Multinational corporation and technology company, largest semiconductor chip manufacturer.",
                "domain": "Hardware",
                "career_link": "https://jobs.intel.com/"
            },
            {
                "id": "nvidia",
                "name": "NVIDIA",
                "profile": "Leader in GPU-accelerated computing, artificial intelligence, and semiconductor design.",
                "domain": "Semiconductor/AI",
                "career_link": "https://www.nvidia.com/en-us/about-nvidia/careers/"
            }
        ],
        "Mid-level Companies": [
            {
                "id": "tata-elxsi",
                "name": "Tata Elxsi",
                "profile": "Global provider of design and technology services across industries.",
                "domain": "Hardware/Software Design",
                "career_link": "https://www.tataelxsi.com/careers"
            }
        ],
        "Mass Recruiters": [
            {
                "id": "tcs",
                "name": "TCS (Tata Consultancy Services)",
                "profile": "Indian multinational IT services and consulting company.",
                "domain": "Software/IT Services",
                "career_link": "https://www.tcs.com/careers"
            },
            {
                "id": "cognizant",
                "name": "Cognizant",
                "profile": "Multinational IT technology and consulting company.",
                "domain": "Software/IT Services",
                "career_link": "https://careers.cognizant.com/"
            }
        ]
    },
    "CSE": {
        "Top Tech Giants": [
            {
                "id": "google",
                "name": "Google",
                "profile": "Multinational corporation specializing in Internet-related services and products.",
                "domain": "Internet/Software",
                "career_link": "https://careers.google.com/"
            },
            {
                "id": "microsoft",
                "name": "Microsoft",
                "profile": "Multinational technology company which produces computer software, cloud services.",
                "domain": "Software/Cloud",
                "career_link": "https://careers.microsoft.com/"
            }
        ],
        "Product Based Companies": [
            {
                "id": "amazon",
                "name": "Amazon",
                "profile": "Multinational technology company focusing on e-commerce, cloud computing, and AI.",
                "domain": "E-commerce/Cloud",
                "career_link": "https://www.amazon.jobs/"
            }
        ],
        "Service Based Companies": [
            {
                "id": "infosys",
                "name": "Infosys",
                "profile": "Multinational IT company providing business consulting and outsourcing services.",
                "domain": "Software/IT Services",
                "career_link": "https://www.infosys.com/careers/"
            },
            {
                "id": "wipro",
                "name": "Wipro",
                "profile": "Multinational corporation for IT, consulting and business process services.",
                "domain": "Software/IT Services",
                "career_link": "https://careers.wipro.com/"
            }
        ]
    },
    "IT": {
        "Top Companies": []
    },
    "EEE": {
        "Top Companies": []
    },
    "Mechanical": {
        "Top Companies": []
    }
}

# Job Roles linked to specific company IDs
ROLES = {
    "qualcomm": [
        {"id": "hardware-engineer", "name": "Hardware Engineer"},
        {"id": "embedded-engineer", "name": "Embedded Engineer"}
    ],
    "intel": [
        {"id": "hardware-engineer", "name": "Hardware Engineer"},
        {"id": "embedded-engineer", "name": "Embedded Engineer"}
    ],
    "nvidia": [
        {"id": "vlsi-design-engineer", "name": "VLSI Design Engineer"},
        {"id": "software-engineer", "name": "Software Engineer"}
    ],
    "tata-elxsi": [
        {"id": "embedded-developer", "name": "Embedded Developer"},
    ],
    "tcs": [
        {"id": "system-engineer", "name": "System Engineer (Ninja / Digital)"}
    ],
    "cognizant": [
        {"id": "programmer-analyst", "name": "Programmer Analyst Trainee"}
    ],
    "google": [
        {"id": "software-engineer", "name": "Software Engineer"},
        {"id": "data-scientist", "name": "Data Scientist"}
    ],
    "microsoft": [
        {"id": "software-engineer", "name": "Software Development Engineer"},
        {"id": "product-manager", "name": "Product Manager"}
    ],
    "amazon": [
        {"id": "sde", "name": "Software Development Engineer (SDE)"},
        {"id": "cloud-support", "name": "Cloud Support Associate"}
    ],
    "infosys": [
        {"id": "system-engineer-infosys", "name": "Systems Engineer"}
    ],
    "wipro": [
        {"id": "project-engineer", "name": "Project Engineer"}
    ]
}

# Specific requirements and learning roadmaps for every Job Role
ROLE_DETAILS = {
    "hardware-engineer": {
        "name": "Hardware Engineer",
        "skills": ["Digital Logic", "Verilog/VHDL", "Computer Architecture", "VLSI Design"],
        "roadmap": [
            "1. Beginner: Revise Digital logic and Boolean algebra fundamentals",
            "2. Intermediate: Computer architecture & organization mapping, Microcontrollers",
            "3. Advanced: FPGA design basics and timing constraints, Advanced VLSI design"
        ],
        "links": [
            {"title": "NPTEL VLSI Design Course", "url": "https://nptel.ac.in/"},
            {"title": "Verilog Tutorial (ChipVerify)", "url": "https://www.chipverify.com/verilog/verilog-tutorial"}
        ],
        "last_updated": "2026-03-30"
    },
    "embedded-engineer": {
        "name": "Embedded Engineer",
        "skills": ["C/C++", "Microcontrollers", "RTOS", "Linux", "Device Drivers"],
        "roadmap": [
            "1. Beginner: Master C programming with emphasis on pointers and memory",
            "2. Intermediate: Learn microcontroller architecture (e.g., ARM Cortex-M) and communication protocols (I2C, SPI, UART)",
            "3. Advanced: Real-Time Operating Systems (RTOS) basics and Linux Device Drivers"
        ],
        "links": [
            {"title": "Embedded Systems Tutorial", "url": "https://www.tutorialspoint.com/embedded_systems/index.htm"},
            {"title": "FreeRTOS Documentation", "url": "https://www.freertos.org/"}
        ],
        "last_updated": "2026-03-30"
    },
    "vlsi-design-engineer": {
        "name": "VLSI Design Engineer",
        "skills": ["Verilog", "VHDL", "Digital Logic", "Scripting (Python/Tcl)"],
        "roadmap": [
            "1. Beginner: Revise Digital logic and Boolean algebra fundamentals",
            "2. Intermediate: Learn a hardware description language (Verilog/VHDL) computationally",
            "3. Advanced: VLSI design concepts and layout rules, STA (Static Timing Analysis)"
        ],
        "links": [
            {"title": "ChipVerify Verilog Tutorial", "url": "https://www.chipverify.com/"}
        ],
        "last_updated": "2026-03-30"
    },
    "system-engineer": {
         "name": "System Engineer",
         "skills": ["Python / Java", "SQL", "Data Structures & Algorithms", "Aptitude"],
         "roadmap": [
             "1. Master one object-oriented programming language (Java, C++, or Python)",
             "2. Strong foundation in Data Structures (Arrays, Linked Lists, Trees) and Algorithms",
             "3. Relational Database Concepts (DBMS) and SQL queries",
             "4. Practice General Aptitude & Logical Reasoning (crucial for mass recruiters)"
         ],
         "links": [
            {"title": "GeeksforGeeks placement practice", "url": "https://www.geeksforgeeks.org/"},
            {"title": "IndiaBix Aptitude test preparation", "url": "https://www.indiabix.com/"}
         ],
         "last_updated": "2026-03-30"
    },
    "programmer-analyst": {
         "name": "Programmer Analyst Trainee",
         "skills": ["C/C++/Java", "DBMS & SQL", "Software Engineering lifecycle"],
         "roadmap": [
             "1. Ensure solid programming fundamentals",
             "2. Practice problem solving on coding platforms to clear coding rounds",
             "3. Know your Object Oriented Programming (OOP) concepts by heart",
             "4. Relational Database Management theory and queries"
         ],
         "links": [
            {"title": "LeetCode interview prep", "url": "https://leetcode.com/"},
            {"title": "W3Schools SQL Tutorial", "url": "https://www.w3schools.com/sql/"}
         ],
         "last_updated": "2026-03-30"
    },
    "embedded-developer": {
         "name": "Embedded Developer",
         "skills": ["Advanced C", "Microprocessors", "Hardware Debugging"],
         "roadmap": [
             "1. Advanced C concepts (Bitwise ops, Pointers, Memory Management)",
             "2. Bare-metal programming vs OS programming",
             "3. Reading datasheets efficiently",
             "4. Debugging hardware using JTAG/SWD tools"
         ],
         "links": [
            {"title": "C Programming FAQs", "url": "https://c-faq.com/"}
         ],
         "last_updated": "2026-03-30"
    },
    "systems-engineer": {
         "name": "Systems Engineer",
         "skills": ["Linux Kernel", "C Programming", "Computer Networks"],
         "roadmap": [
             "1. Operating System Internals (Processes, Threads, Concurrency)",
             "2. System-level programming in C (POSIX APIs)",
             "3. Advanced Computer Networks (TCP/IP stack, layering)"
         ],
         "links": [
            {"title": "Linux Journey (OS & CLI basics)", "url": "https://linuxjourney.com/"}
         ],
         "last_updated": "2026-03-30"
    },
    "software-engineer": {
        "name": "Software Engineer",
        "skills": ["Data Structures & Algorithms", "System Design", "Web Development", "Database Management"],
        "roadmap": [
            "1. Master Data Structures and Algorithms comprehensively.",
            "2. Gain expertise in at least one modern framework (React, Node, etc.).",
            "3. Learn High-Level and Low-Level System Design principles.",
            "4. Build a strong portfolio of projects."
        ],
        "links": [
            {"title": "NeetCode DSA prep", "url": "https://neetcode.io/"},
            {"title": "System Design Primer", "url": "https://github.com/donnemartin/system-design-primer"}
        ],
        "last_updated": "2026-04-01"
    },
    "data-scientist": {
        "name": "Data Scientist",
        "skills": ["Python", "Machine Learning", "Statistics & Probability", "SQL", "Data Visualization"],
        "roadmap": [
            "1. Master Python and core libraries (Pandas, NumPy, Scikit-learn).",
            "2. Deep dive into statistical mathematics and probability theory.",
            "3. Learn supervised and unsupervised ML algorithms.",
            "4. Work on real-world datasets and Kaggle competitions."
        ],
        "links": [
            {"title": "Kaggle Learn", "url": "https://www.kaggle.com/learn"},
            {"title": "StatQuest ML Videos", "url": "https://statquest.org/"}
        ],
        "last_updated": "2026-04-01"
    },
    "product-manager": {
        "name": "Product Manager",
        "skills": ["Product Strategy", "Agile Methodologies", "User Research", "Data Analytics"],
        "roadmap": [
            "1. Learn the product lifecycle management and strategic planning.",
            "2. Understand Agile, Scrum methodologies and sprint planning.",
            "3. Practice creating PRDs (Product Requirement Documents).",
            "4. Familiarize with analytics tools for tracking product metrics."
        ],
        "links": [
            {"title": "Product School Resources", "url": "https://productschool.com/"}
        ],
        "last_updated": "2026-04-01"
    },
    "sde": {
        "name": "Software Development Engineer (SDE)",
        "skills": ["Advanced DSA", "Object Oriented Design", "Scalability", "AWS Basics"],
        "roadmap": [
            "1. Exhaustive practice of technical coding problems.",
            "2. Understand Object-Oriented Analysis and Design patterns.",
            "3. Grasp fundamentals of scalable application architecture.",
            "4. Learn AWS core services conceptually."
        ],
        "links": [
            {"title": "Cracking The Coding Interview", "url": "https://www.crackingthecodinginterview.com/"}
        ],
        "last_updated": "2026-04-01"
    },
    "cloud-support": {
        "name": "Cloud Support Associate",
        "skills": ["Linux/Unix", "Networking", "AWS Services", "Troubleshooting"],
        "roadmap": [
            "1. Master Linux commands, file systems, and administration.",
            "2. Clear understanding of networking basics (DNS, TCP/IP, OSI, HTTP).",
            "3. Understand Cloud principles (EC2, S3, IAM, VPC).",
            "4. Develop strong debugging and troubleshooting logical flow."
        ],
        "links": [
            {"title": "AWS Cloud Practitioner Training", "url": "https://aws.amazon.com/training/"}
        ],
        "last_updated": "2026-04-01"
    },
    "system-engineer-infosys": {
        "name": "Systems Engineer",
        "skills": ["Programming Fundamentals", "Database/SQL", "Aptitude"],
        "roadmap": [
            "1. Strengthen fundamental logic in any programming language (Python, Java, C++).",
            "2. Master intermediate SQL and Database schemas.",
            "3. Heavily practice Quantitative Aptitude and Verbal Reasoning.",
            "4. Prepare for behavioral and HR rounds."
        ],
        "links": [
            {"title": "PrepInsta Infosys Section", "url": "https://prepinsta.com/"}
        ],
        "last_updated": "2026-04-01"
    },
    "project-engineer": {
        "name": "Project Engineer",
        "skills": ["Coding", "Analytical Skills", "Communication", "Teamwork"],
        "roadmap": [
            "1. Gain proficiency in procedural and object-oriented coding.",
            "2. Work on group projects to demonstrate teamwork.",
            "3. Complete logic puzzles to test analytical capabilities.",
            "4. Enhance spoken and written communication."
        ],
        "links": [
            {"title": "GeeksforGeeks Wipro Prep", "url": "https://www.geeksforgeeks.org/"}
        ],
        "last_updated": "2026-04-01"
    }
}

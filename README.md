Student Course Registration Web App (DevOps Project)


📌 Project Overview:
This is a Dynamic Web Application built using Python (Flask) for Student Course Registration.


It follows DevOps concepts like:
Source Code Management (Git + GitHub)
Containerization (Docker)
CI/CD Pipeline (Optional - can add GitHub Actions)
Deployment-ready structure


📂 Project Structure:
student-course-registration/
├── app/
│   ├── main.py
│   └── templates/
│       ├── home.html
│       ├── register.html
│       ├── success.html
│       └── students.html
├── Dockerfile
├── requirements.txt
├── registrations.csv  # Stores registered student data
├── .gitignore
└── README.md


✅ Features:
📝 Student Registration Form
📄 Stores submitted data into a CSV file
📊 Dynamic page to view all registered students
🖥️ Responsive frontend using Bootstrap
🐳 Containerization with Docker
🔗 Version Control with Git and GitHub


🚀 Technologies Used:
Tech	Purpose
Python	Backend
Flask	Web Framework
HTML + Bootstrap	Frontend
Git + GitHub	Source Code Management
Docker	Containerization
(Optional) GitHub Actions	CI/CD Pipeline


🛠️ How to Run Locally:
▶️ Without Docker:
Create Virtual Environment:
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app/main.py
http://localhost:5000


▶️ Using Docker:
Build Image:
docker build -t student-course-app .
docker run -p 5000:5000 student-course-app
http://localhost:5000


🧑‍💻 DevOps Concepts Used:
Concept	How it's applied in this project
Source Code Management	Git & GitHub
Continuous Integration	(Can be added via GitHub Actions)
Containerization	Dockerized Flask app
Automation	Build and run with Docker commands


✅ Future Improvements :
Add MySQL/SQLite database
Deploy on cloud (AWS, Heroku, etc.)
Add CI/CD pipeline with GitHub Actions
Form validations & error handling
Authentication (Admin login to view students)

✅ Author:
👤 Nandala Nithin

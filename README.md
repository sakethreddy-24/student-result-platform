# 🎓 Student Result Management System

![Build Status](https://github.com/sakethreddy-24/student-result-platform/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-black?logo=flask)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![Terraform](https://img.shields.io/badge/Terraform-IaC-7B42BC?logo=terraform)
![Azure](https://img.shields.io/badge/Microsoft%20Azure-Cloud-0078D4?logo=microsoftazure)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-4169E1?logo=postgresql)
![License](https://img.shields.io/badge/License-MIT-green)

A production-ready **Flask-based Student Result Management System** deployed on **Microsoft Azure** using **Terraform**, **Docker**, and **Docker Compose**. This project demonstrates Infrastructure as Code (IaC), containerization, cloud deployment, and DevOps best practices.

---

#  Live Demo

**Application URL**

```
http://52.140.121.158:9090
```

> **Note:** The application is hosted on an Azure Virtual Machine. If the VM is stopped, the application will be unavailable until the VM is started again.

---

#  Project Overview

This project allows users to:

- Add Students
- Manage Student Information
- Add Results
- View Student Results
- Store data in PostgreSQL
- Deploy the complete application using Docker on Azure

The entire infrastructure was provisioned using Terraform, making the deployment repeatable and automated.

---

#  Architecture

```
                Internet
                    │
                    ▼
          Azure Public IP
                    │
                    ▼
          Azure Network Security Group
                    │
                    ▼
              Azure Ubuntu VM
                    │
          Docker Compose Stack
        ┌────────────┴────────────┐
        │                         │
        ▼                         ▼
   Flask Application       PostgreSQL Database
```

---

# 🛠 Tech Stack

### Cloud

- Microsoft Azure
- Azure Virtual Machine
- Network Security Group
- Public IP

### Infrastructure as Code

- Terraform

### Backend

- Python
- Flask
- SQLAlchemy

### Database

- PostgreSQL

### Containerization

- Docker
- Docker Compose

### Version Control

- Git
- GitHub

---

# 📂 Project Structure

```text
student-result-platform/
│
├── app/
├── terraform/
├── screenshots/
├── static/
├── templates/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .github/
```

---

#  Features

- Student Management
- Result Management
- PostgreSQL Integration
- Dockerized Deployment
- Infrastructure as Code using Terraform
- Azure Cloud Deployment
- Responsive Web Interface

---

#  Deployment Workflow

1. Provision Azure Infrastructure using Terraform
2. Create Azure Virtual Machine
3. Install Docker & Docker Compose
4. Clone the repository
5. Configure environment variables
6. Build Docker images
7. Start application using Docker Compose
8. Access the application through Azure Public IP

---

#  Application Screenshots

## Dashboard

![Dashboard](screenshots/app/dashboard.png)

---

## Add Student

![Add Student](screenshots/app/add-student.png)

---

## Students

![Students](screenshots/app/students.png)

---

## Add Result

![Add Result](screenshots/app/add-result.png)

---

## Results

![Results](screenshots/app/results.png)

---

## Live Application

![Live Application](screenshots/app/live-dashboard.png)

---

#  Challenges Faced

During development, several real-world deployment issues were encountered and resolved:

- PostgreSQL table initialization issue
- Database connection configuration
- Azure Network Security Group configuration
- Docker container networking
- Gunicorn deployment configuration
- Environment variable management

Resolving these issues helped improve practical understanding of cloud deployment and DevOps troubleshooting.

---

#  Future Improvements

- HTTPS using Let's Encrypt
- Nginx Reverse Proxy
- GitHub Actions CI/CD
- Custom Domain
- Azure Monitor Integration
- Container Health Checks
- Database Migration using Flask-Migrate
- Kubernetes Deployment (AKS)

---

# 👨‍💻 Author

**Saketh Reddy**

B.Tech CSE (AI & ML)

DevOps Enthusiast

---


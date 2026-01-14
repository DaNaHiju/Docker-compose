# Project 1 – Flask + MySQL with Docker Compose

This project is a simple **Flask** web application that connects to a **MySQL** database running in Docker. The app counts how many times the page is visited and stores this information in MySQL. The whole stack is orchestrated with **Docker Compose**.

---

## Architecture

The stack is composed of two containers:

- **mysql**  
  - Image: `mysql:8.0`  
  - Exposes port `3306`  
  - Uses a Docker **volume** for persistent data  
  - Uses a **bind mount** to run `init.sql` on first startup (creates the table and initial data)

- **flask**  
  - Built from the provided `Dockerfile`  
  - Exposes port `5000` (Flask default)  
  - Connects to the MySQL container using environment variables

---

## Project Structure

```text
project-1/
├── Dockerfile
├── docker-compose.yml
├── init.sql
├── main.py
├── requirements.txt
└── templates/
    └── index.html

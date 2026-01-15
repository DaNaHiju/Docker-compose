# Clock App - Docker Compose Project

A multi-container Docker application demonstrating microservices communication using Flask and Docker Compose.

## Project Overview

This project consists of two Flask applications that communicate with each other:

- **Clock App**: Displays current time and provides an API to update it (Port 5001)
- **Button App**: Contains a button that decrements the clock time via HTTP requests (Port 5002)

## Technologies Used

- Python 3.11
- Flask
- Docker & Docker Compose
- uv (Python package manager)
- Requests library

## Quick Start

### Run with Docker Compose

```bash
docker-compose up --build

Access the applications

    Clock App: http://localhost:5001

    Button App: http://localhost:5002

Test it

    Open http://localhost:5001 - see the clock

    Open http://localhost:5002 - click the button

    Watch the clock time decrement!

Docker Commands

bash
# Start containers
docker-compose up --build

# Stop containers
docker-compose down

# View logs
docker-compose logs -f

# List running containers
docker-compose ps

Project Structure

text
Clock-app/
├── clock_app/
│   ├── app.py
│   ├── templates/
│   ├── Dockerfile
│   └── requirements.txt
├── button_app/
│   ├── app.py
│   ├── templates/
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
└── README.md

How It Works

    Clock App runs on port 5001 and displays current time

    Button App runs on port 5002 with a decrement button

    When button is clicked, it sends POST request to Clock App's /update_time endpoint

    Clock App decrements time by 1 second and returns updated time

    Both apps communicate through Docker's bridge network

API Endpoints
Clock App (5001)

    GET / - Clock UI

    GET /get_time - Get current time (JSON)

    POST /update_time - Decrement time by 1 second

Button App (5002)

    GET / - Button UI

    POST /decrement - Trigger clock decrement

Development

Run locally without Docker:

bash
# Clock App
cd clock_app
uv run python app.py

# Button App (in another terminal)
cd button_app
uv run python app.py
# Flask Docker Manager

Web interface for managing Docker containers with Flask and docker-py. Create, view, delete containers and access their web interfaces directly from your browser.

## Features

- Create containers with custom port mappings
- View all containers (running/stopped)  
- Delete containers with one click
- Auto-redirect to containerized web apps
- Built with Flask 3.0, docker-py 7.0, and uv package manager

## Quick Start

### Local Development
```bash
# Install dependencies
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync

# Run app
uv run app.py
# Visit http://localhost:5000

Docker Deployment

bash
docker build -t flask-docker-manager .
docker run -d -p 5000:5000 -v /var/run/docker.sock:/var/run/docker.sock flask-docker-manager

Prerequisites

    Docker running locally

    Python 3.12+

    User in docker group: sudo usermod -aG docker $USER

Usage

    Create: Click "Create Container" → fill form (name, image like nginx, ports) → submit

    Open: Click "Open" to access container's web interface

    Delete: Click "Delete" to stop and remove container

Tech Stack

Python 3.12 | Flask 3.0 | docker-py 7.0 | uv package manager | Jinja2
Troubleshooting

Port conflict: docker stop container_name && docker rm container_name
Permission denied: sudo usermod -aG docker $USER (logout/login)
DevOps Learning Value

This project teaches:

    Docker Python SDK integration for infrastructure automation

    Modern dependency management with uv (10-100x faster than pip)

    Docker-in-Docker patterns used in CI/CD systems

    Infrastructure as Code principles

    Full-stack container management (backend + frontend + deployment)

Perfect foundation for Kubernetes, CI/CD pipelines, and GenAI deployment platforms.
License

MIT License

text

## Why This Project Matters (Quick Summary)

This is a **mini-Portainer** that teaches production DevOps patterns in 200 lines of code. You're learning how to programmatically control Docker using Python APIs—the same pattern used by Kubernetes, GitLab CI, and enterprise container platforms.[3][4][5]

The uv integration shows modern Python tooling (10-100x faster than pip) critical for CI/CD pipeline optimization. Running a containerized Flask app that manages other containers demonstrates Docker-in-Docker networking used by CI/CD runners.[6][7][8][9]

**Bottom line:** This project combines backend development, container orchestration, and deployment automation—core DevOps skills that scale directly to enterprise infrastructure management and GenAI model deployment platforms.
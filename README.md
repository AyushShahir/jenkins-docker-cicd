
# 🚀 Jenkins + Docker CI/CD Pipeline

## 🎯 Overview

This project demonstrates a simple CI/CD pipeline using Jenkins and Docker.

The pipeline automatically:

1. Builds a Docker image
2. Runs unit tests
3. Deploys the application as a Docker container

## ⚒️ Technologies Used

- Jenkins
- Docker
- Python
- Git
- GitHub

## Project Structure

```text
jenkins-docker-cicd/
├── app.py
├── test_app.py
├── Dockerfile
├── Dockerfile.jenkins
├── Jenkinsfile
├── .gitignore
└── README.md
````

## 📱 Application

The application is a simple Python HTTP server running on port `8000`.

When accessed through the browser, it displays:

```text
Hello from Jenkins + Docker!
```

## 🟣 CI/CD Pipeline

The Jenkins pipeline contains three stages:

### 1. Build

Jenkins builds the Docker image:

```bash
docker build -t jenkins-docker-cicd:latest .
```

### 2. Test

Jenkins runs the unit tests inside a temporary Docker container:

```bash
docker run --rm jenkins-docker-cicd:latest python -m unittest test_app.py
```

### 3. Deploy

Jenkins removes the previous application container and starts a new one:

```bash
docker rm -f jenkins-demo || true
docker run -d -p 8000:8000 --name jenkins-demo jenkins-docker-cicd:latest
```

## Pipeline Flow

```text
GitHub
   ↓
Jenkins
   ↓
Build Docker Image
   ↓
Run Unit Tests
   ↓
Deploy Docker Container
   ↓
Application on localhost:8000
```

## How to Run

### Clone the Repository

```bash
git clone https://github.com/AyushShahir/jenkins-docker-cicd.git
cd jenkins-docker-cicd
```

### Build the Application Manually

```bash
docker build -t jenkins-docker-cicd .
```

### Run the Application

```bash
docker run -d -p 8000:8000 --name jenkins-demo jenkins-docker-cicd
```

Open the application in your browser:

```text
http://localhost:8000
```

## Jenkins Setup

Jenkins was run using Docker and configured to access the Docker Engine through the Docker socket.

The Jenkins pipeline was configured using **Pipeline script from SCM** with the GitHub repository and `Jenkinsfile`.

## ⭐️ Result

The Jenkins pipeline successfully completed:

* Docker image build
* Automated unit testing
* Docker container deployment

Pipeline result:
Finished: SUCCESS

## SCREENSHOTS
<img width="1408" height="881" alt="Screenshot 2026-10-03 at 4 24 02 PM" src="https://github.com/user-attachments/assets/1ae95b9d-fc9b-4c0d-a247-a0ef43751394" />
<img width="1408" height="881" alt="Screenshot 2026-10-03 at 4 23 34 PM" src="https://github.com/user-attachments/assets/3968c3d0-65d3-45bd-b712-b8ec5646a72f" />
<img width="1408" height="881" alt="Screenshot 2026-10-03 at 4 22 38 PM" src="https://github.com/user-attachments/assets/ba431231-3b01-4c4e-8997-ad5f53ae6942" />
=======
```text
Finished: SUCCESS
```

The deployed application was verified at:

```text
http://localhost:8000
```
## Webhook Test

GitHub webhook trigger test.

## Automatic CI Trigger

A GitHub webhook is configured to trigger the Jenkins pipeline whenever changes are pushed to the `main` branch.

GitHub → Webhook → Jenkins → Build → Test → Deploy

## Automatic CI Trigger with GitHub Webhook

To automatically trigger the Jenkins pipeline whenever changes are pushed to the GitHub repository, a GitHub webhook was configured.

Since Jenkins was running locally on `localhost:8080`, **Cloudflare Tunnel (`cloudflared`)** was used to temporarily expose the local Jenkins server to the internet.

### Cloudflare Tunnel

The tunnel was started using:
cloudflared tunnel --url http://localhost:8080

## Screenshots

### Jenkins Pipeline

![Jenkins Pipeline](https://github.com/user-attachments/assets/1ae95b9d-fc9b-4c0d-a247-a0ef43751394)

### Jenkins Build Output

![Jenkins Build Output](https://github.com/user-attachments/assets/3968c3d0-65d3-45bd-b712-b8ec5646a72f)

### Application Running

![Application Running](https://github.com/user-attachments/assets/ba431231-3b01-4c4e-8997-ad5f53ae6942)

````



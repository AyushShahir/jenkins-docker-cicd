pipeline {

    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building Docker image...'

                sh 'docker build -t jenkins-docker-cicd:latest .'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'

                sh 'docker run --rm jenkins-docker-cicd:latest python -m unittest test_app.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'

                sh 'docker rm -f jenkins-demo || true'
                sh 'docker run -d -p 8000:8000 --name jenkins-demo jenkins-docker-cicd:latest'
            }
        }
    }
}
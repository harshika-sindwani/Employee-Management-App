pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/harshika-sindwani/Employee-Management-App.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t employee-management-app .'
            }
        }

        stage('Stop Existing Container') {
            steps {
                sh 'docker stop employee-app || true'
                sh 'docker rm employee-app || true'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name employee-app employee-management-app'
            }
        }
    }

    post {
        success {
            echo 'Application deployed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}

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

        stage('Deploy using Ansible') {
    steps {
        sh 'ansible-playbook -i ansible/hosts ansible/deploy.yml'
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

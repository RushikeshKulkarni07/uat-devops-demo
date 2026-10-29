pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/<YOUR_USERNAME>/uat-devops-demo.git'
            }
        }
        stage('Setup Python Env') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\python -m pip install --upgrade pip'
                bat 'venv\\Scripts\\python -m pip install -r requirements.txt'
            }
        }
        stage('Run hello.py') {
            steps {
                bat 'venv\\Scripts\\python hello.py'
            }
        }
        stage('Pytest') {
            steps {
                bat 'venv\\Scripts\\python -m pytest'
            }
        }
        stage('Evidently Monitor') {
            steps {
                bat 'venv\\Scripts\\python monitor_evidently.py'
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'reports/junit.xml'
            archiveArtifacts artifacts: 'reports/*.html', allowEmptyArchive: true
        }
    }
}

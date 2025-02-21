pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/sachinkumar6205/Integration.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install requests pytest'
            }
        }

        stage('Run Integration Tests') {
            steps {
                sh 'pytest test_integration.py'
            }
        }
    }

    post {
        always {
            junit 'pytest-results.xml'
        }
    }
}

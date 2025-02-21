pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                // GitHub repository se code checkout karein
                git 'https://github.com/sachinkumar6205/Integration.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Python dependencies install karein
                sh 'pip install requests pytest'
            }
        }

        stage('Run Integration Tests') {
            steps {
                // Integration tests run karein
                sh 'pytest --junitxml=pytest-results.xml'
            }
        }
    }

    post {
        always {
            // Test results ko Jenkins ke dashboard par upload karein
            junit 'pytest-results.xml'
        }
    }
}

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Create Python Environment') {
            steps {
                bat '''
                    py -3 -m venv .venv
                    .venv\\Scripts\\python.exe -m pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    .venv\\Scripts\\python.exe -m pip install -r requirements.txt
                    .venv\\Scripts\\python.exe -m playwright install chromium
                '''
            }
        }

        stage('Run Playwright Tests') {
            steps {
                bat '''
                    .venv\\Scripts\\python.exe -m pytest -v --browser chromium --junitxml=reports\\junit.xml
                '''
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'reports/junit.xml'
            archiveArtifacts allowEmptyArchive: true, artifacts: 'reports/**'
        }
    }
}
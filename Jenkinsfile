pipeline {
    agent any

    environment {
        INCIDENT_API_URL = 'http://34.229.17.13:8000/webhook/jenkins'
        WEBHOOK_SECRET   = '2fe931364f4a16f9bcdad4f287880af536a8862a97712fbd151c702a91591c9a'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Run test suite') {
            steps {
                sh 'python3 -m pytest -q'
            }
        }
    }

    post {
        failure {
            sh """
                curl -sS -X POST "${INCIDENT_API_URL}" \\
                  -H "Content-Type: application/json" \\
                  -H "X-Webhook-Secret: ${WEBHOOK_SECRET}" \\
                  -d '{
                    "job_name": "${JOB_NAME}",
                    "build_number": ${BUILD_NUMBER},
                    "build_url": "${BUILD_URL}",
                    "status": "FAILURE",
                    "branch": "${env.GIT_BRANCH ?: 'main'}"
                  }'
            """
        }
    }
}

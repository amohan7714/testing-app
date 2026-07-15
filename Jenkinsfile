pipeline {
    agent any

    environment {
        INCIDENT_API_URL    = 'http://34.229.17.13:8000/webhook/jenkins'
        WEBHOOK_SECRET       = '2fe931364f4a16f9bcdad4f287880af536a8862a97712fbd151c702a91591c9a'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source from main branch...'
                sh 'echo "commit def5678 checked out"'
            }
        }

        stage('Install dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh '''
                    echo "Collecting fastapi==0.115.6"
                    echo "Collecting sqlalchemy==2.0.36"
                    echo "Collecting asyncpg==0.30.0"
                    echo "Successfully installed fastapi-0.115.6 sqlalchemy-2.0.36 asyncpg-0.30.0"
                '''
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
            echo 'Build failed — notifying incident API...'
            sh """
              curl -sS -X POST "${INCIDENT_API_URL}" \\
                -H "Content-Type: application/json" \\
                -H "X-Webhook-Secret: ${WEBHOOK_SECRET}" \\
                -d '{
                  "job_name": "${JOB_NAME}",
                  "build_number": ${BUILD_NUMBER},
                  "build_url": "${BUILD_URL}",
                  "status": "FAILURE",
                  "branch": "${env.GIT_BRANCH ?: 'main'}",
                  "repository_url": "${env.GIT_URL ?: ''}",
                  "commit_sha": "${env.GIT_COMMIT ?: ''}"
                }'
            """
        }
        success {
            echo 'Build succeeded — no incident created.'
        }
    }
}

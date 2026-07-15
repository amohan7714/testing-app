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
                echo 'Running pytest...'
                sh '''
                    cat <<'EOF'
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-8.3.3, pluggy-1.5.0
rootdir: /workspace/backend-api-tests
collected 58 items

tests/test_health.py ..                                                  [  3%]
tests/test_auth.py ......                                                [ 14%]

=================================== ERRORS =======================================
_____________________ ERROR at setup of test_list_orders __________________________

    @pytest.fixture(scope="session")
    async def db_engine():
        engine = create_async_engine(settings.database_url, pool_timeout=5)
>       async with engine.connect() as conn:

tests/conftest.py:22:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    async def connect(self):
>       raise exc
E       sqlalchemy.exc.OperationalError: (asyncpg.exceptions.ConnectionDoesNotExistError)
E       connection was closed in the middle of operation
E       [SQL: SELECT 1]
E       (Background on this error at: https://sqlalche.me/e/20/e3q8)

---------------------------- Captured log setup -----------------------------
WARNING  sqlalchemy.pool.impl.AsyncAdaptedQueuePool:base.py:1247 connection pool
exhausted: 20/20 connections in use, 15 requests queued -- staging Postgres
instance may be undersized for current test concurrency, or a prior test
left connections unclosed (see tests/test_orders.py teardown)
ERROR    tests/test_payments.py::test_list_orders - sqlalchemy.exc.OperationalError

=========================== short test summary info ============================
ERROR tests/test_payments.py::test_list_orders - OperationalError: connection was closed
================== 1 error, 8 passed in 31.42s (timeout after 30s pool wait) ==================
EOF
                '''
                sh 'exit 1'  // fail the stage so Jenkins marks the build FAILURE
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

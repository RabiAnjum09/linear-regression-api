
pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build and Deploy API') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKERHUB_USER',
                        passwordVariable: 'DOCKERHUB_TOKEN'
                    )
                ]) {
                    sh '''
                        set -eu

                        echo "$DOCKERHUB_TOKEN" | docker login \
                            -u "$DOCKERHUB_USER" --password-stdin

                        docker compose -p linear-regression-api build
                        docker compose -p linear-regression-api push

                        docker compose -p linear-regression-api down
                        docker compose -p linear-regression-api up -d

                        docker compose -p linear-regression-api ps
                        docker logout
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Build and deployment succeeded.'
        }
        failure {
            echo 'Build or deployment failed. Check the Console Output.'
        }
    }
}

pipeline {
    agent any

    environment {
        IMAGE_NAME = 'garda05/modul2-flask-db'
        REGISTRY_CREDENTIALS = 'dockerhub-credentials'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Application Image') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'docker build -t "$IMAGE_NAME:$BUILD_NUMBER" .'
                        sh 'docker tag "$IMAGE_NAME:$BUILD_NUMBER" "$IMAGE_NAME:latest"'
                    } else {
                        bat "docker build -t %IMAGE_NAME%:%BUILD_NUMBER% ."
                        bat "docker tag %IMAGE_NAME%:%BUILD_NUMBER% %IMAGE_NAME%:latest"
                    }
                }
            }
        }

        stage('Test Container') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'docker run --rm "$IMAGE_NAME:$BUILD_NUMBER" python -c "import flask; print(\'Flask berhasil di-install\')"'
                    } else {
                        bat "docker run --rm %IMAGE_NAME%:%BUILD_NUMBER% python -c \"import flask; print('Flask berhasil di-install')\""
                    }
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: "${REGISTRY_CREDENTIALS}",
                    usernameVariable: 'DOCKERHUB_USER',
                    passwordVariable: 'DOCKERHUB_TOKEN'
                )]) {
                    script {
                        if (isUnix()) {
                            sh 'printf "%s" "$DOCKERHUB_TOKEN" | docker login -u "$DOCKERHUB_USER" --password-stdin'
                            sh 'docker push "$IMAGE_NAME:$BUILD_NUMBER"'
                            sh 'docker push "$IMAGE_NAME:latest"'
                        } else {
                            bat "docker login -u %DOCKERHUB_USER% -p %DOCKERHUB_TOKEN%"
                            bat "docker push %IMAGE_NAME%:%BUILD_NUMBER%"
                            bat "docker push %IMAGE_NAME%:latest"
                        }
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline selesai. Periksa Console Output untuk detail.'
        }
    }
}

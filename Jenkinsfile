pipeline {

    agent any

    stages {
        stage ('Checkout'){
            steps {
                checkout scm
            }
        }
        stage ('Push'){
            steps {
                script {
                    docker.withRegistry('', 'my_docker') {

                        def customImage = docker.build("tenaciousfoxy/weather")
                        customImage.push()
                    }
                }
            }
        }
    }
}
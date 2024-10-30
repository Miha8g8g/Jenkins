pipeline { 
    options { timestamps() }
    environment {
        DOCKER_CREDS = credentials('Dock_Hub_Tock') // Переменные для доступа к Docker Hub
    }
    agent none 
    stages {  
        
        stage('Check SCM') {  
            agent any 
            steps { 
                checkout scm 
            } 
        } 

        stage('Build') {  
            steps { 
                echo "Building ... ${BUILD_NUMBER}" 
                echo "Build completed" 
            } 
        } 

        stage('Test') { 
            agent { 
                docker { 
                    image 'python:3.9-alpine' 
                    args '-u root' 
                } 
            } 
            steps { 
                sh 'apk add --update python3 py3-pip' 
                sh 'pip install xmlrunner' 
                sh 'pip install -r requirements.txt || echo "No requirements file found"' // установка зависимостей
                sh 'python3 test.py' // запуск тестов, исправление на 'test.py' вместо 'tets.py'
            } 
            post { 
                always { 
                    junit 'test-reports/*.xml' 
                } 
                success { 
                    echo "Application testing successfully completed" 
                } 
                failure { 
                    echo "Oooppss!!! Tests failed!" 
                }  
            } 
        } 

        stage('Publish') {
            agent any
            steps {
                script {
                    sh 'echo $DOCKER_CREDS_PSW | docker login --username $DOCKER_CREDS_USR --password-stdin' // Логин в Docker Hub
                    sh 'docker build -t miha8g8g/notes:latest .' // Сборка Docker-образа
                    sh 'docker push miha8g8g/notes:latest' // Публикация Docker-образа
                }
            } 
        } // stage Publish
    } // stages
} // pipeline


pipeline { 
    options { timestamps() }
    environment {
        DOCKER_CREDS = credentials('Dock_Hub_Tock') // Идентификатор учетных данных Jenkins для Docker Hub
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
                sh 'python3 tets.py' // запуск тестов
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
                    // Проверка, что переменные заполнены
                    echo "Using Docker Username: $DOCKER_CREDS_USR"
                    
                    // Логин в Docker Hub
                    sh 'echo $DOCKER_CREDS_PSW | docker login --username $DOCKER_CREDS_USR --password-stdin' 
                    
                    // Сборка и публикация Docker-образа
                    sh 'docker build -t miha8g8g/notes:latest .' 
                    sh 'docker push miha8g8g/notes:latest' 
                }
            } 
        } // stage Publish
    } // stages
} // pipeline

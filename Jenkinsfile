pipeline {
    agent any
    
    environment {
        PYTHON = 'python3'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Obteniendo el código fuente...'
                checkout scm
            }
        }
        
        stage('Instalar dependencias') {
            steps {
                echo 'Instalando dependencias...'
                sh '''
                    ${PYTHON} -m pip install --upgrade pip
                    ${PYTHON} -m pip install -r requirements.txt
                '''
            }
        }
        
        stage('Ejecutar pruebas') {
            steps {
                echo 'Ejecutando pruebas...'
                sh '''
                    mkdir -p test-results
                    ${PYTHON} -m pytest tests/ -v --junitxml=test-results/junit.xml || true
                '''
            }
            post {
                always {
                    junit 'test-results/*.xml'
                }
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline completado'
        }
    }
}
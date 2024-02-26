pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Hello World'
                sh'''
                python3 test.py
                '''
            }
        }
    }
}

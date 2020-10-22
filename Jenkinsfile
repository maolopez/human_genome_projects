pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh 'python setup.py bdist_wheel' 
            }
        }
    }
}

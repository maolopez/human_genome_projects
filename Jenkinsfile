pipeline {
    agent none 
    stages {
        stage('Build') { 
            steps {
                sh 'python setup.py bdist_wheel' 
            }
        }
    }
}

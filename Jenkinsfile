pipeline {
    agent none 
    stages {
        stage('Build') { 
            steps {
                python setup.py bdist_wheel 
            }
        }
    }
}

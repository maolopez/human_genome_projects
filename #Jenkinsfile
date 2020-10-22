pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh '''which pip
                      which python
                      which python3
                      pip install -U setuptools
                      pip install -U pip
                      pip install -U wheel
                      pip list
                      which pip
                      which python
                      python setup.py bdist_wheel
                    '''
            }
        }
    }
}

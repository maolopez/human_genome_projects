pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh '''pip install -U setuptools
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

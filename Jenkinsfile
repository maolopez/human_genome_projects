pipeline {
    agent any 
    stages {
        stage('build') { 
            steps {
                sh '''PYENV_HOME=$WORKSPACE/.virtualenv/
                      if [ –d $PYENV_HOME ]; 
                      then rm –rf $PYENV_HOME
                      fi
                      virtualenv -v $PYENV_HOME
                      . $PYENV_HOME/bin/activate
                      pip install -r requirements.txt
                      python setup.py bdist_wheel
                    '''
            }
        }
    }
}

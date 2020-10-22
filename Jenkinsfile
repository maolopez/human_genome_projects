pipeline {
    agent any 
    stages {
        stage('prepare') { 
            steps {
                sh '''PYENV_HOME=$WORKSPACE/.human_genome_projects_free_style/
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

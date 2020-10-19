node() {
  stage('checkout') {
    deleteDir()
    checkout scm
  }
  stage('build') {
    sh 'python setup.py bdist_wheel'
  }
}

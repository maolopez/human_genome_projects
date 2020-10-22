node() {
  stage('checkout') {
    deleteDir()
    checkout scm
  }
  stage('build') {
    sh 'python3 setup.py bdist_wheel'
  }
}

pipeline {
  agent any
  stages {
    stage('Stage 1') {
      steps {
        echo 'compiling skype bot'
        sh 'python -m py_compile skype_bot.py'
        echo 'compiling hivebatch'
        sh 'python -m py_compile hivebatch.py'
        echo 'done compiling'
      }
    }
  }
}

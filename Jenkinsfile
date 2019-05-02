pipeline {
  agent {
    docker {
      image 'python:2-alpine'
    }
  }
  stages {
    stage('Stage 1') {
      steps {
        echo 'compiling skype bot'
        sh 'python -m py_compile skype_bot.py'
      }
    }
  }
}

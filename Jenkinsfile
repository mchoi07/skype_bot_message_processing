pipeline {
  agent {
    docker {
      image 'python:2-alpine'
    }
  }
  stages {
    stage('Stage 1') {
      steps {
        echo 'python test'
        sh 'python test.py'
      }
    }
  }
}

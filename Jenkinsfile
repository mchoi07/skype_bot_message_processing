pipeline {
  agent {
    docker {
      image 'python:2-alpine'
    }
  }
  stages {
    stage('Stage 1') {
      steps {
        echo 'python version check'
        sh 'python -V'
      }
    }
  }
}

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
        sh 'python /home/evan/skype_bot_message_processing/test.py'
      }
    }
  }
}

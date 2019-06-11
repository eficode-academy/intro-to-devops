pipeline {
    agent any
    stages {
        stage ("Install requirements") {
            steps {
                sh 'pip install -r source/requirements.txt'
            }
        }
        stage ("Run tests") {
            steps {
                sh 'python -m pytest'
            }

        }
    }
}
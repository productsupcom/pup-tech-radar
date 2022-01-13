env.name                       = "pup-tech-radar"
env.description                = "Project is responsible for updates to our Tech Radar"
env.maintainer                 = "Carsten Neuendorf <carsten.neuendorf@productsup.com>"
env.homepage                   = "https://github.com/productsupcom/pup-tech-radar"
def slack_channel              = "#tech-radar"
env.branch
env.version
env.gitCommitHash
env.gitCommitAuthor
env.gitCommitMessage
env.package_file_name



@Library('jenkins-library@main') _

pipeline {
    agent { label 'jenkins-4'}

    options {
        buildDiscarder(
            logRotator(
                numToKeepStr: '5',
                artifactNumToKeepStr: '5'
            )
        )
        timestamps()
        timeout(time: 1, unit: 'HOURS')
        disableConcurrentBuilds()
        skipDefaultCheckout()
    }

    environment {
        COMPOSE_PROJECT_NAME = "${env.JOB_NAME}_${env.BUILD_ID}"
    }

    stages {
        // Checkout code with tags. The regular scm call does a flat checkout
        // and we need the tags to set the version
        stage("Checkout") {
            steps {
                gitCheckout()
            }
        }

        // set version with the following scheme
        //   tags:   version = <tag>
        //   PR:     version = <latest tag>-<PR number>
        //   branch: version = <latest tag>-<branch name>
        stage('Prepare Info') {
            steps {
                prepareInfo()
            }
        }

        stage ('Build and Publish docker image') {
            when {
                buildingTag()
            }
            steps {
                script {
                    // copy updates files to tech radar server
                }
            }
        }
    }

    // Run post jobs steps
    post {
        // failure sends a failure slack message if the pipeline exit with a failed state
        failure {
            script {
                if (slack_channel) {
                    slackSend message: "${env.name} <${RUN_DISPLAY_URL}|failed>.", channel: "${slack_channel}", color: "danger"
                }
            }
        }
        // success sends a success slack message if the pipeline exit with a success state
        success {
            script {
                if (slack_channel) {
                    slackSend message: "*${env.name} <${RUN_DISPLAY_URL}|success>*. \nAll checks passed for *${env.branch}* \nat commit *${env.gitCommitHash}* \nwhen *${env.gitCommitAuthor}* performed \n> ${env.gitCommitMessage}.", channel: "${slack_channel}", color: "good"
                }
            }
        }
        // cleanup always run last and will trigger for both success and failure states
        cleanup {
            sh "docker-compose down --volumes"
            cleanWs deleteDirs: true
        }
    }
}
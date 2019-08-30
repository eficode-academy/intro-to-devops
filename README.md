# Step by step guide for trainer

# Preparation before the course
1. Make sure you have `docker` and `docker-compose` installed.
1. Create the folder `jenkins-as-code/secrets` and put two files in there: `DOCKER_HUB_PASSWORD` and `DOCKER_HUB_USERNAME`. Put your username and password in these files. If you do not intend to upload to docker hub, just leave the files blank.
1. `cd jenkins-as-code`, then `. ./start.sh` or `DOCKERPATH=$(which docker) docker-compose up -d`
1. You now have a running Jenkins instance with the pipelines in `Jenkinsfile`, `Jenkinsfile2` and `Jenkinsfile3` setup.

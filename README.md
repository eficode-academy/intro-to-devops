# What is this?
This is a companion repository for the Introduction to DevOps course offered by Eficode Praqma.
This repo should be used by the trainer as part of the technical demonstration. It contains the following:

- A docker-compose file for setting up a simple local Jenkins server
- A simple flask app with a simple test
- A Dockerfile for packaging the flask app
- 3 different Jenkinsfiles of varying complexity
- An example of a kubernetes deployment

The story we tell follow these steps, progressing through the Jenkinsfiles:
- Here is a python app
- Let's add a test
- Now we build a Jenkins pipeline to automatically test
- Instead of installing Python on our Jenkins machine, we run the pipeline in a Python container
- Let's build a docker image with our flask app in it, so we know it runs the same way on our production machines
- (Optional) Let's see how it could look if we wanted to deploy our container in a Kubernetes cluster

# Step by step guide for trainer
TODO

# Preparation before the course
1. Make sure you have `docker` and `docker-compose` installed.
1. Create the folder `jenkins-as-code/secrets` and put two files in there: `DOCKER_HUB_PASSWORD` and `DOCKER_HUB_USERNAME`. Put your username and password in these files. If you do not intend to upload to docker hub, just leave the files blank.
1. `cd jenkins-as-code`, then `. ./start.sh` or `DOCKERPATH=$(which docker) docker-compose up -d`
1. You now have a running Jenkins instance with the pipelines in `Jenkinsfile`, `Jenkinsfile2` and `Jenkinsfile3` setup.

# Microdegree DevOps Masterclass

This repository contains the code and configuration files for the Microdegree DevOps Masterclass. It covers the fundamentals of DevOps, including CI/CD, infrastructure as code, containerization, and orchestration.

## Topics Covered

*   Linux Fundamentals
*   Git & GitHub
*   Jenkins
*   Docker
*   Terraform
*   Kubernetes

## Project: Automated CI/CD for a Monolithic Application

This repository includes a hands-on project that demonstrates a complete CI/CD pipeline for a Python-based monolithic application.

The project includes:

*   **Application**: A simple Python Flask application.
*   **Containerization**: The application is containerized using Docker.
*   **CI/CD Pipeline**: A Jenkins pipeline automates the build, test, and deployment process.
*   **Infrastructure as Code**: Terraform is used to provision the necessary infrastructure on AWS (e.g., S3 buckets).
*   **Deployment**: The containerized application is deployed to a Kubernetes cluster.
*   **Networking**: The application is exposed to the internet using a LoadBalancer and is accessible via a custom domain using AWS Route 53.

## Repository Structure

*   [`code/`](code/): Contains the source code for the Python application, [`Dockerfile`](code/Dockerfile:1) for containerization, Kubernetes [`deployment.yaml`](code/deployment.yaml:1), and a [`Jenkinsfile`](code/Jenkinsfile:1) for the CI/CD pipeline.
*   [`Jeenkins-pipelinescripts/`](Jeenkins-pipelinescripts/): Contains example Jenkins pipeline scripts.
*   [`jenkins-2nd-ex/`](jenkins-2nd-ex/): Contains another example of a [`Jenkinsfile`](jenkins-2nd-ex/Jenkinsfile:1).
*   [`jenkins-k8-connection/`](jenkins-k8-connection/): Contains Kubernetes manifests for setting up a Service Account, Role, and RoleBinding to allow Jenkins to communicate with the Kubernetes cluster.
*   [`scripts/`](scripts/): Contains utility scripts, such as for installing Jenkins.
*   [`Terraform/`](Terraform/): Contains Terraform code for provisioning infrastructure.
    *   [`Project-1/`](Terraform/Project-1/): A Terraform project to create an S3 bucket.

### `code/` Directory

This directory is the heart of the project and contains the following files:

*   [`app.py`](code/app.py:1): A simple "Hello, World" Flask application that serves as the monolithic application for this project.
*   [`Dockerfile`](code/Dockerfile:1): This file contains the instructions to build a Docker image for the Flask application. It uses a Python base image, copies the application code, and installs the dependencies from [`requirements.txt`](code/requirements.txt:1).
*   [`deployment.yaml`](code/deployment.yaml:1): A Kubernetes manifest that defines a Deployment and a Service. The Deployment manages the pods running the containerized application, and the Service exposes the application through a LoadBalancer.
*   [`Jenkinsfile`](code/Jenkinsfile:1): This file defines the CI/CD pipeline using Jenkins. The pipeline has stages for building the Docker image, pushing it to a container registry, and deploying the application to the Kubernetes cluster.
*   [`requirements.txt`](code/requirements.txt:1): This file lists the Python dependencies for the application (i.e., Flask).

### Other Directories

*   [`Jeenkins-pipelinescripts/`](Jeenkins-pipelinescripts/): This directory contains additional examples of Jenkins pipeline scripts. These can be used as a reference for creating more complex pipelines.
*   [`jenkins-2nd-ex/`](jenkins-2nd-ex/): This directory provides another example of a [`Jenkinsfile`](jenkins-2nd-ex/Jenkinsfile:1), showcasing a different pipeline structure or set of stages.
*   [`jenkins-k8-connection/`](jenkins-k8-connection/): This directory is crucial for enabling Jenkins to communicate with your Kubernetes cluster. It contains the following Kubernetes manifest files:
    *   [`sa.yaml`](jenkins-k8-connection/sa.yaml:1): Creates a ServiceAccount named `jenkins`.
    *   [`role.yaml`](jenkins-k8-connection/role.yaml:1): Defines a Role with permissions to manage deployments, services, and pods in the default namespace.
    *   [`rb.yaml`](jenkins-k8-connection/rb.yaml:1): Creates a RoleBinding that grants the `jenkins` ServiceAccount the permissions defined in the `jenkins-role`.
*   [`scripts/`](scripts/): This directory contains helper scripts. For example, [`jenkins.sh`](scripts/jenkins.sh:1) could be a script to automate the installation and setup of a Jenkins server.
*   [`Terraform/`](Terraform/): This directory holds the Infrastructure as Code (IaC) for the project. It includes a project to create an S3 bucket, which could be used for storing build artifacts or Terraform state.

## In-Depth Topics

### Linux Fundamentals

A foundational understanding of the Linux command line is essential for any DevOps engineer. Here are some of the most common commands:

*   **File System Navigation:**
    *   `ls`: List directory contents. (e.g., `ls -la` to show all files with details).
    *   `cd`: Change the current directory. (e.g., `cd /var/log`).
    *   `pwd`: Print the current working directory.
*   **File & Directory Management:**
    *   `mkdir`: Create a new directory. (e.g., `mkdir my-project`).
    *   `rm`: Remove files or directories. (e.g., `rm myfile.txt`, `rm -r my-directory`).
    *   `cp`: Copy files or directories. (e.g., `cp source.txt destination.txt`).
    *   `mv`: Move or rename files or directories. (e.g., `mv old-name.txt new-name.txt`).
    *   `touch`: Create an empty file or update the timestamp of an existing file.
*   **File Content:**
    *   `cat`: Concatenate and display the content of files.
    *   `less`/`more`: View file content page by page.
    *   `head`/`tail`: View the beginning or end of a file.
*   **Searching:**
    *   `grep`: Search for a pattern in a file. (e.g., `grep "error" logfile.log`).
    *   `find`: Search for files in a directory hierarchy.
*   **Permissions:**
    *   `chmod`: Change the permissions of a file or directory (e.g., `chmod +x script.sh`).
    *   `chown`: Change the owner of a file or directory.

### Git & GitHub

Git is a distributed version control system that is essential for tracking changes in source code during software development. GitHub is a web-based hosting service for version control using Git.

*   **Basic Git Commands:**
    *   `git init`: Initialize a new Git repository.
    *   `git clone <repository-url>`: Clone a repository onto your local machine.
    *   `git add <file>`: Add a file to the staging area.
    *   `git commit -m "<commit-message>"`: Commit the staged changes with a message.
    *   `git push`: Push the committed changes to the remote repository.
    *   `git pull`: Pull the latest changes from the remote repository.
    *   `git status`: Show the status of the working directory and staging area.
*   **Branching:**
    *   `git branch`: List all branches.
    *   `git branch <branch-name>`: Create a new branch.
    *   `git checkout <branch-name>`: Switch to a different branch.
    *   `git merge <branch-name>`: Merge the specified branch into the current branch.

### Jenkins

Jenkins is an open-source automation server that enables developers to reliably build, test, and deploy their software. It is a cornerstone of CI/CD.

*   **Key Concepts:**
    *   **Pipeline:** A suite of plugins that supports implementing and integrating continuous delivery pipelines into Jenkins.
    *   **Jenkinsfile:** A text file that contains the definition of a Jenkins Pipeline and is checked into source control.
    *   **Stages:** A block that contains a series of steps in a pipeline. (e.g., Build, Test, Deploy).
    *   **Steps:** A single task that tells Jenkins what to do.
*   **Example `Jenkinsfile` Stage:**

    ```groovy
    stage('Build') {
        steps {
            sh 'echo "Building..."'
            // Add build commands here
        }
    }
    ```

### Docker

Docker is a platform that enables developers to containerize applications. Containers are lightweight, portable, and self-sufficient, and they can run on any machine that has Docker installed.

*   **Basic Docker Commands:**
    *   `docker build -t <image-name>:<tag> .`: Build a Docker image from a `Dockerfile`.
    *   `docker run -d -p <host-port>:<container-port> <image-name>:<tag>`: Run a Docker container in detached mode and map a port.
    *   `docker ps`: List all running containers.
    *   `docker images`: List all Docker images.
    *   `docker stop <container-id>`: Stop a running container.
    *   `docker rm <container-id>`: Remove a container.
*   **Example `Dockerfile`:**

    ```dockerfile
    FROM python:3.8-slim

    WORKDIR /app

    COPY requirements.txt .
    RUN pip install -r requirements.txt

    COPY . .

    CMD ["python", "app.py"]
    ```

### Terraform

Terraform is an open-source infrastructure as code (IaC) tool that allows you to build, change, and version infrastructure safely and efficiently.

*   **Basic Terraform Commands:**
    *   `terraform init`: Initialize a new or existing Terraform configuration.
    *   `terraform plan`: Create an execution plan.
    *   `terraform apply`: Apply the changes required to reach the desired state of the configuration.
    *   `terraform destroy`: Destroy the Terraform-managed infrastructure.
*   **Example Terraform Configuration:**

    ```hcl
    resource "aws_s3_bucket" "b" {
      bucket = "my-tf-test-bucket"
      acl    = "private"

      tags = {
        Name        = "My bucket"
        Environment = "Dev"
      }
    }
    ```

### Kubernetes

Kubernetes (K8s) is an open-source system for automating deployment, scaling, and management of containerized applications.

*   **Key Concepts:**
    *   **Pod:** The smallest and simplest unit in the Kubernetes object model that you create or deploy.
    *   **Deployment:** A controller that provides declarative updates for Pods and ReplicaSets.
    *   **Service:** An abstract way to expose an application running on a set of Pods as a network service.
    *   **kubectl:** The command-line tool for interacting with a Kubernetes cluster.
*   **Basic kubectl Commands:**
    *   `kubectl apply -f <filename>`: Apply a configuration to a resource by filename.
    *   `kubectl get pods`: List all pods.
    *   `kubectl get deployments`: List all deployments.
    *   `kubectl get services`: List all services.
    *   `kubectl describe pod <pod-name>`: Show detailed information about a pod.
*   **Example Kubernetes Deployment:**

    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-app
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: my-app
      template:
        metadata:
          labels:
            app: my-app
        spec:
          containers:
          - name: my-app
            image: my-app:1.0
            ports:
            - containerPort: 5000
    ```

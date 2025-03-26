This repository contains my Lab 7 - Kubernetes solution for the Introduction to DevOps module in the third year of the Computer Science course at TU Dublin.

# Overview

The goal of this lab was to deploy a simple Flask web application inside a Kubernetes cluster using Minikube. The lab focused on core DevOps practices such as container orchestration, cluster provisioning, deployment using YAML configuration files, and exposing services using Kubernetes networking components.

The Kubernetes cluster was set up using Minikube within a Virtual Machine configured via Vagrant. The application was built as a Docker image and deployed using a Kubernetes Deployment and Service. The service was accessed externally using a port-forwarding Python script to enable browser access through the host machine.

# Key Tasks

- Installed and configured Docker, Minikube, and kubectl inside a Vagrant-managed VM
- Built a Docker image for a simple Flask app inside the Minikube Docker environment
- Created a Kubernetes Deployment (`flaskapp.yml`) to manage the Flask container
- Exposed the application externally via a LoadBalancer Service (`service.yml`)
- Used `minikube tunnel` to obtain an external IP for the LoadBalancer
- Forwarded VM traffic using a custom `port-forward.py` script to access the app from the browser
- Verified that the Flask app is running correctly via both terminal (`curl`) and browser

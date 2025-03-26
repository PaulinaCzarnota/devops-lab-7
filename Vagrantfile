# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
  config.vm.box = "debian/bookworm64"

  # Forward port 5050 on the guest to 8080 on the host machine
  config.vm.network "forwarded_port", guest: 5050, host: 8080

  # Give ourselves 20GB of disk space
  config.vm.disk :disk, size: "20GB", primary: true

  # We'll give ourselves 2GB of RAM
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2046"
  end

  # Provision the VM by installing Docker, Minikube and Kubelet
  config.vm.provision "shell", inline: <<-SHELL
    apt update
    apt upgrade -y
    apt install -y docker.io python-is-python3
    groupadd docker
    usermod -aG docker vagrant
    wget https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
    install minikube-linux-amd64 /usr/local/bin/minikube
    wget "https://dl.k8s.io/release/v1.32.3/bin/linux/amd64/kubectl"
    install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
    rm -rf ~/*
  SHELL
end
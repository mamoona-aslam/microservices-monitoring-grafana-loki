Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"

  # Define a hostname for your VM
  config.vm.hostname = "ansible-vm"

  # Port forwarding
  config.vm.network "forwarded_port", guest: 3000, host: 3000  # Grafana
  config.vm.network "forwarded_port", guest: 3100, host: 3100  # Loki
  config.vm.network "forwarded_port", guest: 5001, host: 5001  # Product Service
  config.vm.network "forwarded_port", guest: 5002, host: 5002  # Order Service
  config.vm.network "forwarded_port", guest: 5003, host: 5003  # User Service

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "4096"
    vb.cpus = 2
  end

  # Sync a folder from your host machine to the guest VM
  config.vm.synced_folder "./microservices", "/home/vagrant/microservices", owner: "vagrant", group: "vagrant", mount_options: ["dmode=775,fmode=664"]

    # Ansible provisioning
  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "playbook.yml"
    #ansible.provisioning_path = "/vagrant"
    ansible.inventory_path = "inventory"
    # Run as root
    ansible.become = true

    # Limit the Ansible run to this single VM
    ansible.limit = "all"

  end

  # Shell provisioning for Docker and Docker Compose
  config.vm.provision "shell", inline: <<-SHELL
    # Update package list and install Docker
    sudo apt-get update
    sudo apt-get install -y docker.io docker-compose
    

    # Start Docker service
    sudo systemctl start docker
    sudo systemctl enable docker

    # Change to the directory with Docker Compose file
    cd /home/vagrant/microservices/dockerfiles
    # Run Docker Compose

    sudo docker-compose up --build -d
  SHELL
end

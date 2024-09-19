# **Microservices Monitoring with Grafana Loki**

This repository provides a complete setup for monitoring microservices using **Grafana** and **Loki**, with **Promtail** as the log shipper. It uses **Vagrant**, **Ansible**, and **Docker** to automate the entire infrastructure deployment.

## **Table of Contents**
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Testing the Microservices](#testing-the-microservices)
- [How It Works](#how-it-works)
- [License](#license)

## **Project Structure**

This section outlines the structure of the project directory, including the purpose of each component.

```bash
project_directory/
├── Vagrantfile                       # Vagrant configuration file for setting up the VM
├── playbook.yml                      # Main Ansible playbook for provisioning
├── inventory                         # Ansible inventory file specifying hosts
├── README.md                         # Documentation file
├── dashboard.json.j2                 # Template for the Grafana dashboard
├── LICENSE                           # GPLv3 License
├── microservices/                    # Directory containing microservices and their configurations
│   └── dockerfiles/                  # Contains Docker-related files for microservices
│       ├── docker-compose.yml        # Docker Compose file for orchestrating microservices
│       ├── Dockerfile.order          # Dockerfile for the Order service
│       ├── Dockerfile.product        # Dockerfile for the Product service
│       ├── Dockerfile.user           # Dockerfile for the User service
│       └── services-py/              # Python source files and dependencies for microservices
│           ├── order_service.py      # Flask application for handling orders
│           ├── product_service.py    # Flask application for managing products
│           ├── requirements.txt      # Python dependencies for the microservices
│           └── user_service.py       # Flask application for user authentication
└── roles/                            # Directory containing Ansible roles for service setup
    ├── common/                       # Common role with shared tasks and defaults
    │   ├── defaults/                 # Default variables for the common role
    │   │   └── main.yml              # Main defaults file for common tasks
    │   └── tasks/                    # Tasks to be executed in the common role
    │       └── main.yml              # Main tasks file for common role execution
    ├── grafana/                      # Role for setting up Grafana
    │   ├── defaults/                 # Default variables for Grafana
    │   │   └── main.yml              # Main defaults file for Grafana role
    │   └── tasks/                    # Tasks for installing and configuring Grafana
    │       └── main.yml              # Main tasks file for Grafana role execution
    ├── loki/                         # Role for setting up Loki
    │   ├── defaults/                 # Default variables for Loki
    │   │   └── main.yml              # Main defaults file for Loki role
    │   ├── tasks/                    # Tasks for installing and configuring Loki
    │   │   └── main.yml              # Main tasks file for Loki role execution
    │   └── templates/                # Templates for Loki configuration
    │        ├── loki-config.yaml.j2  # Jinja2 template for Loki's configuration file
    │        └── loki.service.j2      # Jinja2 template for Loki's systemd service file
    └── promtail/                     # Role for setting up Promtail
        ├── defaults/                 # Default variables for Promtail
        │   └── main.yml              # Main defaults file for Promtail role
        ├── tasks/                    # Tasks for installing and configuring Promtail
        │   └── main.yml              # Main tasks file for Promtail role execution
        └── templates/                # Templates for Promtail configuration
            ├── promtail-config.yaml.j2 # Jinja2 template for Promtail's configuration file
            └── promtail.service.j2    # Jinja2 template for Promtail's systemd service file
```
## Prerequisites

Tested on Debian 12 / Ubuntu 20.04 or later. Before starting, ensure you have the following installed:

- **Vagrant** (>= 2.4)
- **VirtualBox** (>= 7.0)
- **Ansible** (installed automatically by Vagrant)
- **Docker and Docker Compose** (installed automatically in the VM)


# Getting Started
Follow these steps to set up the monitoring environment:

1. Clone the Repository:

```bash
git clone https://github.com/mamoona-aslam/microservices-monitoring-grafana-loki.git
cd microservices-monitoring-grafana-loki
```

2. Start the Environment: Use Vagrant to spin up the VM and provision everything:

```bash
vagrant up
```
This will:

- Create a Virtual Machine with Ubuntu.
- Install Docker, Docker Compose, and the required services (Grafana, Loki, Promtail).
- Deploy the microservices using Docker.

3. Access Grafana:

- Grafana can be accessed at http://localhost:3000.
- Default credentials: admin / admin.

# Testing the Microservices

You can test the microservices using curl commands:

- Product Service (running on port 5001):

```bash
curl http://localhost:5001/products
```

- User Service (running on port 5003):

```bash
curl -X POST -H "Content-Type: application/json" -d '{"username": "testuser"}' http://localhost:5003/login
```

- Order Service (running on port 5002):

```bash
curl -X POST -H "Content-Type: application/json" -d '{"id": 123}' http://localhost:5002/order
```

## How It Works

This project uses Vagrant to spin up a Virtual Machine (VM), which is automatically provisioned with Ansible to install and configure the following components:

- **Docker & Docker Compose**: Containers for the microservices are managed using Docker Compose.
- **Grafana**: Used to visualize logs and metrics.
- **Loki**: Collects and indexes the logs from microservices.
- **Promtail**: Collects logs from Docker containers and forwards them to Loki.

The microservices are simple Python Flask applications, each running in its own Docker container. Logs are collected by Promtail and sent to Loki for aggregation. These logs can then be visualized in Grafana.

# Services Overview:

- **Grafana** (Port 3000): Dashboard visualization.

- **Loki** (Port 3100): Centralized log aggregation.

- **Promtail**: Log collection from microservices.

# License
This project is licensed under the GPLv3 License. See the **LICENSE** file for details.
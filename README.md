[![Github Actions](https://github.com/mathewsrc/Dio-Bank-System/actions/workflows/main.yml/badge.svg)](https://github.com/mathewsrc/Dio-Bank-System/actions/workflows/main.yml)

# Potência Tech powered by iFood | Ciências de Dados com Python

## Dio-Bank-System

Creating a Bank system with Python (Criando um Sistema Bancário com Python)

This project simulates a bank system where you can deposit, withdraw, create accounts, create users, etc.

## Running this app (Rodando este app)

You can run this app using the bash command-line interface or by using Docker:

1. Command-line

   ```bash
   python main.py
   ```
2. Docker

    Build an image from the Dockerfile
    ```bash
    docker build --tag app-docker .
    ```
  
    Run the container
    ```bash
    docker run -it --rm app-docker python main.py
    ```
   
> **Note**
> For windows users install [Docker Desktop](https://www.docker.com/products/docker-desktop/)

A third option is to use the Makefile file commands on the terminal. The Makefile contains options for:

1. Setup virtual environment
   ```bash
   make setup
   ```
   
2. Install requirements
    ```bash
    make install
    ```

3. Format code
   ```bash
   make format
   ```

4. Lint code
    ```bash
    make lint
    ```

5. Run tests
    ```bash
    make test
     ```
6. Build Docker image
    ```bash
   make docker-build
   ```

7. Run Docker container
    ```bash
   make docker-run
   ```

8. Delete Docker image
    ```bash
   make docker-cleanup
   ```


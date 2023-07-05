[![Github Actions](https://github.com/mathewsrc/Dio-Bank-System/actions/workflows/main.yml/badge.svg)](https://github.com/mathewsrc/Dio-Bank-System/actions/workflows/main.yml)

# Potência Tech powered by iFood | Ciências de Dados com Python

## Dio-Bank-System

Creating a Bank system with Python (Criando um Sistema Bancário com Python)

This project simulates a bank system where you can deposit, withdraw, create accounts, create users, etc.

## Preview



https://github.com/mathewsrc/Dio-Bank-System/assets/94936606/862f3c70-0379-48ed-9c99-83208720356b



## Usage (Rodando este app)

You can run this app using the bash command-line interface or by using Docker:

### 1. Command-line

   1.1 Creating a virtual environment

   ```bash
   python -m venv .env
   ```

   1.2 Activating the virtual environment 

   Linux
   ```bash
   source .env/bin/activate
   ```

   Windows
   ```bash
   source .env/Scripts/activate
   ```

   1.3 Installing the dependencies

   ```bash
   pip install --upgrade pip  && pip install -r requirements.txt
   ```

   1.4 Running the app
   
   ```bash
   python main.py
   ```

 ### 2. Docker

Docker is a tool used to develop, run, and ship containers. Containers provide portability (runs on any infrastructure), reproducibility (runs the same anywhere), and security (isolates the application from the host).

   Building an image from the Dockerfile
   ```bash
   docker build --tag app-docker .
   ```
  
   Running the Docker container
   ```bash
   docker run -it --rm app-docker python main.py
   ```
   
> **Note**
> For Windows users install [Docker Desktop](https://www.docker.com/products/docker-desktop/)


### A third option is to use the Linux make utility. 

The Make utility is a software tool for managing and maintaining computer programs. It reads its instruction from a file called Makefile. The Makefile is a way of automating software building and tasks. With Makefile we can write complex commands with a given name.

The Makefile contains options for:

> **Note**
> Windows users will need to install the Makefile. More information can be founded here: https://earthly.dev/blog/makefiles-on-windows/

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

9. Run app on terminal
     ```bash
   make run-app
   ```


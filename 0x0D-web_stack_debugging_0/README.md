# System-Engineering Devops - Web stack debugging #0

## Description
This project is part of the Web Stack Debugging series which aims to train in the art of debugging. In this task, you will need to get Apache to run on a Docker container and to return a page containing "Hello Holberton" when querying the root of it.

## Project Structure
| Task | Description | Source Code |
|-----------------------------------|------------------------------------------------------|-----------------------------------------------|
| 0. Give me a page! | Debug the Docker container to get Apache running and serving a "Hello Holberton" page at the root. | [0-give_me_a_page](./0-give_me_a_page) |

## Objective
This project involves debugging a Docker container to get Apache running and serving a "Hello Holberton" page at the root.

## Features
**Debug the Docker container to get Apache running and serving a "Hello Holberton" page at the root.**

**Debug and fix Apache within the container:** 

- Write the Bash script that performs these actions.

   - Install Apache if it's not installed:
    - Ensure Apache is started:
    - Create an HTML file to serve:


## Requirements

- All your files will be interpreted on Ubuntu 14.04 LTS
- All your files should end with a new line
- All your Bash script files must be executable
- Your Bash scripts must pass Shellcheck without any error
- Your Bash scripts must run without error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`

## How to Use
**To complete this project, you need to have Docker installed. Follow the installation instructions for your OS:**

## Installation
- [Mac OS](https://docs.docker.com/docker-for-mac/install/)
- [Windows](https://docs.docker.com/docker-for-windows/install/)
- [Ubuntu 14.04](https://docs.docker.com/engine/install/ubuntu/) (Note that Docker for Ubuntu 14 is deprecated)
- [Ubuntu 16.04](https://docs.docker.com/engine/install/ubuntu/)

1. **Run the Docker container:**
    ```bash
    docker run -p 8080:80 -d -it holbertonschool/265-0
    ```
2. **Check the status of the container**:
    ```bash
    docker ps
    ```
    
3. **Access the running container:**
    ```bash
    docker exec -ti <container_id> /bin/bash
    ```

3. **Execute the script inside the container to fix the issue:**
    ```bash
    ./0-give_me_a_page
    ```

5. **Exit the container** and test the page:
    ```bash
    curl 0:8080
    ```

**The page should display "Hello Holberton".**


### Making the Script Executable

Make sure your script is executable by running:

```bash
chmod +x 0-give_me_a_page
```

## Tasks

### 0. Give me a page!

In this first debugging project, you will need to get Apache to run on the container and to return a page containing "Hello Holberton" when querying the root of it.

#### Example

```bash
vagrant@vagrant:~$ docker run -p 8080:80 -d -it holbertonschool/265-0
47ca3994a4910bbc29d1d8925b1c70e1bdd799f5442040365a7cb9a0db218021
vagrant@vagrant:~$ docker ps
CONTAINER ID        IMAGE                   COMMAND             CREATED             STATUS              PORTS                  NAMES
47ca3994a491        holbertonschool/265-0   "/bin/bash"         3 seconds ago       Up 2 seconds        0.0.0.0:8080->80/tcp   vigilant_tesla
vagrant@vagrant:~$ curl 0:8080
curl: (52) Empty reply from server
vagrant@vagrant:~$
```

Here we can see that after starting my Docker container, I `curl` the port `8080` mapped to the Docker container port `80`, it does not return a page but an error message. Note that you might also get the error message `curl: (52) Empty reply from server.`

```bash
vagrant@vagrant:~$ curl 0:8080
Hello Holberton
vagrant@vagrant:~$
```

After connecting to the container and fixing whatever needed to be fixed (here is your mission), you can see that curling port 80 return a page that contains "Hello Holberton." Paste the command(s) you used to fix the issue in your answer file.

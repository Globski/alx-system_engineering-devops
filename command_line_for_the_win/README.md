# System-Engineering DevOps - CMD CHALLENGE

## Description

The CMD CHALLENGE project is designed to improve your Bash command line skills through a series of progressively challenging tasks in Bash scripting, including loops, conditionals, parsing, and file operations. The game involves solving complex problems using Bash commands and scripts to test and improve your command line skills. You'll gain hands-on experience with essential Bash scripting techniques.

## Environment
- Ubuntu 20.04 LTS environment, 
- [Command Challenge](https://cmdchallenge.com/)

## Learning Objectives

- Improve your Bash and command line skills.
- Develop scripting and task automation skills.
- Learn to use SFTP for secure file transfers.

 ### Requirements
- Use the SFTP command-line tool to upload local screenshots to the sandbox environment.
- **Bash Version:** 
- **SFTP Configuration:**
- **Sandbox Environment Details:** [hostname, username, and password]

## How to Use

**Complete Tasks:**
   - Follow the tasks outlined [Command Challenge](https://cmdchallenge.com/). As you complete each task, take screenshots of your terminal showing the completed tasks.
   - Obtain the hostname, username, and password for the sandbox environment where you'll upload your screenshots.

**Upload Screenshots:**
   - Use the SFTP command-line tool to upload your screenshots to the sandbox environment. Instructions for this process are provided below.

## SFTP File Transfer Instructions

To submit your screenshots, you need to transfer them to the sandbox environment using SFTP. Follow these steps:

1. **Take Screenshots:** Capture images of the completed tasks as specified.

2. **Open Terminal:** Open a terminal or command prompt on your local machine.

3. **Connect to Sandbox Environment via SFTP:**
   - Use the following command to connect:
     ```bash
     sftp username@hostname
     ```
   - Replace `username` and `hostname` with your sandbox credentials.

4. **Navigate to Directory:**
   ```bash
   cd /root/alx-system_engineering-devops/command_line_for_the_win/
   ```

5. **Upload Screenshots:**
- Use the `put` command to upload your screenshots:
   ```bash
   put <local_screenshot_file>
   ```
   Example:
     ```bash
     put 0-first_9_tasks.jpg
     put 1-next_9_tasks.jpg
     put 2-next_9_tasks.jpg
     ```

6. **Verify Upload:**
   - Ensure the files are uploaded correctly by listing the contents sandbox directory:
   ```bash
     ls
    ```

## Tasks

1. **Task 0: First 九 Tasks**
   - **Objective:** Complete the first 9 tasks.
   - **File Name for Screenshot:** `0-first_9_tasks.jpg` or `0-first_9_tasks.png`

2. **Task 1: Reach חי Completed Tasks**
   - **Objective:** Complete the next 9 tasks to reach a total of 18 completed tasks.
   - **File Name for Screenshot:** `1-next_9_tasks.jpg` or `1-next_9_tasks.png`

3. **Task 2: Reach the Perfect Cube, 27**
   - **Objective:** Complete the next 9 tasks to reach a total of 27 completed tasks.
   - **File Name for Screenshot:** `2-next_9_tasks.jpg` or `2-next_9_tasks.png`

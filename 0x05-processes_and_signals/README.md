# System-Engineering Devops - Processes and Signals

## Description

This project focuses on the concepts of processes and signals in shell scripting. Understanding how processes work and how signals can be used to communicate with them is crucial for effective process management and automation.

## Project Structure

| Task                              | Description                                                               | Source Code                                   |
|-----------------------------------|---------------------------------------------------------------------------|-----------------------------------------------|
| What is my PID                    | Display the PID of the Bash script itself.                                | [0-what-is-my-pid](0-what-is-my-pid)         |
| List your processes               | Display a list of currently running processes.                            | [1-list_your_processes](1-list_your_processes)|
| Show your Bash PID                | Display lines containing the word "bash" to get the PID of the Bash process. | [2-show_your_bash_pid](2-show_your_bash_pid) |
| Show your Bash PID made easy      | Display the PID and process name of all processes containing the word "bash". | [3-show_your_bash_pid_made_easy](3-show_your_bash_pid_made_easy) |
| To infinity and beyond            | Display "To infinity and beyond" indefinitely with a sleep between each iteration. | [4-to_infinity_and_beyond](4-to_infinity_and_beyond) |
| Don't stop me now!                | Stop the process started by "To infinity and beyond" using kill.          | [5-dont_stop_me_now](5-dont_stop_me_now)    |
| Stop me if you can                | Stop the process started by "To infinity and beyond" without using kill.  | [6-stop_me_if_you_can](6-stop_me_if_you_can)|
| Highlander                        | Display "To infinity and beyond" indefinitely, and respond to SIGTERM with "I am invincible!!!". | [7-highlander](7-highlander)                 |
| Beheaded process                  | Kill the process started by "Highlander".                                 | [8-beheaded_process](8-beheaded_process)     |
| Process and PID file              | Create a PID file and display messages indefinitely, responding to signals. | [100-process_and_pid_file](100-process_and_pid_file) |
| Manage my process                 | Write an init script to manage a background process.                      | [101-manage_my_process](101-manage_my_process), [manage_my_process](manage_my_process) |
| Zombie                            | Create zombie processes in a C program.                                   | [102-zombie.c](102-zombie.c)                 |

## Environment

- Ubuntu 20.04 LTS.
- Shellcheck (version 0.7.0)
- Betty style.

## Requirements

- All files should end with a new line.
- All Bash script files must be executable.
- The first line of all Bash scripts should be `#!/usr/bin/env bash`.
- C programs must comply with the Betty style.
- Shell scripts must pass Shellcheck (version 0.7.0) without any error.

## Learning Objectives
Upon completing this project, you should be able to explain:

- What is a PID and how to find it.
- How to manage processes using Bash scripts.
- Signal handling in Bash (What are the 2 signals that cannot be ignored).
- Process management techniques such as creating background processes and managing PID files.
- How to create and manage zombie processes in C.

## How to use

**Installation**
For Ubuntu/Debian:

```bash
sudo apt-get update
sudo apt-get install shellcheck
```

**Using ShellCheck**

Once ShellCheck is installed, you can run it on a shell script by using the command:
```bash
shellcheck your_script.sh
```

**Clone the repository:**
   ```bash
   git clone <repository_url>
   ```

**Navigate to the project directory:**
   ```bash
   cd 0x05-processes_and_signals
   ```

**Make the scripts executable:**
   ```bash
   chmod +x <script_name>
   ```

**Run the scripts:**
   ```bash
   ./<script_name>
   ```

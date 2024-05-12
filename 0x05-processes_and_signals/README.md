# System-Engineering Devops - Processes and Signals

## Description
In this project, you'll explore the concepts of processes and signals in the context of shell scripting. Understanding how processes work and how signals can be used to communicate with them is crucial for effective process management and automation.

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

- All files will be interpreted on Ubuntu 20.04 LTS.
- Shell scripts must pass Shellcheck (version 0.7.0) without any error.
- C programs must comply with the Betty style.

## Requirements

- All files should end with a new line.
- All Bash script files must be executable.
- The first line of all Bash scripts should be `#!/usr/bin/env bash`.
- The second line of all Bash scripts should be a comment explaining what the script is doing.

## Learning Objectives
Upon completing this project, you should be able to explain:

- What is a PID and how to find it.
- How to manage processes using Bash scripts.
- Signal handling in Bash (What are the 2 signals that cannot be ignored).
- Process management techniques such as creating background processes and managing PID files.
- How to create and manage zombie processes in C.

## Additional Notes

- Ensure proper cleanup and termination of processes to avoid system instability.
- Practice safe handling of signals to prevent unexpected behavior and ensure system reliability.

## How to Use

1. Clone the repository to your local machine.
2. Navigate to the project directory `0x05-processes_and_signals`.
3. Ensure all scripts are executable using `chmod +x script_name`.
4. Execute each script with appropriate arguments to perform the specified tasks.

Happy scripting!

# System-Engineering Devops - Loops, Conditions, and Parsing

## Description
In this project, you'll delve into the world of shell scripting, focusing on loops, conditions, and parsing. By mastering these concepts, you'll be able to create efficient and robust Bash scripts for automating various tasks.

## Project Structure

| Task                              | Description                                          | Source Code                                   |
|-----------------------------------|------------------------------------------------------|-----------------------------------------------|
| Create a SSH RSA key pair         | Generate a RSA key pair for secure SSH connections.  | [0-RSA_public_key.pub](0-RSA_public_key.pub) |
| For Best School loop              | Display "Best School" using a for loop.              | [1-for_best_school](1-for_best_school)       |
| While Best School loop            | Display "Best School" using a while loop.            | [2-while_best_school](2-while_best_school)   |
| Until Best School loop            | Display "Best School" using an until loop.           | [3-until_best_school](3-until_best_school)   |
| If 9, say Hi!                     | Display "Hi" on the 9th iteration of "Best School". | [4-if_9_say_hi](4-if_9_say_hi)               |
| 4 bad luck, 8 is your chance      | Display "bad luck" on the 4th iteration and "good luck" on the 8th iteration. | [5-4_bad_luck_8_is_your_chance](5-4_bad_luck_8_is_your_chance) |
| Superstitious numbers             | Display numbers with superstitions at specific iterations. | [6-superstitious_numbers](6-superstitious_numbers) |
| Clock                             | Display the time in hours and minutes.              | [7-clock](7-clock)                           |
| For ls                            | List files with names after the first dash.         | [8-for_ls](8-for_ls)                         |
| To file, or not to file           | Check if a file exists and display its properties.   | [9-to_file_or_not_to_file](9-to_file_or_not_to_file) |
| FizzBuzz                          | Implement the FizzBuzz algorithm.                   | [10-fizzbuzz](10-fizzbuzz)                   |
| Read and cut                      | Display specific fields from /etc/passwd.           | [100-read_and_cut](100-read_and_cut)         |
| Tell the story of passwd          | Display details of users from /etc/passwd.          | [101-tell_the_story_of_passwd](101-tell_the_story_of_passwd) |
| Let's parse Apache logs           | Parse Apache logs to display IP and status code.    | [102-lets_parse_apache_logs](102-lets_parse_apache_logs) |
| Dig the data                      | Group visitors by IP and HTTP status code.          | [103-dig_the-data](103-dig_the-data)         |

## Environment

- All files will be interpreted on Ubuntu 20.04 LTS.
- Shell scripts must pass Shellcheck without errors.

## Requirements

- All files should end with a new line.
- All Bash script files must be executable.
- Your Bash script must pass Shellcheck (version 0.7.0) without any error
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`.
- The second line of all Bash scripts should be a comment explaining what the script is doing.

## Learning Objectives

After completing this project, you should be able to explain:

- How to create SSH keys for secure connections.
- Usage of loops (for, while, until) and conditionals (if, else, elif).
- Parsing techniques using cut, case statements, and file comparison operators.
- Writing portable Bash scripts (What is the advantage of using #!/usr/bin/env bash over #!/bin/bash).
- Importance of passing Shellcheck for script validation.

## Additional Note

- Avoid disrupting system functionality by reverting any changes made to configuration settings after testing.

## How to Use

1. Clone the repository to your local machine.
2. Navigate to the project directory `0x04-loops_conditions_and_parsing`.
3. Ensure all scripts are executable using `chmod +x script_name`.
4. Execute each script with appropriate arguments to perform the specified tasks.

Happy scripting!

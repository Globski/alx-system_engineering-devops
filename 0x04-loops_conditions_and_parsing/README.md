# System-Engineering Devops - Loops, Conditions, and Parsing

## Description
This project is designed to teach fundamental concepts of Bash scripting, including loops, condition statements, and parsing. The tasks focus on creating scripts that utilize various types of loops (for, while, until) and conditional statements (if, elif, else, case). By the end of this project, you will be able to handle different scripting scenarios in a Unix-based environment.

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

## Learning Objectives

After completing this project, you should be able to explain:

- How to create SSH keys for secure connections.
- Usage of loops (for, while, until) and conditionals (if, else, elif).
- Parsing techniques using cut, case statements, and file comparison operators.
- Writing portable Bash scripts (What is the advantage of using #!/usr/bin/env bash over #!/bin/bash).
- Importance of passing Shellcheck for script validation.

## Tasks

### 0. Create a SSH RSA key pair
- **File:** `0-RSA_public_key.pub`
- **Description:** Create an RSA key pair.

### 1. For Best School loop
- **File:** `1-for_best_school`
- **Description:** Write a Bash script that displays "Best School" 10 times using a `for` loop.

### 2. While Best School loop
- **File:** `2-while_best_school`
- **Description:** Write a Bash script that displays "Best School" 10 times using a `while` loop.

### 3. Until Best School loop
- **File:** `3-until_best_school`
- **Description:** Write a Bash script that displays "Best School" 10 times using an `until` loop.

### 4. If 9, say Hi!
- **File:** `4-if_9_say_hi`
- **Description:** Write a Bash script that displays "Hi" for the 9th iteration, and "Best School" for the rest of the iterations, using a `while` loop and an `if` statement.

### 5. 4 bad luck, 8 is your chance
- **File:** `5-4_bad_luck_8_is_your_chance`
- **Description:** Write a Bash script that loops from 1 to 10 and:
  - Displays "bad luck" for the 4th iteration.
  - Displays "good luck" for the 8th iteration.
  - Displays "Best School" for the other iterations.

### 6. Superstitious numbers
- **File:** `6-superstitious_numbers`
- **Description:** Write a Bash script that displays numbers from 1 to 20, but:
  - Displays "4" and then "bad luck from China" for the 4th iteration.
  - Displays "9" and then "bad luck from Japan" for the 9th iteration.
  - Displays "17" and then "bad luck from Italy" for the 17th iteration.

### 7. Clock
- **File:** `7-clock`
- **Description:** Write a Bash script that displays the time for 12 hours and 59 minutes:
  - Display hours from 0 to 12.
  - Display minutes from 0 to 59.

### 8. For ls
- **File:** `8-for_ls`
- **Description:** Write a Bash script that displays:
  - The content of the current directory.
  - In a list format where only the name of the file is displayed.

### 9. To file, or not to file
- **File:** `9-to_file_or_not_to_file`
- **Description:** Write a Bash script that gives information about a file.

### 10. FizzBuzz
- **File:** `10-fizzbuzz`
- **Description:** Write a Bash script that displays numbers from 1 to 100 with FizzBuzz rules:
  - Display "Fizz" for multiples of 3.
  - Display "Buzz" for multiples of 5.
  - Display "FizzBuzz" for multiples of both 3 and 5.

### 11. Read and cut
- **File:** `11-read_and_cut`
- **Description:** Write a Bash script that reads each line of a file and cuts specific fields from it.

### 12. Tell the story of passwd
- **File:** `12-tell_the_story_of_passwd`
- **Description:** Write a Bash script that tells the story of each user in the `/etc/passwd` file by extracting and displaying relevant information.

### 13. Parse Apache logs
- **File:** `13-parse_apache_logs`
- **Description:** Write a Bash script that parses Apache log files and displays visitor IP addresses along with the corresponding HTTP status codes.

### 14. Dig the data
- **File:** `14-dig_the_data`
- **Description:** Write a Bash script that groups visitors by IP address and HTTP status code, sorts the data by the number of occurrences, and displays it in the required format.

## Additional Note

- Avoid disrupting system functionality by reverting any changes made to configuration settings after testing.

## How to Use

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd 0x04-loops_conditions_parsing
   ```
3. Make the scripts executable:
   ```bash
   chmod +x <script_name>
   ```
4. Run the scripts:
   ```bash
   ./<script_name>
   ```

Happy scripting!

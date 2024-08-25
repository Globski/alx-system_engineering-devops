# System Engineering Devops - API advanced

## Description
This project focuses on creating Python scripts to interact with the Reddit API. The project includes several tasks that require querying Reddit's endpoints, handling pagination, and processing JSON data. The ultimate goal is to practice and demonstrate your ability to work with APIs using Python. This project helps in understanding API interactions, recursive functions, and data parsing.


## Project Structure
| Task | Description | Source Code |
|------|-------------|-------------|
| 0. How Many Subs? | Write a function that queries the Reddit API and returns the number of subscribers for a given subreddit. If the subreddit is invalid, return 0. | [0-subs.py](./0-subs.py) |
| 1. Top Ten | Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit. | [1-top_ten.py](./1-top_ten.py) |
| 2. Recurse It! | Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found, return None. | [2-recurse.py](./2-recurse.py) |
| 3. Count It! | Write a recursive function that queries the Reddit API, parses the titles of all hot articles, and prints a sorted count of given keywords. Results should be sorted by frequency and then alphabetically. | [100-count.py](./100-count.py) |

## Learning Objectives

By the end of this project, you should be able to:
- Read API documentation to find the endpoints you need.
- Use an API with pagination.
- Parse JSON results from an API.
- Make recursive API calls.
- Sort dictionaries by value.

## Environment

- **Operating System:** Ubuntu 20.04 LTS
- **Python Version:** 3.4.3

## Requirements

- **Libraries:** Requests (install via `pip install requests`)
- **Libraries:** Use the Requests module for API requests.
- All Python files should end with a newline.
- The first line of all Python files should be `#!/usr/bin/python3`.
- Libraries in Python files must be organized alphabetically.
- Code should follow PEP 8 style guidelines.
- Ensure all files are executable and have proper documentation.

## How to Use

1. Clone the repository:
    ```bash
    git clone https://github.com/alx-system_engineering-devops/0x16-api_advanced.git
    cd 0x16-api_advanced
    ```

2. For each task, execute the corresponding `main.py` file with the appropriate arguments:
    ```bash
    python3 0-main.py <subreddit_name>
    python3 1-main.py <subreddit_name>
    python3 2-main.py <subreddit_name>
    python3 100-main.py <subreddit_name> '<list_of_keywords>'
    ```

3. Review the results printed to the console.


## Tasks
### 0. How Many Subs?

**Description:** Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.

**Requirements:**
- **Prototype:** `def number_of_subscribers(subreddit)`
- If not a valid subreddit, return 0.
- Hint: No authentication is necessary for most features of the Reddit API. If you’re getting errors related to Too Many Requests, ensure you’re setting a custom User-Agent.
- Ensure that you are not following redirects.

**Test Commands:**
```bash
$ python3 0-main.py programming
756024
$ python3 0-main.py this_is_a_fake_subreddit
0
```

**File:** `0-subs.py`

---

### 1. Top Ten

**Description:** Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

**Requirements:**
- **Prototype:** `def top_ten(subreddit)`
- If not a valid subreddit, print None.
- Ensure that you are not following redirects.

**Test Commands:**
```bash
$ python3 1-main.py programming
Firebase founder's response to last week's "Firebase Costs increased by 7000%!"
How a 64k intro is made
HTTPS on Stack Overflow: The End of a Long Road
...
$ python3 1-main.py this_is_a_fake_subreddit
None
```

**File:** `1-top_ten.py`

---

### 2. Recurse It!

**Description:** Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.

**Requirements:**
- **Prototype:** `def recurse(subreddit, hot_list=[])`
- Note: You may change the prototype, but it must be able to be called with just a subreddit supplied.
- If not a valid subreddit, return None.
- Must use recursion and handle pagination.

**Test Commands:**
```bash
$ python3 2-main.py programming
932
$ python3 2-main.py this_is_a_fake_subreddit
None
```

**File:** `2-recurse.py`

---

### 3. Count It!

**Description:** Write a recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces). Keywords should be printed in descending order of their frequency. If the count is the same for separate keywords, they should then be sorted alphabetically.

**Requirements:**
- **Prototype:** `def count_words(subreddit, word_list)`
- The function must work without supplying a starting value in the main.
- Results should be printed in descending order, by the count, and if the count is the same for separate keywords, they should be sorted alphabetically (ascending, from A to Z).
- Words with no matches should be skipped and not printed.
- Words must be printed in lowercase.
- Results are based on the number of times a keyword appears, not titles it appears in.
- Ensure that you are not following redirects.

**Test Commands:**
```bash
$ python3 100-main.py programming 'react python java javascript scala no_results_for_this_one'
java: 27
javascript: 20
python: 17
...
$ python3 100-main.py not_a_valid_subreddit 'python java'
```
**File:** `100-count.py`

## Additional Note

- Ensure that you are not following redirects when handling invalid subreddits.
- Use a custom User-Agent if you encounter errors related to "Too Many Requests."


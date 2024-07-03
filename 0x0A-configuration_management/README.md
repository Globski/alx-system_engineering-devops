# System-Engineering Devops - Configuration Management

## Description

This project demonstrates basic configuration management using Puppet. It includes tasks to create a file, install a package, and execute a command.

## Project Structure
| Task                          | Description                                                                   | Source Code                 |
|-------------------------------|-------------------------------------------------------------------------------|-----------------------------|
| Task 0: Create a File         | Creates a file at `/tmp/school` with permissions `0744`, owner `www-data`, group `www-data`, and content `I love Puppet`. | [0-create_a_file.pp](0-create_a_file.pp)        |
| Task 1: Install a Package     | Installs Flask version 2.1.0 using `pip3`.                                     | [1-install_a_package.pp](1-install_a_package.pp)    |
| Task 2: Execute a Command     | Kills a process named `killmenow` using the `pkill` command.                  | [2-execute_a_command.pp](2-execute_a_command.pp)   |

## Learning Objectives
By the end of this project, you should be able to explain:

- Basics of configuration management.
- Write Puppet manifests to manage files, packages, and processes.

## Environment
- **OS:** Ubuntu 20.04 LTS
- **Puppet Version:** 5.5
- **Puppet Lint Version:** 2.1.1 or higher (2.5.2)


### Requirements
   - Files must end with a new line.
   - Puppet manifests should pass puppet-lint version 2.1.1 without errors.
   - Manifests must run without any errors.

## Features

- **Manifest Creation:**
  - Create Puppet manifests (.pp files) that configure various aspects of your infrastructure on Ubuntu 20.04 LTS.

- **Testing and Validation:**
  - Run puppet-lint to ensure manifests meet linting requirements.
  - Execute Puppet manifests to verify they configure the system without errors.

## How to Use

- **Installation:**
``` 
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
  $ apt-get install -y ruby-augeas
  $ apt-get install -y ruby-shadow
  $ apt-get install -y puppet
  $ gem install puppet-lint
```

**Ensure that you have the necessary environment set up, including Puppet and Puppet Lint, before running these commands.**

**Lint the manifest:**

```bash
   puppet-lint <manifest_file>
```

**Apply the manifest:**

```bash
   puppet apply <manifest_file>

```

**Verify the installation:**

```   bash
   flask --version
```

**Verify the process termination:**
Ensure the process killmenow is terminated.

```   bash
   ./killmenow
   ps aux | grep killmenow
```

## Tasks

### Task 0: Create a File

- **Manifest File:** 0-create_a_file.pp
- **Description:** Creates a file at /tmp/school with permissions 0744, owner www-data, group www-data, and content I love Puppet.

**Example:**
```
root@6712bef7a528:~# puppet-lint --version
puppet-lint 2.5.2
root@6712bef7a528:~# puppet-lint 0-create_a_file.pp
root@6712bef7a528:~# 
root@6712bef7a528:~# puppet apply 0-create_a_file.pp
Notice: Compiled catalog for 6712bef7a528.ec2.internal in environment production in 0.04 seconds
Notice: /Stage[main]/Main/File[school]/ensure: defined content as '{md5}f1b70c2a42a98d82224986a612400db9'
Notice: Finished catalog run in 0.03 seconds
root@6712bef7a528:~#
root@6712bef7a528:~# ls -l /tmp/school
-rwxr--r-- 1 www-data www-data 13 Mar 19 23:12 /tmp/school
root@6712bef7a528:~# cat /tmp/school
I love Puppetroot@6712bef7a528:~#
```

### Task 1: Install a Package

- **Manifest File:** 1-install_a_package.pp
- **Description:** Installs Flask version 2.1.0 using pip3.

**Example:**
```
root@9665f0a47391:/# puppet apply 1-install_a_package.pp
Notice: Compiled catalog for 9665f0a47391 in environment production in 0.14 seconds
Notice: /Stage[main]/Main/Package[Flask]/ensure: created
Notice: Applied catalog in 0.20 seconds
root@9665f0a47391:/# flask --version
Python 3.8.10
Flask 2.1.0
Werkzeug 2.1.1
```

### Task 2: Execute a Command

- **Manifest File:** 2-execute_a_command.pp
- **Description:** Kills a process named killmenow using the pkill command.

**Example:**
**Terminal #0 - starting my process**
```
root@d391259bf577:/# cat killmenow
#!/bin/bash
while [[ true ]]
do
    sleep 2
done

root@d391259bf577:/# ./killmenow
```

**Terminal #1 - executing my manifest**
```
root@d391259bf577:/# puppet apply 2-execute_a_command.pp
Notice: Compiled catalog for d391259bf577.hsd1.ca.comcast.net in environment production in 0.01 seconds
Notice: /Stage[main]/Main/Exec[killmenow]/returns: executed successfully
Notice: Finished catalog run in 0.10 seconds
root@d391259bf577:/# 
```
**Terminal #0 - process has been terminated**
```
root@d391259bf577:/# ./killmenow
Terminated
root@d391259bf577:/#
```

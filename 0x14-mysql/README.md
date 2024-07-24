# High-Level Programming - MySQL

## Description

The project involves working with MySQL databases. It focuses on setting up and configuring MySQL replication between a primary and a replica server, as well as creating and managing MySQL backups. This project will test your skills in database administration and web stack debugging.

## Project Structure

| Task | Description | Source Code |
|------|-------------|-------------|
| **0. Install MySQL** | Install MySQL distribution 5.7.x on both web-01 and web-02 servers. Ensure MySQL status can be checked. | [Source Code](https://github.com/username/alx-system_engineering-devops/tree/main/0x14-mysql) |
| **1. Let us in!** | Create a MySQL user holberton_user on both servers with the password projectcorrection280hbtn and grant necessary permissions. | [Source Code](https://github.com/username/alx-system_engineering-devops/tree/main/0x14-mysql) |
| **2. If only you could see what I've seen with your eyes** | Create a database named tyrell_corp and a table named nexus6 with at least one entry. Ensure holberton_user has SELECT privileges. | [Source Code](https://github.com/username/alx-system_engineering-devops/tree/main/0x14-mysql) |
| **3. Quite an experience to live in fear, isn't it?** | Create a MySQL user replica_user for replication with appropriate permissions. Ensure holberton_user can check the user’s permissions. | [Source Code](https://github.com/username/alx-system_engineering-devops/tree/main/0x14-mysql) |
| **4. Setup a Primary-Replica infrastructure using MySQL** | Set up replication between the primary MySQL server (web-01) and the replica server (web-02). Provide configurations and ensure replication works. | [Source Code](https://github.com/username/alx-system_engineering-devops/tree/main/0x14-mysql) |
| **5. Backup your database** | Write a Bash script to create a backup of your MySQL database, save it in /tmp/, and format the filename as day-month-year.tar.gz. Handle authentication and compression. | [Source Code](https://github.com/username/alx-system_engineering-devops/tree/main/0x14-mysql) |

## Features

- Install and configure MySQL servers.
- Set up MySQL replication between primary and replica servers.
- Create and manage MySQL users with appropriate permissions.
- Implement and verify MySQL backups.

## Learning Objectives
By the end of this project, you should be able to explain:

- What is the main role of a database
- What is a database replica
- What is the purpose of a database replica
- Why database backups need to be stored in different physical locations
- What operation should you regularly perform to make sure that your database backup strategy actually works
- What is a primary-replica cluster?
- MySQL primary replica setup
- Build a robust database backup strategy
- mysqldump

## Environment

- Ubuntu 16.04 LTS
- **Web-01**: MySQL primary server.
- **Web-02**: MySQL replica server.
- **MySQL 5.7.x**


## Requirements

- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any error
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- All your files should end with a new line

## How to Use

### Setup Instructions

#### 1. Installing MySQL 5.7

**Installation**: Follow the instructions for installing MySQL on your servers. Ensure both servers have MySQL 5.7.x installed and running.

1. **Update package information:**
   
bash
   sudo apt-get update


2. **Install MySQL server:**
   
bash
   sudo apt-get install mysql-server-5.7


3. **Verify installation:**
   
bash
   mysql --version


#### 2. Setting Up Users

**Configuration**: Configure MySQL on both servers as described in the tasks. Create users, set permissions, and configure replication as outlined.

1. **Create holberton_user on both servers:**
   
sql
   CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
   GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
   FLUSH PRIVILEGES;


2. **Create replica_user on the primary server:**
   
sql
   CREATE USER 'replica_user'@'%' IDENTIFIED BY 'your_password';
   GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
   FLUSH PRIVILEGES;


#### 3. Configuring MySQL Replication

**Verification**: Verify MySQL replication and permissions using provided commands and examples. Check that replication is working by adding records and ensuring they appear on both servers.

1. **Primary Server Configuration (web-01):**
   - Edit MySQL configuration file (/etc/mysql/mysql.conf.d/mysqld.cnf):
     
ini
     [mysqld]
     log_bin = /var/log/mysql/mysql-bin.log
     server_id = 1
     binlog_do_db = tyrell_corp

   - Restart MySQL:
     
bash
     sudo service mysql restart


2. **Replica Server Configuration (web-02):**
   - Edit MySQL configuration file (/etc/mysql/mysql.conf.d/mysqld.cnf):
     
ini
     [mysqld]
     server_id = 2
     relay_log = /var/log/mysql/mysql-relay-bin.log
     log_bin = /var/log/mysql/mysql-bin.log

   - Restart MySQL:
     
bash
     sudo service mysql restart


3. **Setting Up Replication:**
   - On primary server (web-01), get the binary log file name and position:
     
sql
     SHOW MASTER STATUS;

   - On replica server (web-02), start replication:
     
sql
     CHANGE MASTER TO MASTER_HOST='web-01-ip', MASTER_USER='replica_user', MASTER_PASSWORD='your_password', MASTER_LOG_FILE='mysql-bin.000001', MASTER_LOG_POS=log_position;
     START SLAVE;


#### 4. Running the Backup Script

**Backup**: Use the provided Bash script to create backups of your database. Ensure the backup is correctly formatted and stored.

1. **Create a Bash script (5-mysql_backup.sh):**
   
bash
   #!/usr/bin/env bash
   # This script generates a MySQL dump and creates a compressed archive.

   PASSWORD=$1
   FILE_NAME=$(date +'%d-%m-%Y').tar.gz

   mysqldump -u root -p${PASSWORD} --all-databases > backup.sql
   tar -czvf ${FILE_NAME} backup.sql
   rm backup.sql


2. **Make the script executable:**
   
bash
   chmod +x 5-mysql_backup.sh


3. **Run the script:**
   
bash
   ./5-mysql_backup.sh your_mysql_root_password


## **Additional Tips**

- **Check MySQL Documentation:** Refer to the MySQL documentation for detailed commands and configuration options.
- **Backup Testing:** Regularly test your backup and restore procedures to ensure they work as expected.
- **Firewall Configuration:** Ensure UFW allows traffic on port 3306 for MySQL replication to function properly.

## Tasks

0. **Install MySQL (Task 0)**
   - **Objective:** Install MySQL version 5.7.x on both web-01 and web-02 servers.
   - **Verification:** Ensure MySQL is installed by running mysql --version on both servers.
   - **Repo Info:** GitHub repository: alx-system_engineering-devops, Directory: 0x14-mysql.
gh-Level Programming - MySQL

## Description

The project involves working with MySQL databases. It focuses on setting up and configuring MySQL replication between a primary and a replica server, as well as creating and managing MySQL backups. This project will test your skills in database administration and web stack debugging.

## Project Structure

| Task | Description | Source Code |
|------|-------------|-------------|
| **0. Install MySQL** | Install MySQL distribution 5.7.x on both web-01 and web-02 servers. Ensure MySQL status can be checked. | [Source Code](https://github.com/username/alx-system_engineering-devops/tree/main/0x14-mysql) |
| **1. Let us in!** | Create a MySQL user holberton_user on both servers with the password projectcorrection280hbtn and grant necessary permissions. | [Source Code](https://github.com/username/alx-system_engineering-devops/tree/main/0x14-mysql) |
| **2. If only you could see what I've seen with your eyes** | Create a database named tyrell_corp and a table named nexus6 with at least one entry. Ensure holberton_user has SELECT privileges. | [Source Code](https://github.com/username/alx-system_engineering-devops/tree/main/0x14-mysql) |
| **3. Quite an experience to live in fear, isn't it?** | Create a MySQL user replica_user for replication with appropriate permissions. Ensure holberton_user can check the user’s permissions. | [Source Code](https://github.com/username/alx-system_engineering-devops/tree/main/0x14-mysql) |
| **4. Setup a Primary-Replica infrastructure using MySQL** | Set up replication between the primary MySQL server (web-01) and the replica server (web-02). Provide configurations and ensure replication works. | [Source Code](https://github.com/username/alx-system_engineering-devops/tree/main/0x14-mysql) |
| **5. Backup your database** | Write a Bash script to create a backup of your MySQL database, save it in /tmp/, and format the filename as day-month-year.tar.gz. Handle authentication and compression. | [Source Code](https://github.com/username/alx-system_engineering-devops/tree/main/0x14-mysql) |

## Features

- Install and configure MySQL servers.
- Set up MySQL replication between primary and replica servers.
- Create and manage MySQL users with appropriate permissions.
- Implement and verify MySQL backups.

## Learning Objectives
By the end of this project, you should be able to explain:

- What is the main role of a database
- What is a database replica
- What is the purpose of a database replica
- Why database backups need to be stored in different physical locations
- What operation should you regularly perform to make sure that your database backup strategy actually works
- What is a primary-replica cluster?
- MySQL primary replica setup
- Build a robust database backup strategy
- mysqldump

## Environment

- Ubuntu 16.04 LTS
- **Web-01**: MySQL primary server.
- **Web-02**: MySQL replica server.
- **MySQL 5.7.x**


## Requirements

- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any error
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- All your files should end with a new line

## How to Use

### Setup Instructions

#### 1. Installing MySQL 5.7

**Installation**: Follow the instructions for installing MySQL on your servers. Ensure both servers have MySQL 5.7.x installed and running.

1. **Update package information:**
   
```bash
   sudo apt-get update
```

2. **Install MySQL server:**
   
```bash
   sudo apt-get install mysql-server-5.7
```

3. **Verify installation:**
   
```bash
   mysql --version
```

#### 2. Setting Up Users

**Configuration**: Configure MySQL on both servers as described in the tasks. Create users, set permissions, and configure replication as outlined.

1. **Create holberton_user on both servers:**
   
```sql
   CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
   GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
   FLUSH PRIVILEGES;
```

2. **Create replica_user on the primary server:**
   
```sql
   CREATE USER 'replica_user'@'%' IDENTIFIED BY 'your_password';
   GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
   FLUSH PRIVILEGES;
```

#### 3. Configuring MySQL Replication

**Verification**: Verify MySQL replication and permissions using provided commands and examples. Check that replication is working by adding records and ensuring they appear on both servers.

1. **Primary Server Configuration (web-01):**
   - Edit MySQL configuration file (/etc/mysql/mysql.conf.d/mysqld.cnf):
     
```ini
     [mysqld]
     log_bin = /var/log/mysql/mysql-bin.log
     server_id = 1
     binlog_do_db = tyrell_corp
```
   - Restart MySQL:
   
```bash
     sudo service mysql restart
```

2. **Replica Server Configuration (web-02):**
   - Edit MySQL configuration file (/etc/mysql/mysql.conf.d/mysqld.cnf):
     
```ini
     [mysqld]
     server_id = 2
     relay_log = /var/log/mysql/mysql-relay-bin.log
     log_bin = /var/log/mysql/mysql-bin.log
```
   - Restart MySQL:
     
```bash
     sudo service mysql restart
```

3. **Setting Up Replication:**
   - On primary server (web-01), get the binary log file name and position:
     
```sql
     SHOW MASTER STATUS;
```
   - On replica server (web-02), start replication:
     
```sql
     CHANGE MASTER TO MASTER_HOST='web-01-ip', MASTER_USER='replica_user', MASTER_PASSWORD='your_password', MASTER_LOG_FILE='mysql-bin.000001', MASTER_LOG_POS=log_position;
     START SLAVE;
```

#### 4. Running the Backup Script

**Backup**: Use the provided Bash script to create backups of your database. Ensure the backup is correctly formatted and stored.

1. **Create a Bash script (5-mysql_backup.sh):**
   
```bash
   #!/usr/bin/env bash
   # This script generates a MySQL dump and creates a compressed archive.

   PASSWORD=$1
   FILE_NAME=$(date +'%d-%m-%Y').tar.gz

   mysqldump -u root -p${PASSWORD} --all-databases > backup.sql
   tar -czvf ${FILE_NAME} backup.sql
   rm backup.sql
```

2. **Make the script executable:**
   
```bash
   chmod +x 5-mysql_backup.sh
```

3. **Run the script:**
   
```bash
   ./5-mysql_backup.sh your_mysql_root_password
```

## **Additional Tips**

- **Check MySQL Documentation:** Refer to the MySQL documentation for detailed commands and configuration options.
- **Backup Testing:** Regularly test your backup and restore procedures to ensure they work as expected.
- **Firewall Configuration:** Ensure UFW allows traffic on port 3306 for MySQL replication to function properly.

## Tasks

0. **Install MySQL (Task 0)**
   - **Objective:** Install MySQL version 5.7.x on both web-01 and web-02 servers.
   - **Verification:** Ensure MySQL is installed by running mysql --version on both servers.
   - **Repo Info:** GitHub repository: alx-system_engineering-devops, Directory: 0x14-mysql.

Example:
```bash
ubuntu@229-web-01:~$ mysql --version
mysql  Ver 14.14 Distrib 5.7.25, for Linux (x86_64) using  EditLine wrapper
ubuntu@229-web-01:~$
```

1. **Create MySQL User (Task 1)**
   - **Objective:** Create a MySQL user holberton_user on both servers with password projectcorrection280hbtn.
   - **Permissions:** Grant the user permission to check replication status.
   - **Verification:** Run mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'".
   - **Repo Info:** GitHub repository: alx-system_engineering-devops, Directory: 0x14-mysql.

Example:
```bash
ubuntu@229-web-01:~$ mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'"
Enter password:
+-----------------------------------------------------------------+
| Grants for holberton_user@localhost                             |
+-----------------------------------------------------------------+
| GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost' |
+-----------------------------------------------------------------+
ubuntu@229-web-01:~$
```

2. **Setup Database and Table (Task 2)**
   - **Objective:** Create a database tyrell_corp and a table nexus6 with at least one row on the primary server (web-01).
   - **Permissions:** Ensure holberton_user has SELECT permissions on the nexus6 table so that we can check that the table exists and is not empty..
   - **Verification:** Run mysql -uholberton_user -p -e "use tyrell_corp; select * from nexus6".
   - **Repo Info:** GitHub repository: alx-system_engineering-devops, Directory: 0x14-mysql.

Example:
```bash
ubuntu@229-web-01:~$ mysql -uholberton_user -p -e "use tyrell_corp; select * from nexus6"
Enter password:
+----+-------+
| id | name  |
+----+-------+
|  1 | Leon  |
+----+-------+
ubuntu@229-web-01:~$
```

3. **Quite an experience to live in fear, isn't it? (Task 3)**
   - **Objective:** Before you get started with your primary-replica synchronization, you need one more thing in place. On your primary MySQL server (web-01), create a new user for the replica server.

- The name of the new user should be replica_user, with the host name set to %, and can have whatever password you’d like.
- replica_user must have the appropriate permissions to replicate your primary MySQL server.
- holberton_user will need SELECT privileges on the mysql.user table in order to check that replica_user was created with the correct permissions.
- **Repo Info:** GitHub repository: alx-system_engineering-devops, Directory: 0x14-mysql.

Example:
```bash
ubuntu@229-web-01:~$ mysql -uholberton_user -p -e 'SELECT user, Repl_slave_priv FROM mysql.user'
+------------------+-----------------+
| user             | Repl_slave_priv |
+------------------+-----------------+
| root             | Y               |
| mysql.session    | N               |
| mysql.sys        | N               |
| debian-sys-maint | Y               |
| holberton_user   | N               |
| replica_user     | Y               |
+------------------+-----------------+
ubuntu@229-web-01:~$
```

### 4. Setup a Primary-Replica infrastructure using MySQL
**Mandatory**

Having a replica member on for your MySQL database has 2 advantages:

- Redundancy: If you lose one of the database servers, you will still have another working one and a copy of your data
- Load distribution: You can split the read operations between the 2 servers, reducing the load on the primary member and improving query response speed

Requirements:
- MySQL primary must be hosted on web-01 - do not use the bind-address, just comment out this parameter
- MySQL replica must be hosted on web-02
- Setup replication for the MySQL database named tyrell_corp
- Provide your MySQL primary configuration as an answer file (my.cnf or mysqld.cnf) with the name 4-mysql_configuration_primary
- Provide your MySQL replica configuration as an answer file with the name 4-mysql_configuration_replica

Tips:
- Once MySQL replication is setup, add a new record in your table via MySQL on web-01 and check if the record has been replicated in MySQL web-02. If you see it, it means your replication is working!
- Make sure that UFW is allowing connections on port 3306 (default MySQL port) otherwise replication will not work.
  - **Files Required:**
     - Primary configuration file: 4-mysql_configuration_primary
     - Replica configuration file: 4-mysql_configuration_replica
   - **Verification:** Add a new record in the primary table and check replication on the replica server.

Example:
**web-01**
```bash
ubuntu@web-01:~$ mysql -uholberton_user -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 1467
Server version: 5.5.49-0ubuntu0.14.04.1-log (Ubuntu)

Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show master status;
+------------------+----------+--------------------+------------------+
| File             | Position | Binlog_Do_DB       | Binlog_Ignore_DB |
+------------------+----------+--------------------+------------------+
| mysql-bin.000009 |      107 | tyrell_corp        |                  |
+------------------+----------+--------------------+------------------+
1 row in set (0.00 sec)

mysql>
```
**web-02**
```bash
root@web-02:/home/ubuntu# mysql -uholberton_user -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 53
Server version: 5.5.49-0ubuntu0.14.04.1-log (Ubuntu)

Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show slave status\G
*************************** 1. row ***************************
               Slave_IO_State: Waiting for master to send event
                  Master_Host: 158.69.68.78
                  Master_User: replica_user
                  Master_Port: 3306
                Connect_Retry: 60
              Master_Log_File: mysql-bin.000009
          Read_Master_Log_Pos: 107
               Relay_Log_File: mysql-relay-bin.000022
                Relay_Log_Pos: 253
        Relay_Master_Log_File: mysql-bin.000009
             Slave_IO_Running: Yes
            Slave_SQL_Running: Yes
              Replicate_Do_DB: 
          Replicate_Ignore_DB: 
           Replicate_Do_Table: 
       Replicate_Ignore_Table: 
      Replicate_Wild_Do_Table: 
  Replicate_Wild_Ignore_Table: 
                   Last_Errno: 0
                   Last_Error: 
                 Skip_Counter: 0
          Exec_Master_Log_Pos: 107
              Relay_Log_Space: 452
              Until_Condition: None
               Until_Log_File: 
                Until_Log_Pos: 0
           Master_SSL_Allowed: No
           Master_SSL_CA_File: 
           Master_SSL_CA_Path: 
              Master_SSL_Cert: 
            Master_SSL_Cipher: 
               Master_SSL_Key: 
        Seconds_Behind_Master: 0
Master_SSL_Verify_Server_Cert: No


            Last_IO_Errno: 0
            Last_IO_Error: 
           Last_SQL_Errno: 0
           Last_SQL_Error:
```
- **Repo:**  
  GitHub repository: alx-system_engineering-devops  
  Directory: 0x14-mysql

### 5. Backup your database
**Mandatory**

Having backups of your MySQL database is very important as it allows you to restore your data in case of corruption or data loss. 

- Write a Bash script that will create a backup of your MySQL database and store it in /tmp/
- The name of the backup file should be formatted as day-month-year.tar.gz (e.g. 28-07-2024.tar.gz).
- The script should also handle authentication and compression. It must take the MySQL root password as an argument.

Example:
```bash
#!/bin/bash
#### Backup script for MySQL databases

BACKUP_DIR="/tmp"
DATE=$(date +"%d-%m-%Y")
FILENAME="backup_$DATE.tar.gz"
MYSQL_USER="root"
MYSQL_PASSWORD="$1"

if [ -z "$MYSQL_PASSWORD" ]; then
  echo "Usage: $0 <mysql_root_password>"
  exit 1
fi
```
#### Create the backup
mysqldump -u $MYSQL_USER -p$MYSQL_PASSWORD --all-databases | gzip > $BACKUP_DIR/$FILENAME

##### Check if backup was successful
if [ $? -eq 0 ]; then
  echo "Backup successful: $BACKUP_DIR/$FILENAME"
else
  echo "Backup failed"
  exit 1
fi

- **Repo:**  
  GitHub repository: alx-system_engineering-devops  
  Directory: 0x14-mysql  
  File: 5-mysql_backup

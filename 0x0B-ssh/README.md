# System-Engineering Devops - SSH

## Description
This project aims to deepen your understanding of SSH (Secure Shell) and its usage in a DevOps environment. You will learn how to create and use SSH RSA key pairs to connect to remote servers securely, including using Puppet for automated configuration management. This is a critical skill for managing servers and ensuring secure communication over networks.

## Project Structure

| Task | Description | Source Code |
|-----------------------------------|------------------------------------------------------|-----------------------------------------------|
| Task 0: Use a Private Key | Write a Bash script that uses SSH to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`. | [0-use_a_private_key](0-use_a_private_key) |
| Task 1: Create an SSH Key Pair | Write a Bash script that creates an RSA key pair named `school` with 4096 bits, protected by the passphrase `betty`. | [1-create_ssh_key_pair](1-create_ssh_key_pair) |
| Task 2: Client Configuration File | Configure your SSH client to use the private key `~/.ssh/school` and refuse password authentication. | [2-ssh_config](2-ssh_config) |
| Task 4: Client Configuration File (w/ Puppet) | Use Puppet to configure your SSH client to use the private key `~/.ssh/school` and refuse password authentication. | [100-puppet_ssh_config.pp](100-puppet_ssh_config.pp) |

## Learning Objectives
By the end of this project, you should be able to explain:
- What a server is and where servers usually live.
- What SSH is and why it is used.
- How to create an SSH RSA key pair.
- How to connect to a remote host using an SSH RSA key pair.
- The advantage of using `#!/usr/bin/env bash` instead of `/bin/bash` in script files.

## Requirements
- **Operating System:** Ubuntu 20.04 LTS
- **File Endings:** All files must end with a new line.
- **Scripts:** All Bash scripts must be executable and start with `#!/usr/bin/env bash`.

### How to Use
**Clone the Repository:**
```sh
git clone https://github.com/<your-username>/alx-system_engineering-devops.git
cd alx-system_engineering-devops/0x0B-ssh
```

**Task 0: Use a Private Key**
- Connect to a remote server using a private key.
```
ssh -i ~/.ssh/school ubuntu@172.17.0.34
```
- Replace `172.17.0.34` with your actual server IP address.

**Task 1: Create an SSH Key Pair**
- Generate an RSA key pair.
```
ssh-keygen -t rsa -b 4096 -f ~/.ssh/school -N betty
```

**Task 2: Client Configuration File**
- Configure your SSH client to use the private key and refuse password authentication.

**Configuration File (`~/.ssh/config`):**
```
Host *
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
```
- Make sure to add this configuration to your `~/.ssh/config` file.

**Task 3: Let Me In!**
- Add the provided SSH public key to your server to allow connections using the `ubuntu` user.

**Steps:**
**Connect to your server using SSH:**
   ```bash
   ssh ubuntu@<server-ip>
   ```
   Replace `<server-ip>` with your actual server IP address.

**Create and set up the `.ssh` directory:**
   ```bash
   mkdir -p ~/.ssh
   chmod 700 ~/.ssh
   ```

**Add the public key to `authorized_keys`:**
   ```bash
   echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNdtrNGtTXe5Tp1EJQop8mOSAuRGLjJ6DW4PqX4wId/Kawz35ESamp" >> ~/.ssh/authorized_keys
   chmod 600 ~/.ssh/authorized_keys
   ```

**Set permissions for key files:**
   ```bash
   chmod 600 ~/.ssh/school
   chmod 644 ~/.ssh/school.pub
   ```

**Task 4: Client Configuration File (w/ Puppet)**
- Use Puppet to automate the SSH client configuration.

**Puppet Manifest (`100-puppet_ssh_config.pp`):**
**Apply the Puppet manifest:**
   ```bash
   sudo puppet apply 100-puppet_ssh_config.pp
   ```
- This will configure your SSH client to use the specified private key and disable password authentication.


## Additional Notes

**File Permissions:**
   Ensure that your SSH key files and configuration files have the correct permissions to avoid security issues.
   
**Puppet Installation:**
   Ensure Puppet is installed on your system. You can install it using:
   ```bash
   sudo apt-get update
   sudo apt-get install puppet
   ```

## Tasks

### Task 0: Use a Private Key
**Description:** Write a Bash script that uses ssh to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`.

**Requirements:**
- Only use ssh single-character flags.
- You cannot use `-l`.
- You do not need to handle the case of a private key protected by a passphrase.

**Example:**
```sh
sylvain@ubuntu$ ./0-use_a_private_key
ubuntu@server01:~$ exit
Connection to 8.8.8.8 closed.
sylvain@ubuntu$ 
```

### Task 1: Create an SSH Key Pair
**Description:** Write a Bash script that creates an RSA key pair.

**Requirements:**
- Name of the created private key must be school.
- Number of bits in the created key to be created: 4096.
- The created key must be protected by the passphrase betty.

**Example:**

```sh
sylvain@ubuntu$ ls
1-create_ssh_key_pair
sylvain@ubuntu$ ./1-create_ssh_key_pair
Generating public/private rsa key pair.
Your identification has been saved in school.
Your public key has been saved in school.pub.
The key fingerprint is:
5d:a8:c1:f5:98:b6:e5:c0:9b:ee:02:c4:d4:01:f3:ba vagrant@ubuntu
The key's randomart image is:
+--[ RSA 4096]----+
|      oo...      |
|      .+.o =     |
|     o  + B +    |
|      o. = O     |
|     .. S = .    |
|      .. .       |
|      E.  .      |
|        ..       |
|         ..      |
+-----------------+
sylvain@ubuntu$ ls
1-create_ssh_key_pair school  school.pub
sylvain@ubuntu$
```

### Task 2: Client Configuration File
Description: Your machine has an SSH configuration file for the local SSH client. Let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.

**Requirements:**
- Your SSH client configuration must be configured to use the private key ~/.ssh/school.
- Your SSH client configuration must be configured to refuse to authenticate using a password.

**Example:**
```sh
sylvain@ubuntu$ ssh -v ubuntu@98.98.98.98
OpenSSH_6.6.1, OpenSSL 1.0.1f 6 Jan 2014
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 47: Applying options for *
debug1: Connecting to 98.98.98.98 port 22.
debug1: Connection established.
debug1: identity file /home/sylvain/.ssh/school type -1
debug1: identity file /home/sylvain/.ssh/school-cert type -1
debug1: Enabling compatibility mode for protocol 2.0
debug1: Local version string SSH-2.0-OpenSSH_8.1
debug1:Remote protocol version 2.0, remote software version OpenSSH_7.6p1 Ubuntu-4ubuntu0.5
debug1: match: OpenSSH_7.6p1 Ubuntu-4ubuntu2.1 pat OpenSSH* compat 0x04000000
debug1: SSH2_MSG_KEXINIT sent
debug1: SSH2_MSG_KEXINIT received
debug1: kex: server->client aes128-ctr hmac-sha1-etm@openssh.com none
debug1: kex: client->server aes128-ctr hmac-sha1-etm@openssh.com none
debug1: sending SSH2_MSG_KEX_ECDH_INIT
debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
debug1: Server host key: ECDSA bd:03:f8:6a:12:28:d6:17:85:c1:b6:91:f1:da:0f:37
debug1: Host '98.98.98.98' is known and matches the ECDSA host key.
debug1: Found key in /home/sylvain/.ssh/known_hosts:1
debug1: ssh_ecdsa_verify: signature correct
debug1: SSH2_MSG_NEWKEYS sent
debug1: expecting SSH2_MSG_NEWKEYS
debug1: SSH2_MSG_NEWKEYS received
debug1: SSH2_MSG_SERVICE_REQUEST sent
debug1: SSH2_MSG_SERVICE_ACCEPT received
debug1: Authentications that can continue: publickey,password
debug1: Next authentication method: publickey
debug1: Trying private key: /home/sylvain/.ssh/school
debug1: key_parse_private2: missing begin marker
debug1: read PEM private key done: type RSA
debug1: Authentication succeeded (publickey).
Authenticated to 98.98.98.98 ([98.98.98.98]:22).
debug1: channel 0: new [client-session]
debug1: Requesting no-more-sessions@openssh.com
debug1: Entering interactive session.
debug1: client_input_global_request: rtype hostkeys-00@openssh.com want_reply 0
debug1: Sending environment.
debug1: Sending env LANG = en_US.UTF-8
ubuntu@magic-server:~$
```

### Task 3: Let Me In!
Description: Add the SSH public key below to your server so that we can connect using the ubuntu user.

**Public Key:**

```sh
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNdtrNGtTXe5Tp1EJQop8mOSAuRGLjJ6DW4PqX4wId/Kawz35ESamp
```

### Task 4: Client Configuration File (w/ Puppet)

**Description:** Let’s practice using Puppet to make changes to our configuration file. Just as in the previous configuration file task, we’d like you to set up your client SSH configuration file so that you can connect to a server without typing a password.

**Requirements:**
- Your SSH client configuration must be configured to use the private key ~/.ssh/school.
- Your SSH client configuration must be configured to refuse to authenticate using a password.

**Example:**
```sh
vagrant@ubuntu:~$ sudo puppet apply 100-puppet_ssh_config.pp
Notice: Compiled catalog for ubuntu-xenial in environment production in 0.11 seconds
Notice: /Stage[main]/Main/File_line[Turn off passwd auth]/ensure: created
Notice: /Stage[main]/Main/File_line[Declare identity file]/ensure: created
Notice: Finished catalog run in 0.03 seconds
vagrant@ubuntu:~$
```


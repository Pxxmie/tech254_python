
### Secure Shell Protocol (SSH)

`What is SSH?` 

SSH is known as Secure Shell and is a network protocol used to securely connect to remove servers over a network. 

It is a method for secure remote login from one computer to another. 

It provides strong password authentication and strong encryption. 

`What is it used for?` 

- Used to connect to servers, make changes, perform uploads and exit either using tools or directly through the terminal.
- manage routers, server hardware, virtualization platforms, operating systems and inside system management and file transfer application.
- Manage website hosted on a server
- Perform administrative tasks on a remote computer
- Securely transfer files between computers
- Network management
- File Transfers - a secure file transfer protocol managed by SSH, provides a safe way to manipulate files over a network.

`How does SSH work?` 

1) **Connection Request:**

Client contacts server to initiate a connection

2) **Server Identification:**

The remote server receives your connection request. It sends back its public key to identify itself. 

3) **Key Exchange:** 

Your SSH client uses the server’s public key to e

`Public and Private Key` 

- Anyone with a copy of the public key can encrypt data which can then only be read by the person who holds the corresponding private key. Once an SSH server receives a public key from a user and considers the key trustworthy, the server marks the key as authorized in its authorised **key file**. Such keys are called authorised keys.
- A private key that remains (only) with the user. The possession of this key is proof of the user's identity. Only a user in possession of a private key that corresponds to the public key at the server will be able to authenticate successfully. The private keys need to be stored and handled carefully, and no copies of the private key should be distributed. The private keys used for user authentication are called identity keys. 

`Why use SSH? How does it increase security?` 

SSH is used for several reasons, and one of its primary advantages is the enhanced security it provides for remote access and communication.

- Encryption
- Authentication
- Protection against brute force attacks
- Key Based Authentication
- Secure File transfers (SFTP)
- Port Forwarding
- Host Verification
- Multi-Factor Authentication
- Wide Adoption and Support.

`How can you create a SSH key pair?` 

You can generate a new SSH key on your local machine. After you generate the key, you can add the public key to your account on GitHub to enable authentication for Git operations over SSH.

1. Open Git Bash.
2. Paste the text below, substituting in your GitHub email address.
    
    ```
    ssh-keygen -t ed25519 -C "your_email@example.com"
    ```
    
    This creates a new SSH key, using the provided email as a label.
    
    ```
    > Generating public/private ALGORITHM key pair.
    ```
    
    When you're prompted to "Enter a file in which to save the key", you can press **Enter** to accept the default file location. `Please note that if you created SSH keys previously, ssh-keygen may ask you to rewrite another key, in which case we recommend creating a custom-named SSH key`. To do so, type the default file location and replace id_ssh_keyname with your custom key name.
    
    `> Enter a file in which to save the key (/c/Users/YOU/.ssh/id_ALGORITHM):[Press enter]`
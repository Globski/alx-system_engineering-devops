# Simple web stack

## What is a Server?
A server is a robust computer or software program that caters to other computers, known as clients, by providing services or resources over a network such as hosting websites, managing files, handling email, and ensuring secure network communication. The arrangement is termed the client-server model. Servers come in various types such as web servers (e.g., Apache HTTP Server), application servers (e.g., Apache Tomcat), database servers (e.g., MySQL), etc., each fulfilling specific functions like hosting websites, handling application logic, or managing data.

Additionally, there are physical servers, dedicated hardware machines with components like CPU and storage, and virtual servers, software-based emulations running on physical servers through virtualization technology. The key difference lies in physical servers using dedicated hardware resources while virtual servers share resources with other virtual servers. Servers like VPN servers ensure secure remote network access, while game servers host multiplayer games, and print servers manage print jobs on a network.

## What is the role of the domain name
By giving users a memorable and simple-to-remember address, a domain name enables users to browse websites without having to memorize numerical IP addresses. For instance, the Domain Name System (DNS) maps the human-readable address www.foobar.com  into machine-readable IP addresses (like 80.142.74.130) making it simpler for consumers to remember and visit the website. 
This translation is essential because, while humans navigate the web using domain names, computers and other network devices use IP addresses to identify each other and communicate on the internet.

## What type of DNS record www is in www.foobar.com
The `www` in `www.foobar.com` is typically a subdomain CNAME (Canonical Name) record. This type of DNS record maps an alias name to the canonical domain name. For example, www.foobar.com might be a CNAME for foobar.com, which is then resolved to an IP address by an A or AAAA record.

## What is the role of the web server
A web server is responsible for handling and responding to incoming HTTP/HTTPS requests from users' web browsers.
It serves static website content such as HTML, CSS, JavaScript, and images, and processes user requests to deliver the appropriate resources.

## What is the role of the application server
An application server processes user requests and executes server-side logic. It handles tasks like processing user inputs, running scripts, and interacting with databases to generate content that is served by the web server.
Examples of application servers include Flask, a web framework using Python for small to medium-sized applications. 

## What is the role of the database
The database stores and manages data for the site. It handles requests from the application server to retrieve, insert, update, or delete data (user information, posts, etc.). It provides a structured way of storing, retrieving, and manipulating data.

## What is the server using to communicate with the computer of the user requesting the website
The server communicates with the user's computer (client) using TCP/IP over HTTP or HTTPS protocols. 
HTTP is used for unencrypted data transfer, while HTTPS, secured by SSL/TLS, encrypts the data for secure transmission.
TCP/IP stands for Transmission Control Protocol/Internet Protocol. It is a set of communication protocols that govern how data is transmitted over the Internet. After obtaining the IP address, the browser establishes a TCP/IP connection to communicate with the web server using the resolved IP address.
This involves a three-way handshake

## SPOF
A Single Point of Failure (SPOF) is a component whose failure can bring down the entire system.

**Examples**
- **Web server**: If the web server fails, the website becomes unavailable.
- **Database**: If the database fails, data retrieval and updates are disrupted.
- **Load balancer**: A single load balancer can be an SPOF if it fails. 

**Load balancer** evenly distributes incoming traffic across multiple web servers. This practice ensures that no single server becomes overloaded it directs traffic to the server with the fewest active connections, to better balance the load.

## Impact of SPOF
#### Downtime when maintenance needed (like deploying new code web server needs to be restarted)
- Essential services become unavailable during maintenance or failure. If you need to restart the web server for maintenance or to deploy new code, the site will be temporarily unavailable.  This downtime can affect the user experience and potentially lead to lost revenue.

#### Cannot scale if too much incoming traffic
- Limited infrastructure may struggle under high traffic, leading to performance degradation. If the infrastructure cannot handle high traffic, the website may become slow or unresponsive, resulting in a poor user experience. Without proper load balancing or scaling mechanisms, the system may fail under heavy load. This is because the capacity of the system is limited to a single server, which can lead to performance problems when traffic is high.

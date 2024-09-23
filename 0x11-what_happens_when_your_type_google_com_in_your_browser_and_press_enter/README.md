#  What happens when you type google.com in your browser and press Enter
![image](https://github.com/user-attachments/assets/9cb448a3-0b9e-459d-a997-ca0cb6067325)

## Description
The project involves explaining in detail the processes that occur when you type "https://www.google.com" into your browser and press Enter. it tests your understanding of the basic workings of the internet, how different layers of the web stack interact, and the role of various network, server, and security components in delivering a web page.

The blog post covers the entire journey of a web request from the client (your browser) to the server and back. This includes network-level operations, DNS resolution, TCP/IP communication, HTTPS/SSL handshake, the role of firewalls, load balancing, web and application server interactions, and how the database is queried and responds. It also explains the browser's role in rendering the final page. The project aims to assess your understanding of network fundamentals, system architecture, DevOps principles, and security practices. 

## Project Structure

| Task | Description | Source Code |
|-----------------------------------|------------------------------------------------------|-----------------------------------------------|
| **0. What Happens When...** | Write a blog post explaining what happens when you type `https://www.google.com` in your browser and press Enter. Your post must cover DNS request, TCP/IP, Firewall, HTTPS/SSL, Load-balancer, Web server, Application server, and Database. | [Link to blog post](#) |
| **1. Everything's Better with a Pretty Diagram** | Add a schema to your blog post illustrating the flow of the request created when you type `https://www.google.com` in your browser and press Enter. The diagram should include DNS resolution, hitting server IP, encryption, firewall, load balancer, web server, application server, and database. | [Link to diagram](#) |
| **2. Contribute!** | Contribute to the `what-happens-when` GitHub repository by submitting a pull request that adds meaningful value. | [Link to pull request](#) |

## Terms
 **DNS Request**: How the browser resolves the domain name to an IP address.
-  When you type `google.com`, the browser checks if it already knows the IP address through its cache. If not, it sends a DNS query to resolve the domain to an IP address.

**TCP/IP**: How a TCP connection is established using the three-way handshake and how the IP protocol handles data transmission.
- Once the IP address is known, the browser initiates a TCP connection to the server using a process called the three-way handshake (SYN, SYN-ACK, ACK).

**Firewall**:How firewalls might inspect and filter traffic to protect the network.
- If the website uses HTTPS, an SSL handshake occurs to establish a secure connection. 

**HTTPS/SSL**: The SSL/TLS handshake that secures the connection when HTTPS is used.
- The browser sends an HTTP request to the server, requesting the webpage.

**Load-Balancer**: How a load balancer might distribute incoming traffic across multiple servers.
- The server processes the request and sends back an HTTP response, which includes the requested resources (HTML, CSS, JavaScript, images, etc.).

**Web Server**: The role of the web server in serving static content and handling requests.
- The browser starts rendering the webpage by parsing the HTML, CSS, and JavaScript.

**Application Server**: How the application server processes dynamic requests.
- The browser continues to fetch and render any additional resources required to fully load the page.

**Database**: How the application server interacts with the database to fetch and store data.

---

## Environment
- **Tools**: Gliffy, Medium/LinkedIn, GitHub

## Requirements

- Understanding of DNS, TCP/IP, Firewall, HTTPS/SSL, Load Balancers, Web Servers, Application Servers, and Databases.
- Ability to write and publish a technical blog post.
- Familiarity with GitHub for contributing to open-source projects.

## Learning Objectives

- Gain a comprehensive understanding of the web stack and how different components interact.
- Improve technical writing skills by explaining complex concepts clearly.
- Contribute to the open-source community by enhancing existing explanations or adding new insights.
---

### Task

#### 0. What Happens When...
- **Description**: Write a blog post explaining what happens when you type `https://www.google.com` in your browser and press Enter.
- **Requirements**:
  - Your post must cover:
    - DNS request
    - TCP/IP
    - Firewall
    - HTTPS/SSL
    - Load-balancer
    - Web server
    - Application server
    - Database
  - Publish your blog post on Medium or LinkedIn.
  - Share the URL of your blog post in your answer file and in the field provided.

  - Directory: `0x11-what_happens_when_your_type_google_com_in_your_browser_and_press_enter`
  - File: `0-blog_post`

#### 1. Everything's Better with a Pretty Diagram
- **Description**: Add a schema to your blog post illustrating the flow of the request created when you type `https://www.google.com` in your browser and press Enter.
- **Diagram should show**:
  - DNS resolution
  - The request hitting server IP on the appropriate port
  - The traffic is encrypted
  - The traffic goes through a firewall
  - The request is distributed via a load balancer
  - The web server answers the request by serving a web page
  - The application server generates the web page
  - The application server requests data from the database
- **Tools**: Gliffy is recommended, but use what fits you best.
- **Share the URL of your diagram image** in your answer file and in the field provided.

  - Directory: `0x11-what_happens_when_your_type_google_com_in_your_browser_and_press_enter`
  - File: `1-what_happen_when_diagram`

#### 2. Contribute!
- **Description**: Help the online community by submitting a pull request to the `what-happens-when` GitHub repository.
- **Requirements**:
  - The pull request must bring meaningful value (not a typo correction or style improvement).
  - Share the pull request URL in your answer file and in the field provided.
- **Link**: [What happens when... GitHub repository](https://github.com/alex/what-happens-when#the-g-key-is-pressed)

  - Directory: `0x11-what_happens_when_your_type_google_com_in_your_browser_and_press_enter`
  - File: `2-contribution-to_what-happens-when_github_answer`

---
## Additional Info
- Follow best practices in technical writing and diagramming to make your content easily understandable.



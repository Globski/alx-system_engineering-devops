# Distributed web infrastructure

## What distribution algorithm your load balancer is configured with and how it works
### Load-balancer(HAProxy)
Load balancers are often used by large websites and high-traffic web applications to distribute incoming traffic evenly across multiple web servers.  This ensures that no server is overloaded. Load balancers use a variety of methods to route incoming requests to the most appropriate server. This distribution eliminates the possibility of a bottleneck developing on any one server. Load balancers keep a constant eye on the back-end servers. By spreading the workload across multiple servers and using only healthy servers, they improve the overall performance, availability, and scalability of the online application by directing traffic only to servers that are working properly. The distribution algorithm used by a load balancer determines how requests are assigned to servers.

#### Distribution Algorithms and how they work
**Round Robin:** The load balancer distributes each incoming request to the next server in a circular order. After reaching the last server, it loops back to the first server.
- **Example**: If there are three servers (A, B, and C), the load balancer sends the first request to A, the second request to B, the third request to C, and the fourth request again to A.

**Least Connections:** The load balancer directs traffic to the server with the fewest active connections. This algorithm helps balance the load more dynamically based on the current number of connections each server is handling.
- **Example**: If server A has 10 active connections, server B has 5, and server C has 3, the load balancer will send the next request to server C.

**Least Response Time:** The load balancer selects the server that responds the quickest to a health check request. This ensures that requests are sent to the server with the fastest response time, which can improve the overall user experience.
- **Example**: If server A responds in 100ms, server B in 150ms, and server C in 200ms, the load balancer will send the request to server A.

**Weighted Round Robin:** Similar to Round Robin, servers are assigned a weight based on their capacity. Servers with higher weights receive more requests.
- **Example**: If server A has a weight of 3, server B has a weight of 2, and server C has a weight of 1, server A will handle three times as many requests as server C.

**Weighted Least Connections:**  Combines Least Connections with weighted servers. Servers with higher weights get more requests, but the load balancer still considers the number of active connections.
- **Example**: If server A has a weight of 3 and 10 connections, server B has a weight of 2 and 5 connections, and server C has a weight of 1 and 3 connections, the load balancer will prioritize server A but still balance connections.

**IP Hash:** Uses a hash of the client’s IP address to determine which server will handle the request. This ensures that the same client consistently connects to the same server, which can be useful for session persistence.
- **Example**: If a client with IP address `192.168.1.10` is hashed and maps to server A, all subsequent requests from this IP address will be directed to server A.

**Least Bandwidth:** Directs traffic to the server that is currently handling the least amount of bandwidth. This helps distribute the load based on the amount of data being processed.
- **Example**: If server A is handling 1GB of bandwidth, server B is handling 500MB, and server C is handling 200MB, the load balancer will direct the next request to server C.

## Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both
Load balancers can operate in either Active-Active or Active-Passive configurations. The main difference between active-active and active-passive setups for a load balancer lies in how they handle incoming traffic and provide redundancy and high availability.
Choosing between Active-Active and Active-Passive setups depends on your specific needs for performance, cost, and redundancy.

**Active-Active:** In an active-active setup for a load balancer, both load balancers are actively distributing traffic at the same time. This means that both load balancers are handling incoming requests and sharing the load evenly between them. This setup provides redundancy and high availability as if one load balancer fails, the other can continue to handle the traffic.
Multiple load balancers are active, so if one fails, others can take over, minimizing downtime. Traffic is distributed among all active load balancers, which can improve performance and resource utilization.
All load balancers are actively managing traffic, providing better load distribution and higher redundancy. Suitable for high-traffic environments where continuous service is crucial.
- **Example**: If you have two load balancers (L1 and L2) in an Active-Active setup, both L1 and L2 receive and distribute traffic. If L1 fails, L2 continues to handle all incoming requests without interruption.

**Active-Passive:** In an active-passive setup, only one load balancer is actively distributing traffic while the other remains on standby. The standby load balancer only takes over if the active load balancer fails. The primary load balancer (active) handles all traffic, while the secondary load balancer (passive) is not utilized during normal operation. The passive load balancer is kept in sync with the active one and becomes operational if the active load balancer encounters a failure.
The standby load balancer incurs lower operational costs as it is not actively processing traffic. Easier to configure and manage since only one load balancer handles traffic at any given time.
One load balancer handles traffic while the other remains on standby, providing redundancy but not utilizing the standby load balancer until a failure occurs. This setup is more cost-effective but may involve more downtime during a failure transition.
- **Example**: If you have two load balancers (L1 and L2) in an Active-Passive setup, L1 handles all traffic while L2 remains in standby mode. If L1 fails, L2 will take over and start handling the traffic.

## How a database Primary-Replica (Master-Slave) cluster works

A Primary-Replica (or Master-Slave) database cluster is a common setup that ensures data safety and smooth service operation. The main database (primary) handles incoming information, such as write operations (inserts, updates, deletes), and captures changes made using a process called change data capture, often through transaction logs to capture changes. These changes are then replicated to one or more replica (or slave) databases. There are two methods for replication: synchronous and asynchronous. In synchronous replication, the primary waits for the replicas to acknowledge the changes before committing, while in asynchronous replication, the primary does not wait for acknowledgments. Replica databases (slaves) keep copies of the data and serve read requests, distributing read load to offload traffic from the primary database. If the primary database goes down, the system can fail over to one of the replica databases to ensure continued service. This setup also provides handy features like backup and disaster recovery, as replicas can restore the data in case of loss or corruption on the primary, reducing data loss risk. Replicas get information from the primary in different ways: either waiting for confirmation or grabbing information as it comes. This kind of setup makes the entire database system more reliable and scalable, ensuring smooth operation even in the event of issues.

## What is the difference between the Primary node and the Replica node regarding the application
**Primary Node**
The primary node is responsible for handling all write operations, including inserts, updates, and deletes. It is where any changes to the data are made, processing all transactions to ensure data consistency and integrity. The primary node is the authoritative source of the data and contains the most up-to-date information. On the other hand, the replica node(s) handles read operations, relieving the primary node of read traffic and improving overall query performance. It also provides redundancy and fault tolerance. In the event of a primary node failure, a replica node can be promoted to the primary role to ensure continuous service. Two additional benefits of the replica node are scalability and support for backup and recovery. Replica nodes can be used to horizontally scale the application by distributing read traffic across multiple nodes. Additionally, they serve as a backup and support disaster recovery by maintaining a copy of the data from the primary node. In summary, the primary node is responsible for write operations, data authority, and high availability, while the replica node primarily serves read operations, provides redundancy, scalability, and supports backup and recovery functions.

## Where are SPOF
Single Point of Failure (SPOF) is any component or part of a system that, if it fails, can cause the entire system to fail. 

**Examples include:**
- **Web server:** If the web server fails, the website becomes unavailable.
- **Database Server**: If the database server fails, data retrieval and updates are disrupted. This can prevent users from accessing or modifying their data and can affect the functionality of the application.
- **Load Balancer**: A single load balancer that fails will result in traffic not being distributed, which can cause the website to become unavailable or experience performance issues. 
- **DNS Server**: If the DNS server fails, users cannot resolve domain names to IP addresses, making the website unreachable by its domain name.
- **Application Server**: Failure of the application server can disrupt the processing of user requests, impacting the functionality of the application or website.
- **Network Components**: Components like routers or switches can also be SPOFs. If they fail, they can disrupt the entire network, affecting all connected services and servers.
- **Power Supply**: The failure of a data center's power supply or backup power solutions can lead to downtime for all hosted services and servers.
- **Firewalls**: If a firewall fails, it could expose the entire network to potential security threats or disrupt access to network resources.

## Security issues (no firewall, no HTTPS)
The lack of HTTPS and firewall protection makes the infrastructure vulnerable. 

**Lack of Firewall**
- Without a firewall, your server and system infrastructure are vulnerable to unauthorized access, malicious attacks, and potential security breaches. 
- Systems without firewalls are more susceptible to attacks such as Distributed Denial of Service (DDoS) attacks, where the attacker overwhelms the server with traffic, causing service disruption.
- A lack of firewall protection increases the risk of data breaches, where sensitive information can be accessed or stolen by malicious actors.

**Lack of HTTPS**
- Without HTTPS, data transmitted between users and your server is sent in plaintext. This makes it vulnerable to interception and eavesdropping by attackers, who can capture and read sensitive information.
- Lack of encryption means data can be altered during transmission, leading to potential data corruption or tampering.
- Modern browsers flag non-HTTPS sites as “Not Secure,” which can deter users from interacting with your site, impacting trust and user experience.
- Without HTTPS, ISPs or other intermediaries might inject unwanted content or ads into web pages. 
 
## No monitoring
Security Issues go unnoticed without proper monitoring tools. Monitoring helps detect issues early, provides insights into performance, and alerts you to potential failures before they impact users. Monitoring is a critical component of maintaining the health and security of your web infrastructure. The absence of monitoring tools can lead to several issues that might compromise the performance, security, and reliability of your systems. 

**Undetected Issues**
- Without monitoring, system failures, crashes, or malfunctions may go unnoticed until they cause significant disruption or downtime.
- The lack of alerts means that problems are detected only after they have escalated, making it more challenging and costly to address issues effectively.
- Issues like high CPU usage, memory leaks, or slow response times may not be detected promptly, leading to degraded performance and a poor user experience.
- Without monitoring, it’s difficult to understand resource utilization and optimize server performance. This can lead to over-provisioning or under-provisioning of resources.
- Monitoring data helps in forecasting future needs based on current trends. The absence of this data makes it harder to plan for scaling and capacity needs.
- Diagnosing performance issues or identifying the root cause of problems becomes more challenging without performance metrics and historical data.
- Without monitoring, security breaches or unauthorized access may go undetected, allowing attackers to exploit vulnerabilities without being noticed.
- Lack of monitoring makes it difficult to detect and respond to security incidents in real-time, increasing the risk of data loss and system compromise.

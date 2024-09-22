## Incident Postmortem Report: Web Stack Debugging #0

![A1](https://github.com/user-attachments/assets/ff78d88f-a20c-4daf-be2b-37dd0b8337a7)

### Incident Overview

**Date of Incident:** July 1, 2024  
**Duration of Outage:** 2 hours  
**Impact:** Users are unable to access the "Hello Holberton" page, resulting in complete downtime for the service.  
**Severity Level:** Sev-2

### Summary

On July 1, 2024, the Apache server within a Docker container failed to serve the expected "Hello Holberton" webpage resulting in a 100% downtime for users attempting to access the web page. Initial user reports indicated that accessing the service resulted in an empty response when querying the server. This incident was critical as it impacted all users attempting to reach the service.

### Timeline of Events

- **10:00 AM**: Users report issues accessing the page.
- **10:05 AM**: Monitoring alerts indicate high error rates.
- **10:10 AM**: Engineering team begins investigation.
- **10:15 AM**: Confirmation that Apache is not running. Surprise, surprise!
- **10:30 AM**: Investigated Docker container setup and found misconfigurations.
- **10:45 AM**: Apache service restarted, and initial tests began.
- **11:00 AM**: Service restored, confirmed operational via tests. “Hello Holberton” is back!
- **11:15 AM**: User notifications sent out regarding service restoration.

### Root Cause Analysis

The primary cause of the incident was a misconfiguration in the Docker container setup that prevented Apache from starting correctly. Additionally, the HTML file intended for the root page was missing, which resulted in the empty response—definitely not the “Hello” we wanted to share!

### Actions Taken

1. **Immediate Remediation:**
   - **Docker Container Initialization:**
     - Ran the Docker container with the following command:
       ```bash
       docker run -p 8080:80 -d -it holbertonschool/265-0
       ```
   - **Container Access:**
     - Accessed the running container:
       ```bash
       docker exec -ti <container_id> /bin/bash
       ```
   - **Apache Installation:**
     - Checked if Apache was installed and installed it if necessary:
       ```bash
       apt-get update && apt-get install -y apache2
       ```
   - **Configuration:**
     - Added a `ServerName` entry to avoid startup warnings:
       ```bash
       echo "ServerName localhost" >> /etc/apache2/apache2.conf
       ```
   - **HTML File Creation:**
     - Created the HTML file to serve:
       ```bash
       echo "Hello Holberton" > /var/www/html/index.html
       ```
   - **Starting Apache Service:**
     - Started the Apache service within the Docker container:
       ```bash
       service apache2 start
       ```

2. **Verification:**
   - **Service Status Check:**
     - Verified that the Apache service was running:
       ```bash
       service apache2 status
       ```
   - **Testing the Setup:**
     - Used `curl` to confirm the page served correctly:
       ```bash
       curl 0:8080
       ```
     - Expected output: "Hello Holberton".

3. **Investigation and Diagnosis:**
   - Reviewed Docker container logs for any errors:
     ```bash
     docker logs <container_id>
     ```
   - Conducted a thorough check of configuration settings to ensure Apache starts automatically on container initialization.

### Additional Debugging Steps

- **Automated Setup Script:**
  - Developed a Bash script to automate the following actions:
    ```bash
    #!/usr/bin/env bash

    apt-get update
    apt-get install -y apache2
    echo "ServerName localhost" >> /etc/apache2/apache2.conf
    echo "Hello Holberton" > /var/www/html/index.html
    service apache2 start
    ```

- **Script Execution:**
  - Made the script executable:
    ```bash
    chmod +x 0-give_me_a_page
    ```
  - Executed the script inside the container to streamline the setup process:
    ```bash
    ./0-give_me_a_page
    ```

### Learnings and Next Steps

- **What Went Well:**
  - The team responded quickly, with investigation efforts initiated within minutes.
  - Effective communication throughout the team ensured rapid identification of the issue.

- **What Didn't Go Well:**
  - The initial misconfiguration could have been avoided with more thorough testing of the Docker setup.
  - Missing HTML files should be monitored to prevent similar incidents.

- **Preventative Measures:**
  - Implement a checklist for setting up Docker containers to ensure all necessary services are installed.
  - Create a simple script that will run tests to automate service verification upon container startup and then confirm that necessary files are present and services are operating properly after deployment.
  - Schedule regular reviews of incident response processes to identify areas for improvement. Organize a training session for the team focused on best practices for Docker and web service deployment.


### Metrics Captured

- **Downtime:** 2 hours
- **Mean Time to Resolution (MTTR):** 50 minutes
- **Severity of the Incident:** Sev-2

### Conclusion

This incident highlighted the importance of thorough configuration checks and the need for robust testing procedures before deployment. By conducting this postmortem, we have identified actionable steps to enhance our incident response process and improve service reliability moving forward. Regular reviews of past incidents will help institutionalize a culture of continuous improvement within the team. 

### Next Steps

1. Schedule a team meeting to discuss findings and preventive measures.
2. Update incident response documentation to reflect changes.
3. Initiate follow-up actions within the next sprint cycle.

![A1](https://github.com/user-attachments/assets/392b232b-6be3-4d85-b282-28a657db7592)

## Additional Note
### Severity Level Rationale

The incident was classified as Sev-2 for several reasons:

- **Impact on Users:** Although the outage resulted in complete downtime for users accessing the "Hello Holberton" page, it did not affect critical business operations or cause significant financial loss. The repercussions were mainly inconveniences related to user experience.

- **Duration:** The outage lasted 2 hours, which is substantial but not long enough to escalate the severity to Sev-1, typically reserved for critical system failures with prolonged outages.

- **Workarounds and Alternatives:** There were no known alternative pages or services affected, but the specific impact was limited to this particular webpage.

- **Response Time:** The engineering team identified and resolved the issue within a reasonable timeframe (50 minutes MTTR), which is characteristic of Sev-2 incidents that are managed effectively.

Overall, Sev-2 signifies a significant yet manageable incident that required attention but was not an existential threat to the service or business operations.

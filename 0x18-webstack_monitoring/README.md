# System-Engineering Devops - Webstack Monitoring

## Description

This project involves setting up monitoring for a web stack using Datadog. Monitoring is crucial for understanding the health and performance of your servers and applications. In this project, you'll set up Datadog to monitor metrics, create dashboards, and ensure proper alerting for your infrastructure.

## Project Structure

| Task | Description | Source Code |
|------|-------------|-------------|
| **0. Sign up for Datadog and install datadog-agent** | Sign up for Datadog, install the Datadog agent on web-01, and configure it. | [How to Use Section](/0x18-webstack_monitoring) |
| **1. Monitor some metrics** | Set up monitors in Datadog to track read and write requests per second. | [How to Use Section](/0x18-webstack_monitoring) |
| **2. Create a dashboard** | Create a Datadog dashboard with at least four widgets to visualize various metrics. | [How to Use Section](/0x18-webstack_monitoring) |

## Objective
Web stack monitoring and setting up the necessary tools for efficient monitoring and alerting.

## Learning Objectives

By the end of this project, you should be able to:

- Explain why monitoring is needed.
- Describe the two main areas of monitoring: application monitoring and server monitoring.
- Understand what access and error logs are for web servers such as Nginx.

## Environment

- **Operating System**: Ubuntu 16.04 LTS

## Requirements

- **Bash Script Requirements**:
- **File Endings:** All files should end with a new line.
- **Executable Scripts:** All Bash scripts must be executable.
- **Shellcheck:** Scripts must pass Shellcheck (version 0.3.7) without errors.
- **Script Header:** The first line of all Bash scripts should be `#!/usr/bin/env bash`, followed by a comment explaining the script’s purpose.
- **API Keys:** Your DataDog API key and application key must be securely stored.

## How to Use

### 1. Set Up Datadog

**Objective:** Install and configure the Datadog agent on your server to start collecting metrics.

**Steps:**

1. **Sign Up for Datadog:**
   - Visit [Datadog’s sign-up page](https://www.datadoghq.com) and create a free account.
   - Select the US1 region when prompted.

2. **Install Datadog Agent on `web-01`:**
   - Log in to your `web-01` server.
   - Follow Datadog’s installation guide for Ubuntu. You can find the specific installation commands on [Datadog’s documentation](https://docs.datadoghq.com/agent/basic_agent_usage/ubuntu/).
   - Use the following commands as a guide:
     ```bash
     DD_AGENT_MAJOR_VERSION=7 DD_API_KEY=<YOUR_DATADOG_API_KEY> bash -c "$(curl -L https://s3.amazonaws.com/dd-agent/scripts/install_script.sh)"
     ```
   - Replace `<YOUR_DATADOG_API_KEY>` with your actual Datadog API key.

3. **Verify Installation:**
   - Check that the Datadog agent is running with the command:
     ```bash
     sudo datadog-agent status
     ```
   - Ensure that `web-01` appears on the Datadog dashboard under the hostname `XX-web-01`.

4. **Create an Application Key:**
   - In the Datadog dashboard, navigate to the API section.
   - Generate an application key and save it securely for future use.

5. **Update Hostname (if needed):**
   - If you need to update the hostname using the Datadog API, follow the instructions in [Datadog’s API documentation](https://docs.datadoghq.com/api/latest/hosts/).
   - Use cURL or your preferred HTTP client to make API requests.

6. **Secure Your API Key:**
   - Ensure your API and application keys are stored securely, possibly in environment variables or a secret management tool.

### 2. Configure Monitors

**Objective:** Set up Datadog monitors to track specific metrics and alert you based on predefined conditions.

**Steps:**

1. **Log In to Datadog:**
   - Go to [Datadog’s dashboard](https://app.datadoghq.com).

2. **Create Monitors:**
   - Navigate to **Monitors** in the left sidebar.
   - Click **New Monitor** and choose the type of monitor you want to create (e.g., Metric Monitor).

3. **Set Up Read Requests Monitor:**
   - For read requests per second:
     - **Monitor Type:** Metric
     - **Metric:** `system.diskio.reads`
     - **Threshold:** Set an appropriate threshold value based on your server’s load.
     - **Alert Conditions:** Configure the alert conditions and notifications as per your requirements.

4. **Set Up Write Requests Monitor:**
   - For write requests per second:
     - **Monitor Type:** Metric
     - **Metric:** `system.diskio.writes`
     - **Threshold:** Set an appropriate threshold value.
     - **Alert Conditions:** Define the alert conditions and notifications.

5. **Save Monitors:**
   - After configuring each monitor, click **Save**.
   - Test the monitors to ensure they trigger alerts under the expected conditions.

### 3. Create and Configure Dashboard

**Objective:** Create a Datadog dashboard to visualize your metrics with various widgets.

**Steps:**

1. **Create a New Dashboard:**
   - Go to the **Dashboards** section in Datadog.
   - Click **New Dashboard** and provide a name for your dashboard.

2. **Add Widgets to Dashboard:**
   - Click **Add Widget** and choose the type of widget you need (e.g., Time Series, Query Value).
   - Configure each widget to display relevant metrics. You can use the following types:
     - **Time Series:** To show metrics over time (e.g., read/write requests).
     - **Query Value:** To show specific metric values.
     - **Top List:** To list top metrics based on specific criteria.

3. **Customize Widgets:**
   - Configure widget settings such as titles, data sources, and visual styles.
   - Arrange the widgets on your dashboard for optimal visualization.

4. **Retrieve Dashboard ID:**
   - Once your dashboard is configured, use the Datadog API to retrieve the dashboard ID:
     ```bash
     curl -X GET "https://api.datadoghq.com/api/v1/dashboard" \
     -H "Content-Type: application/json" \
     -H "DD-API-KEY: <YOUR_DATADOG_API_KEY>" \
     -H "DD-APPLICATION-KEY: <YOUR_DATADOG_APPLICATION_KEY>"
     ```
   - Replace `<YOUR_DATADOG_API_KEY>` and `<YOUR_DATADOG_APPLICATION_KEY>` with your actual keys.

5. **Save Dashboard ID:**
   - Save the dashboard ID in a file named `2-setup_datadog` as required.

4. **Submit Your Work:**
   - Ensure all configurations are correct and your dashboard is properly set up.
   - Validate that your API and application keys are correctly added.

### 4. Verify and Test

1. **Check Monitors:**
   - Verify that your monitors are active and correctly set up.
   - Test the alerts by simulating conditions that would trigger them.

2. **Review Dashboard:**
   - Ensure that your dashboard displays all required metrics and data accurately.
   - Make adjustments as needed based on your observations.

3. **Submit Your Work:**
   - Confirm that all configurations are correct and working.
   - Ensure your dashboard ID and monitor settings are documented and submitted according to your project’s requirements.

## Tasks

### 0. Sign up for Datadog and install datadog-agent

**Objective:** Sign up for a free Datadog account, install the Datadog agent on `web-01`, and configure it. When signing up, you’ll have the option of selecting statistics from your current stack that Datadog can monitor for you.

![A1](https://github.com/user-attachments/assets/b26dfb1e-0731-45c4-97b1-5fbcfd2c9104)

**Steps:**

1. **Sign Up:**
   - Go to [Datadog’s website](https://www.datadoghq.com) and sign up for an account using the US1 region.

2. **Install Datadog Agent on `web-01`:**
   - Follow the instructions on the Datadog website to install the agent. Ensure `web-01` is visible under the hostname `XX-web-01` in Datadog.

3. **Create an Application Key:**
   - In the Datadog dashboard, generate an application key and ensure it is stored securely.

4. **Update Hostname (if needed):**
   - Use the Datadog API to update the hostname if necessary. You can validate this using the API.

5. **Secure Your API Key:**
   - Copy-paste your DataDog API key and application key into your Intranet user profile as required.

- After installation, verify using Datadog’s API if needed.

### 1. Monitor Some Metrics

Among the litany of data your monitoring service can report to you are system metrics. You can use these metrics to determine statistics such as reads/writes per second, which can help your company determine if/how they should scale. Set up some monitors within the Datadog dashboard to monitor and alert you of a few.  You can read about the various system metrics that you can monitor here: [System Check](https://docs.datadoghq.com/integrations/system/)

**Objective:** Set up Datadog monitors to track system metrics, specifically read and write requests per second. 

![A1](https://github.com/user-attachments/assets/0a8b2957-3da6-4e07-91d8-f27bc4b27edb)

**Steps:**

1. **Create Monitors:**
   - **Read Requests Monitor:**
     - In the Datadog dashboard, create a monitor for the number of read requests issued to the device per second.
   - **Write Requests Monitor:**
     - Create another monitor for the number of write requests issued to the device per second.

2. **Configuration:**
   - Access the Datadog dashboard and navigate to the Monitors section.
   - Create new monitors with appropriate thresholds and alert conditions.

- Access Datadog's dashboard to set up and configure the monitors based on the metrics provided.

### 2. Create a Dashboard

**Objective:** Create a Datadog dashboard with at least four widgets to visualize different metrics.

**Steps:**

1. **Create a New Dashboard:**
   - Go to the Dashboards section in Datadog.
   - Add at least 4 widgets to display various metrics.
   - Create a file named `2-setup_datadog` with the dashboard ID on the first line.

2. **Add Widgets:**
   - Choose widgets that best represent the metrics you want to visualize.
   - Customize the widgets to show relevant data and metrics.

3. **Retrieve Dashboard ID:**
   - Use Datadog’s API to get the dashboard ID.
   - Save the dashboard ID in a file named `2-setup_datadog`.

Note: in order to get the id of your dashboard, you may need to use [Datadog’s API](https://intranet.alxswe.com/rltoken/n2KPoJtwzx8LjCpmCB4KVQ)

## Additional Information

- **Datadog Documentation:** Refer to Datadog’s official documentation for more details on configuring monitors and dashboards.
- **Monitoring Best Practices:** Regularly review and update your monitoring setup to ensure it meets the evolving needs of your infrastructure.


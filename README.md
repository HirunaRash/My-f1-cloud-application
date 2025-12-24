🏎️ F1 Data Insights Dashboard
https://my-f1-cloud-application.streamlit.app/

A full-stack data visualization project leveraging Python, Pandas, and Streamlit, deployed on a custom Ubuntu VM via Google Cloud Platform (GCP).

📌 Project Overview

This dashboard provides deep-dive analytics into Formula 1 race data. Unlike simple local scripts, this project was architected to run on a production-ready cloud environment, requiring custom VPC networking and infrastructure configuration.

🛠️ Tech Stack

Language: Python
Data Processing: Pandas, NumPy
Frontend/UI: Streamlit
Infrastructure: Google Compute Engine (GCE)
OS: Ubuntu 22.04 LTS
Networking: GCP VPC Firewall & Network Tags

🚀 Cloud Infrastructure & Networking

The highlight of this deployment was overcoming the "Connection Refused" bottleneck by configuring the cloud networking stack from scratch.
The Challenge: Ingress Connectivity
By default, GCP blocks all external traffic to a VM. To make the Streamlit app accessible on port 8501, I implemented the following:
VPC Firewall Policy: Created an ingress rule for tcp:8504.

Diagnostic Tooling: I used ss -tulpn to monitor socket states and verify that the application was correctly bound to the network interface.

📊 Dashboard Features

Race Winners
Championship Standings
Team Stats

📝 Lessons Learned

Managing Cloud VPCs and understanding how ingress traffic flows.
The difference between Loopback (127.0.0.1) and Global (0.0.0.0) address binding in Linux.
Cleaning and transforming complex nested F1 datasets using Pandas.




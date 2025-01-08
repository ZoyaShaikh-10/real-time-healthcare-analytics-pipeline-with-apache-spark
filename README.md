

# Real-Time Healthcare Patient Monitoring System with Apache Spark and Azure Event Hub

## Overview
This project implements a real-time healthcare monitoring system using Azure Event Hub, Apache Spark, and other Azure services. The system ingests and processes healthcare safety reports to analyze patient data in real-time. The data, which includes patient reactions to drugs, age, and other health-related metrics, is processed using Spark for anomaly detection, trend analysis, and other insights.

## High-Level Architecture

**1. Python:** Used for generating mock data and integrating the data flow into the system.

**2. Azure Event Hub:** A managed service that facilitates the ingestion of high-throughput API real-time data.

**3. Apache Spark (Azure Databricks):** Real-time processing of the ingested data for analytics, anomaly detection, and transformation.

**4. Azure SQL Database:** Stores processed data for querying and reporting.

**5. Power BI:** For visualization and reporting of the processed healthcare data.

## Project WorkFlow

**1. Mock Data Generation:**

-   A Python script generates mock healthcare safety report data in the JSON format

**2. Data Ingestion:**

-   The Python script continuously generates this mock data and sends it to Azure Event Hub for ingestion.
-   Azure Event Hub allows for the ingestion of large volumes of real-time data, handling each event in a scalable and low-latency manner.

**3. Data Processing:**

-   Apache Spark processes the real-time data from Event Hub using Azure Databricks.

**4. Data Storage:**

-   After processing, the data is stored in Azure SQL Database for structured querying and reporting.


**5. Visualization:**

-   Data is visualized using Power BI to provide healthcare providers with insights on patient safety and drug reactions.
-   Dashboards are updated in real-time to reflect the most current patient monitoring data.


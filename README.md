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
![plot](./healtcare-pipeline-image/eventhub_data_ingestion.png)


**3. Data Processing:**

-   Apache Spark processes the real-time data from Event Hub using Azure Databricks.
![plot](./healtcare-pipeline-image/databrick_load_data.png)
![plot](./healtcare-pipeline-image/databrick_transform_data.png)


**4. Data Storage:**

-   After processing, the data is stored in Azure SQL Database for structured querying and reporting.
![plot](./healtcare-pipeline-image/SQL_load_data.png)



**5. Visualization:**

-   Data is visualized using Power BI to provide healthcare providers with insights on patient safety and drug reactions.
-   Dashboards are updated in real-time to reflect the most current patient monitoring data.
```
## File Structure
├──healthcare-pipeline-dev/
├──├──event_data_transformation_to_sql.ipynb # nb to exec in databrick workspace
├── sample_data
├──├──├──sample.json ## mock data
|── eventhub_api_data_ingester.py ## uploads data to event hub
├── generate_healthcare_streaming_data.py ## generates mock data
└── README.md  # This File
```


## Project Execution
**Prerequisites**

- Azure Event Hub configured for ingestion.
- Azure Databricks workspace.
- Azure SQL Database setup with required tables.
- Power BI installed for visualization.

Steps

- Run the `generate_healthcare_streaming_data.py` script to generate mock data 
- Run the `eventhub_api_data_ingester.py` to ingest the data to Event Hub.
- Use `event_data_transformation_to_sql.ipynb` in Databricks workspace to process and transform the data and to store the transform data to Azure SQL Database.
- Visualize the data using Power BI dashboards.
Database Schema

```

Table: PatientAdverseEventReport
Columns:
safetyreportid (STRING)
transmissiondate_converted (DATE)
patientonsetage (INT)
patientsex (INT)
reaction.reactionmeddrapt (STRING)
drug_name (STRING)
drug_characterization (INT)
drug_indication (STRING)
is_overdose (BOOLEAN)

```

**Expected Insights**

- Common patient reactions by drug type.
- Age groups most affected by specific reactions.
- Trends in drug-related overdose cases.

This workflow ensures real-time patient safety monitoring, aiding healthcare providers in making informed decisions.



# Real-Time Healthcare Analytics Pipeline with Azure

## Overview
This project demonstrates how to build a real-time healthcare analytics pipeline using Azure Event Hub, Azure Stream Analytics, Azure SQL Database, and Power BI to monitor health data such as patient reactions, drug administration errors, and overdose incidents. The pipeline processes real-time reports from pharmaceutical safety data (e.g., Food And Drugs Administration (FDA) reports). It visualizes key metrics like patient age, drug usage, and reaction types for proactive monitoring and insights.


## High-Level Architecture

**1. Healthcare Safety Reports**:
-  This data includes patient reactions, drug abuse cases, and administration errors. For example, reactions like "DRUG ADMINISTRATION ERROR" or "OVERDOSE" are tracked.

**2. Azure Event Hub**:


-  Azure Event Hub is used to ingest real-time healthcare safety reports, including incident details such as reaction types, drug usage, patient age, and gender.


**3. Azure Stream Analytics**:

-  This component processes incoming reports, performs transformations (e.g., aggregations, filtering), and prepares the data for storage and analysis.

**4. Azure SQL Database:**

-  The processed data is stored in Azure SQL Database, which can be queried for analysis and reporting.

**5. Power BI:**

-  Power BI provides real-time dashboards to monitor safety metrics, such as the number of overdose incidents, drug-related reactions, and trends in patient demographics (e.g., age and sex).


## Project Workflow

**1. Data Generation:**

-  Real-time safety reports from the pharmaceutical industry, such as FDA data, are used. Reports include details like patient reactions (e.g., "DRUG ADMINISTRATION ERROR"), drug information (e.g., "DURAGESIC-100"), and patient details (age, sex, etc.).

**2. Data Ingestion:**

-  The real-time reports are sent to Azure Event Hub for processing. This could involve data from sources like FDA Public Use or other pharmaceutical safety systems.

**3. Data Processing:**

-  Azure Stream Analytics processes the data to identify and transform key health events. For example, reaction types like "OVERDOSE" and "DRUG ADMINISTRATION ERROR" are extracted and prepared for storage.

**4. Data Storage:**

-  The processed data is stored in an Azure SQL Database to enable detailed querying, tracking, and analysis.

**5. Data Visualization:**

-  Power BI provides interactive dashboards and real-time monitoring of key metrics such as patient reactions, drug abuse incidents, age distribution, and reaction types.

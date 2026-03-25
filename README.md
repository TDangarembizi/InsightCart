# 🧠 InsightCart

**Turning raw e-commerce data into actionable business insights using scalable data engineering and analytics tools.**

---

## 📌 Overview
**InsightCart** is a scalable e-commerce analytics pipeline that processes, transforms, and analyses transactional data. The system uses PySpark on Apache Spark within Databricks to build analytics-ready datasets, which are then visualised through interactive dashboards in Microsoft Power BI.

This project demonstrates an end-to-end data workflow, from raw data ingestion to business intelligence reporting, with optional Excel export functionality.

---

## 🏗️ Architecture

Data Source (CSV / Generated Data) </br>
↓ </br>
Databricks (PySpark Processing) </br>
↓ </br>
Delta Tables (Storage Layer) </br>
↓ </br>
Power BI Dashboard (Visualisation) </br>
↓ </br>
Excel Reports (Export Feature)

---

## ⚙️ Tech Stack

- **Processing:** PySpark (Apache Spark)  
- **Platform:** Databricks  
- **Visualisation:** Microsoft Power BI  
- **Storage:** Delta Tables / SQL Warehouse  
- **Language:** Python  

---

## 📊 Features

- Data ingestion from raw CSV or generated datasets  
- Data cleaning and transformation using PySpark  
- Star schema data modelling (fact and dimension tables)  
- KPI generation (revenue, average order value, sales trends)  
- Scalable data storage using Delta tables  
- Interactive dashboards in Power BI  
- Automated Excel report generation  

---

## 🗃️ Data Model

### Fact Table
- **Sales**
  - order_id  
  - customer_id  
  - product_id  
  - quantity  
  - unit_price  
  - total_price  
  - order_date  

### Dimension Tables

- **Customers**
  - customer_id  
  - name  
  - email  
  - country  
  - signup_date  

- **Products**
  - product_id  
  - product_name  
  - category  
  - price
  - product_id
  - stars
  - reviews
  - is_best_seller

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/TDangarembizi/InsightCart.git
cd InsightCart
```

### 2. Set up environment
```bash
pip install -r requirements.txt
```

### 3. Run data pipeline 
Execute notebooks in order:
	1.	Data ingestion
	2.	Data cleaning
	3.	Transformations
	4.	Aggregations
	5.	Delta storage
	6.	Excel export (optional)

## 📈 Power BI Dashboard
The dashboard includes:
-	Revenue trends over time
-	Top-performing products
-	Customer insights
-	Key performance indicators (KPIs)

## Usage
1.	Connect Microsoft Power BI to your Databricks SQL endpoint
2.	Load Delta tables
3.	Open or build the .pbix dashboard

## 📤 Excel Export
Processed datasets can be exported as Excel reports for offline analysis and sharing. This is implemented using PySpark to Pandas conversion and automated scripts.

## 🔮 Future Improvements
- Real-time data streaming with Spark Structured Streaming
-	API layer (FastAPI)
-	Automated scheduling (daily pipelines)
-	Cloud deployment (AWS / Azure)

## 💼 Project Value
This project demonstrates:
-	End-to-end data pipeline development
-	Big data processing with PySpark
-	Data modelling and transformation
-	Business intelligence and reporting

## Data Sources
-   Product data from https://www.kaggle.com/datasets/asaniczka/amazon-uk-products-dataset-2023
-   Customer data generated using Faker

## 👤 Author
Tinotenda Dangarembizi

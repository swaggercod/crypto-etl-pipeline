# Crypto ETL Data Pipeline

A lightweight, automated ETL (Extract, Transform, Load) pipeline built with Python and Pandas.

## Overview
This project demonstrates a foundational Data Engineering workflow. It extracts real-time cryptocurrency pricing data (Bitcoin & Ethereum) from the public CoinGecko API, transforms the nested JSON response into a structured tabular format using Pandas, and loads it into a persistent local CSV data store. 

This project was built to showcase my ability to handle API requests, perform data transformation, and write clean, documented Python code.

## Tech Stack
* **Language:** Python 3.x
* **Libraries:** `pandas`, `requests`
* **Data Source:** CoinGecko REST API
* **Output:** Local `.csv` storage (Data Warehouse simulation)

## How to Run
1. Clone this repository.
2. Install the required dependencies:
   `pip install requests pandas`
3. Run the pipeline:
   `python crypto_pipeline.py`

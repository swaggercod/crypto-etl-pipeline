import requests
import pandas as pd
import os
from datetime import datetime

def run_crypto_etl_pipeline():

    
    api_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd&include_24hr_change=true"
    
    print("[1/3] EXTRACT: Fetching real-time market data from remote API...")
    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            raw_data = response.json()
            print("[2/3] TRANSFORM: Parsing raw JSON and structuring data...")
            
            
            cleaned_market_data = [
                {
                    "Coin": "Bitcoin",
                    "Price_USD": raw_data["bitcoin"]["usd"],
                    "24h_Change_%": round(raw_data["bitcoin"]["usd_24h_change"], 2),
                    "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                },
                {
                    "Coin": "Ethereum",
                    "Price_USD": raw_data["ethereum"]["usd"],
                    "24h_Change_%": round(raw_data["ethereum"]["usd_24h_change"], 2),
                    "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            ]
            
            
            df = pd.DataFrame(cleaned_market_data)
            
            print("[3/3] LOAD: Appending transformed data to local CSV storage...")
            target_file = "crypto_market_data.csv"
            
           
            if os.path.exists(target_file):
                df.to_csv(target_file, mode='a', header=False, index=False)
            else:
                
                df.to_csv(target_file, mode='w', header=True, index=False)
                
            print(f"ETL Pipeline Process Completed Successfully! Target File: '{target_file}'")
            
        else:
            print(f"API Error: Failed to fetch data. HTTP Status Code: {response.status_code}")
            
    except Exception as error:
        print(f"Pipeline Execution Failed due to connection or runtime error: {error}")

if __name__ == "__main__":
    run_crypto_etl_pipeline()
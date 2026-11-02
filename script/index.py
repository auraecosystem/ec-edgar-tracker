import requests
import pandas as pd

headers = {
    'User-Agent': 'YourName YourEmail@example.com',
    'Accept-Encoding': 'gzip, deflate'
}

def parse_daily_sec_index():
    # Example URL for a daily SEC index file
    url = "https://sec.gov"
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Could not fetch the daily index map.")
        return
        
    lines = response.text.split("\n")
    
    # Skip the descriptive metadata text headers until we reach the data rows
    data_rows = []
    start_parsing = False
    
    for line in lines:
        if "CIK|Company Name|Form Type|Date Filed|Filename" in line:
            start_parsing = True
            continue # skip the header line itself
        if "--------------------------------------------------------" in line:
            continue
            
        if start_parsing and "|" in line:
            parts = line.strip().split("|")
            if len(parts) == 5:
                data_rows.append(parts)
                
    # Load into a clean DataFrame map
    df = pd.DataFrame(data_rows, columns=["CIK", "Company Name", "Form Type", "Date Filed", "Filename"])
    
    # Filter for Apple (CIK 320193) or specific filings instantly
    apple_filings = df[df["CIK"] == "320193"]
    return apple_filings

if __name__ == "__main__":
    apple_map = parse_daily_sec_index()
    print(apple_map.head())

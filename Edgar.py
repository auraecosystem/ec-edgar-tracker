import os
import time
import requests

# 1. Update these headers to identify yourself (Mandatory by SEC policy)
HEADERS = {
    "User-Agent": "YourOrganization Name contact_email@example.com",
    "Accept-Encoding": "gzip, deflate"
}

def download_sec_index(year: int, quarter: int, output_dir: str = "sec_indexes"):
    """
    Downloads the master.zip index file for a given year and quarter 
    from the modern SEC HTTPS archives.
    """
    # Create local storage directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # Construct the modern HTTPS URL mirroring the old FTP structure
    # Example: https://sec.gov
    url = f"https://sec.gov{year}/QTR{quarter}/master.zip"
    
    file_name = f"master_{year}_Q{quarter}.zip"
    output_path = os.path.join(output_dir, file_name)
    
    print(f"Connecting to SEC Archives: {url}...")
    
    try:
        # Stream the download to be memory efficient
        response = requests.get(url, headers=HEADERS, stream=True, timeout=30)
        
        # Catch common issues like invalid year/quarter (404) or missing User-Agent (403)
        response.raise_for_status()
        
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    
        print(f"Success! File saved to: {output_path}")
        
    except requests.exceptions.HTTPError as e:
        if response.status_code == 403:
            print("Error 403 Forbidden: Ensure your User-Agent header is set correctly.")
        elif response.status_code == 404:
            print(f"Error 404 Not Found: Check if {year} Q{quarter} is available yet.")
        else:
            print(f"HTTP Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example: Download the index for 2026 Quarter 1
    # Note: Ensure you respect the SEC rate limit (max 10 requests per second)
    download_sec_index(year=2026, quarter=1)
    
    # Optional: Small pause if you loop through multiple quarters
    time.sleep(0.2)

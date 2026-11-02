import requests

# 1. Define the target URL
url = "https://sec.gov" # SEC API endpoint for Apple
filing_txt_url = "https://sec.gov"

# 2. Mandatory SEC Header: Declare your Company Name and Email Address
headers = {
    'User-Agent': 'YourCompanyName Admin Contact (your-email@example.com)',
    'Accept-Encoding': 'gzip, deflate'
}

def download_filing(url):
    print(f"Requesting data from SEC...")
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        with open("apple_subsidiary_filing.txt", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("Success! Saved to apple_subsidiary_filing.txt")
    else:
        print(f"Failed. Status Code: {response.status_code}")
        print("Check if your User-Agent header meets SEC compliance rules.")

if __name__ == "__main__":
    download_filing(filing_txt_url)

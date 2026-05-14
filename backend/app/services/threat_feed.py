import requests

API_KEY = "YOUR_ABUSEIPDB_KEY"

def check_ip(ip):
    response = requests.get(
        "https://api.abuseipdb.com/api/v2/check",
        headers={
            "Key": API_KEY,
            "Accept": "application/json"
        },
        params={
            "ipAddress": ip
        }
    )
    return response.json()
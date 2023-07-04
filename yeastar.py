import time
from urllib.parse import urlencode

base_url = "https://197.248.2.92:8088/"
api_path = "/api/call_schedule_report/download"
access_token = "your_access_token"

# Generate the timestamp
timestamp = str(int(time.time()))

# Construct the query parameters
query_params = {
    "access_token": access_token,
    "timestamp": timestamp
}

# Append the query parameters to the URL
url = f"{base_url}{api_path}?{urlencode(query_params)}"

print(url)

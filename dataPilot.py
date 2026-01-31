# import requests

# TOKEN_URL = "https://api.ouraring.com/oauth/token"

# data = {
#     "grant_type": "authorization_code",
#     "code": "your_code_here",
#     "redirect_uri": "http://localhost:8080",
#     "client_id": "client_id_here",
#     "client_secret": "client_secret_here"
# }

# response = requests.post(TOKEN_URL, data=data)
# response.raise_for_status()

# tokens = response.json()
# print(tokens)
# Use printed tokens for access_token

import requests
import pandas as pd
# import os

ACCESS_TOKEN = "ACCESS_TOKEN_HERE"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

url = "https://api.ouraring.com/v2/usercollection/heartrate"

# heartrate during day + sleep, HRV, steps

params = {
    "start_datetime": "2026-01-20T00:00:00",
    "end_datetime": "2026-01-28T23:59:59"
}

# Ensure params are large enough to capture all day

r = requests.get(url, headers = headers, params = params)
r.raise_for_status()

data = r.json()["data"]
df = pd.DataFrame(data)

# print(df.head())      # View data

df["timestamp"] = pd.to_datetime(df["timestamp"])

df.to_csv(
    "oura_heartrate_pilot.csv",
    index = False
)

# Find where the file went
# print("Saving to:", os.getcwd())
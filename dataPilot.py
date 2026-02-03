import requests
import pandas as pd
import os

# install packages: python -m pip install requests

# CODE FOR GETTING INFORMATION FROM OuraAPI
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
# print(tokens)                         # Use printed tokens for access_token

ACCESS_TOKEN = "ACCESS_TOKEN_HERE"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

# url changes depending on what you want to
url = "https://api.ouraring.com/v2/usercollection/heartrate"

# collect: heartrate during day + sleep, HRV, steps

# Ensure params are large enough to capture all day
params = {
    "start_datetime": "2026-01-20T00:00:00",
    "end_datetime": "2026-01-28T23:59:59"
}

r = requests.get(url, headers = headers, params = params)
r.raise_for_status()

data = r.json()["data"]
df = pd.DataFrame(data)                 # Convert data into df

# print(df.head())                      # View data

df["timestamp"] = pd.to_datetime(df["timestamp"])

# Convert df to csv to be saved locally
df.to_csv(
    "oura_heartrate_pilot.csv",
    index = False
)

# print("Saving to:", os.getcwd())      # Find where the file went
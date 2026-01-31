# import requests

# TOKEN_URL = "https://api.ouraring.com/oauth/token"

# data = {
#     "grant_type": "authorization_code",
#     "code": "ug8ruzyKJYk6GJ4a4Xcclv3C85TyTJC8",
#     "redirect_uri": "http://localhost:8080",
#     "client_id": "9fd81580-c34c-4001-95cb-be2eb6a57105",
#     "client_secret": "rjVU4lC9sjqyOcV2iQm1XnQFd8fQQGTR-1XiSiOez0o"
# }

# response = requests.post(TOKEN_URL, data=data)
# response.raise_for_status()

# tokens = response.json()
# print(tokens)
# Use printed tokens for access_token

import requests
import pandas as pd
# import os

ACCESS_TOKEN = "_0XBPWQQ_ba1dc679-a6fe-4c21-942e-0da6269ca943"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

url = "https://api.ouraring.com/v2/usercollection/heartrate"

# heartrate during day + sleep, HRV, steps

params = {
    "start_datetime": "2026-01-20T00:00:00",
    "end_datetime": "2026-01-28T23:59:59"
}

r = requests.get(url, headers = headers, params = params)
r.raise_for_status()

data = r.json()["data"]
df = pd.DataFrame(data)

# print(df.head())
# View data

df["timestamp"] = pd.to_datetime(df["timestamp"])

df.to_csv(
    "oura_heartrate_pilot.csv",
    index = False
)

# Find where the file went
# print("Saving to:", os.getcwd())

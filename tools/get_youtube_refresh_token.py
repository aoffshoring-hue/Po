#!/usr/bin/env python3
"""ONE-TIME setup, run on your own PC (not on GitHub).

1. Google Cloud Console -> create a project -> enable "YouTube Data API v3"
2. OAuth consent screen -> add your Google account as test user, then publish it ("In production")
3. Credentials -> OAuth client ID -> type "Desktop app" -> download as client_secret.json
4. pip install google-auth-oauthlib && python get_youtube_refresh_token.py
5. Log in with the account that owns the YouTube channel
6. Copy the 3 printed values into GitHub -> Settings -> Secrets and variables -> Actions
"""
import json
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/youtube.upload", "https://www.googleapis.com/auth/youtube"]
flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
creds = flow.run_local_server(port=0, access_type="offline", prompt="consent")
info = json.load(open("client_secret.json"))
info = info.get("installed") or info.get("web")
print("\nYT_CLIENT_ID     =", info["client_id"])
print("YT_CLIENT_SECRET =", info["client_secret"])
print("YT_REFRESH_TOKEN =", creds.refresh_token)

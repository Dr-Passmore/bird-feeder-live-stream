import os
import google.auth
from googleapiclient.discovery import build

# Set the path to your service account key file
service_account_key_file = "serviceKey.json"

# Set the API service name and version
api_service_name = "youtube"
api_version = "v3"

# Create credentials using the service account key file
credentials, project = google.auth.load_credentials_from_file(service_account_key_file, scopes=["https://www.googleapis.com/auth/youtube.force-ssl"])

# Build the YouTube API client
youtube = build(api_service_name, api_version, credentials=credentials)

# Now you can make API requests using the youtube object
# For example, let's retrieve the live chat ID
request = youtube.liveBroadcasts().list(
    part="snippet",
    mine=True
)
response = request.execute()

# Extract the live chat ID from the first live broadcast
if "items" in response:
    live_broadcast = response["items"][0]
    live_chat_id = live_broadcast["snippet"]["liveChatId"]
    print(f"Live Chat ID: {live_chat_id}")
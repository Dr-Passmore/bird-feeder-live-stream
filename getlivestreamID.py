import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def get_live_chat_id():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "clientYoutube.json"

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    # Request the live broadcasts associated with your channel
    request = youtube.liveBroadcasts().list(
        part="snippet",
        mine=True
    )
    response = request.execute()

    # Extract the live chat ID from the first live broadcast
    if "items" in response:
        live_broadcast = response["items"][0]
        live_chat_id = live_broadcast["snippet"]["liveChatId"]
        return live_chat_id

    return None

# Call the function to get the live chat ID
live_chat_id = get_live_chat_id()
print(f"Live Chat ID: {live_chat_id}")
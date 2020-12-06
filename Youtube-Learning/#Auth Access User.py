import os
import pickle
from google.auth import credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

credentials = None

if os.path.exists('token.pickle'):
    print('Loading Credentials From File...')
    with open('token.pickle','rb') as token:
        credentials = pickle.load(token)

if not credentials or not credentials.valid:
    if credentials and credentials.expired and credentials.refresh_token:
        print('Refreshing Access Token...')
        credentials.refresh(Request())
    else:
        print('Fetching New Token...')
        flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json',
            scopes=['https://www.googleapis.com/auth/youtube.readonly'])

        flow.run_local_server(port=8080, prompt='consent',authorization_prompt_message='')
        credentials = flow.credentials

        with open('token.pickle','wb') as token:
            print('Saving Credentials For Future Use...')
            pickle.dump(credentials,token)


youtube = build('youtube','v3',credentials=credentials)

request = youtube.playlistItems().list(part='status , contentDetails',playlistId='UUCezIgC97PvUuR4_gbFUs5g')

response = request.execute()

for item in response['items']:
    vidId = item['contentDetails']['videoId']
    link = f"https://youtu.be/{vidId}"
    print(link)
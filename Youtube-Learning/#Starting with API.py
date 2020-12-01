
# Using Youtube API.

from googleapiclient.discovery import build
import os

youtube = build('youtube','v3', developerKey=os.environ.get('YT_API'))

request = youtube.channels().list(
    part='statistics',
    id='UCCezIgC97PvUuR4_gbFUs5g'
)

response = request.execute()

print(response)
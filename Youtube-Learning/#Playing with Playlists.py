# Accessing Playlists

from googleapiclient.discovery import build
import os
import re
from datetime import timedelta


youtube = build('youtube','v3', developerKey=os.environ.get('YT_API'))

hours_pattern = re.compile(r'(\d+)H')
minutes_pattern = re.compile(r'(\d+)M')
seconds_pattern = re.compile(r'(\d+)S')

total_seconds = 0
nextPageToken = None

while True:
    pl_request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId='PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME',
        maxResults=50,
        pageToken=nextPageToken
    )

    pl_response = pl_request.execute()

    vid_ids = [item['contentDetails']['videoId'] for item in pl_response['items']]

    STRvid_ids = ','.join(vid_ids)


    vid_request = youtube.videos().list(
        part='contentDetails',
        id= STRvid_ids
    )

    vid_response = vid_request.execute()

    duration = [item['contentDetails']['duration'] for item in vid_response['items']]

    for i in duration:
        hours = hours_pattern.search(i)
        minutes = minutes_pattern.search(i)
        seconds = seconds_pattern.search(i)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        video_seconds = timedelta(
            hours=hours,
            minutes=minutes,
            seconds=seconds
        ).total_seconds()

        total_seconds += video_seconds


    nextPageToken = pl_response.get('nextPageToken')

    if not nextPageToken:
        break

total_seconds = int(total_seconds)

minutes,seconds = divmod(total_seconds,60)
hours,minutes = divmod(minutes,60)

pl_runtime = timedelta(
    hours= hours,
    minutes= minutes,
    seconds= seconds
)

print(pl_runtime)
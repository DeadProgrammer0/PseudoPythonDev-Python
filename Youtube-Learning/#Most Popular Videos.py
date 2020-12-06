# Finding most popular videos of playlist.

#* Requirements.
from googleapiclient.discovery import build
import os

#* API Building.
youtube = build('youtube','v3', developerKey=os.environ.get('YT_API'))

#* Variables.
pl_id= 'PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME'
nextPageToken = None
videos = []

#* Main loop for accessing all videos of the Playlist.
while True:

    #* Getting Video IDs.
    pl_request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId=pl_id,
        maxResults=50,
        pageToken=nextPageToken)
    pl_response = pl_request.execute()

    vid_ids = [item['contentDetails']['videoId'] for item in pl_response['items']]

    #* Getting video details.
    STRvid_ids = ','.join(vid_ids)
    vid_request = youtube.videos().list(
        part='statistics,snippet',
        id= STRvid_ids)
    vid_response = vid_request.execute()       


    vid_views= [item['statistics']['viewCount'] for item in vid_response['items']]

    titles_tmp= [item['snippet']['title'] for item in vid_response['items']]

    vid_titles = []
    for i in titles_tmp:
        edit = i.split('|')[0]
        vid_titles.append(edit)

    videos_tmp = [{'views':view,'url':f'https://youtu.be/{url}','title':f'( {title})' } for view, url, title in zip(vid_views, vid_ids, vid_titles)]

    for item in videos_tmp:
        videos.append(item)

    nextPageToken = pl_response.get('nextPageToken')
    if not nextPageToken:
        break

videos.sort(key=lambda vid:vid['views'],reverse=True)

for video in videos[:10]:
    print(video['url'],video['views'],video['title'])


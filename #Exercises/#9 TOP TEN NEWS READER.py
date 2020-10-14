
from win32com.client import Dispatch 
speak = Dispatch("SAPI.SpVoice")
import os 
import json
import requests
import unicodedata

if __name__ == "__main__":
        
    api = os.environ['NEWS_API']

    url = 'https://newsapi.org/v2/everything?'

    parameters = {
        'sources':'the-hindu',
        'domains':'http://www.thehindu.com/',
        'sort_by':'publishedAt',
        'page':1,
        'pageSize':10,
        'language':'en',
        'content':500,
        'apiKey':api
    }

    response = requests.get(url,params=parameters)

    response_json = response.json()
    with open('headlines.json','w') as json_file:
        json.dump(response_json,json_file,indent=True)


    with open('headlines.json','r') as json_file:
        json_data = json.load(json_file)

    TXT_file = open('Articles.txt','a')
    TXT_file.seek(0)
    TXT_file.truncate()

    for article,num in zip(json_data['articles'],range(1,len(json_data['articles'])+1)):
        title = article['title']
        title = unicodedata.normalize('NFKD', title).encode('ascii', 'ignore')
        description = article['description']
        description = unicodedata.normalize('NFKD', description).encode('ascii', 'ignore')
        if article['content'] != None:
            content = article['content']
            content = content[:-13]
        else:
            content = 'No more info on this topic.'
        content = unicodedata.normalize('NFKD', content).encode('ascii', 'ignore')
        news_url = article['url']
        publish_time = article['publishedAt']
        publish_time = publish_time.split('T')
        publish_time = f'Time : {publish_time[1][:-1]} | Date : {publish_time[0]}'
        author = article['author']
        
        if num == 1:
            Headline = f'Headline Number {num}. Title : {title}\nDetails : {description}.\n More Info : {content[:-13]}\n For more details and link of Articles open Articles.txt.'
        else:
            Headline = f'\n\nNext News. Headline Number {num}. Title : {title}\nDetails : {description}.\n More Info : {content}\n For more details and link of Articles open Articles.txt.'

        TXT_content = f'\n\nHeadline {num}\nURL - {news_url}\nPublished at - {publish_time}\nAuthor - {author}'
        TXT_file.write(TXT_content)

        speak.Speak(Headline)
    TXT_file.close()

import requests
import os 
from bs4 import BeautifulSoup

def crawler(url,folder):
    response = requests.get(url).text
    soup = BeautifulSoup(response,'html.parser')
    imgs = soup.find_all('img')

    if not os.path.isdir(folder):
        os.mkdir(folder)
    os.chdir(folder)

    for num,img in enumerate(imgs):
        if num == 10:
            break

        else:
            link = img['src']

            try:
                name = img['alt']+'.jpg'
            except Exception as E:
                name = link.split('/')[-1]
            finally:
                name = name.replace(' ',"").replace('|','').replace('/','')
                if len(name)>255:
                    name = name[:255]+'.jpg'

            if link.startswith('http') == True:
                with open(name,'wb') as pic:
                    pic_response = requests.get(link).content
                    pic.write(pic_response)

if __name__ == "__main__":
    crawler('https://w11.read-onepiece.com/manga/one-piece-chapter-146/','One Piece')
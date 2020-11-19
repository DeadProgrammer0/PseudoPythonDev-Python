import os
import requests
import time
import concurrent.futures

urls = ["https://images.unsplash.com/photo-1536890992765-f42a1ee1e2a8",
        "https://images.unsplash.com/photo-1531398745307-6ad63a8b5284",
        "https://images.unsplash.com/photo-1589973033042-acd254cb2283",
        "https://images.unsplash.com/photo-1580920459139-68dcb30f70fe",
        "https://images.unsplash.com/photo-1596743343697-bd2c1e5a8c81"]

if not os.path.isdir('Download'):
    os.mkdir('Download')
    os.chdir('Download')

start = time.perf_counter()

def downloader(link):
    # for link in links:
    img_bytes = requests.get(link).content
    img_name = link.split('/')[3]
    img_name = f'{img_name}.jpg'
    
    with open(fr'{img_name}','wb') as img_file:
        img_file.write(img_bytes)
        print(f'Downloaded {img_name}.')
# downloader(urls)

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(downloader,urls)

end = time.perf_counter()

print(f'Finished in {round(end-start,2)} Seconds.')



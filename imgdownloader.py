import threading
import requests
import httpx
import os

counter = -1

print('loading urls')

with open('urls.txt', 'r') as _:
    global img_list
    img_list = _.read().splitlines()
os.chdir(os.path.join(os.getcwd(), 'image'))

def start():
    global counter
    counter += 1
    image = img_list[counter]
    try:
        bruh = httpx.get(f'https://{str(image)}?', proxies=f'http://127.0.0.1:24000')
        with open(f"{counter}.jpg", "wb") as image:
            image.write(bruh.content)
        print(f'[+] DOWNLOADED IMAGE #{counter}', end='\r')
    except Exception as e:
        print(e)
        





print('starting')
for _ in img_list:
    t = threading.Thread(target=start)
    t.start()
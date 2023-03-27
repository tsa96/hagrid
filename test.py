from duckduckgo_search import ddg_images
import random
import requests
import shutil

images = ddg_images('hagrid', region='uk-en', safesearch='On', max_results=5)
urls = []
for image in images:
    url = image['image']
    name:str = url.split('/')[-1]
    urls.append(url)
print(urls)

url = random.choice(urls)
name = url.split('/')[-1]
print(url)
print(name)
r = requests.get(url, stream=True)
if r.status_code == 200:
	with open('./hagrids/' + name, 'wb') as f:
		shutil.copyfileobj(r.raw, f)
del r

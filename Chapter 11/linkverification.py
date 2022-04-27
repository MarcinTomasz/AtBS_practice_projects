#! python
#Program that downloads every linked page from given website.

import os, requests, bs4

#Ask for webpage url.
url = input('URL of website that should be downloaded: ')
os.makedirs('url', exist_ok=True)

#Download website
print('Downloading links to folder: URL')
page = requests.get(url)
page.raise_for_status

soup = bs4.BeautifulSoup(page.text, features = 'html.parser')

#Find URL of links
links = soup.select('a')

final_url = []

for link in links:
    url_end = link['href']
    final_url += url + url_end

print(final_url)

#Download page.
    
#Save the links to ./pages.
#linkpage = open(os.path.join('url', os.path.basename(final_url)), 'wb')
#for chunk in res.iter_content(1000000):
#    linkpage
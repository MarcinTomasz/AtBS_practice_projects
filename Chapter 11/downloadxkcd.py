#! python3
#download Xkcd.py - downloads every single xkcd comic on website

import requests, os, bs4

url = 'http://xkcd.com'                 #starting url
os.makedirs('xkcd', exist_ok=True)      #store comics in ./xkcd, folder exist_ok=True prevents exception if folder already exists

while not url.endswith('#'):
  #Download the page.
  print('Downloading page %s...' % url)
  res = requests.get(url)
  res.raise_for_status()                #Throws an exception and ends the program if something goes wrong with the download.
  
  #Creates BeautifulSoup text object from the res variable.
  soup = bs4.BeautifulSoup(res.text)    
  
  #Find the URL of the comic image.
  comicElem = soup.select('#comic img')
  if comicElem == []:
    print('Could not find comic image.')
  else:
    try:                               #Needed because some url are missing domain name.
        comicUrl = 'https:' + comicElem[0].get('src')
            
        #Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
    
        #Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    
    except:
        comicUrl = 'https://xkcd.com' + comicElem[0].get('src')
            
        #Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
    
        #Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
  
  #Get the Prev button's url.
  prevLink = soup.select('a[rel="prev"]')[0]
  url = 'http://xkcd.com' + prevLink.get('href')
    
print('Done')

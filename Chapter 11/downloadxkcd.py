#! python3

#Script to download all XKCD comics
import os, requests, bs4

number = input('How many comics do you want to download: ' )

url = 'https://xkcd.com/' + number
os.makedirs('xkcd', exist_ok = True)

os.getcwd()

while not url.endswith('#'):
    #Download the comic.
    print('Downloading page %s...' %url)
    res = requests.get(url)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text, features = 'html.parser')
    
    #Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
            
    #Download image.
    print('Downloading image %s...' % (comicUrl))
    res =requests.get(comicUrl)
    res.raise_for_status()
    
    #Save the image to ./xkcd.
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    #Get the Previous button's url.
    prevLink = soup.select('a[rel = "prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
                                    
print('All files downloaded.')             
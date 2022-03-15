#! python3

#Program to download images from photo hosting website with certain tag

import os, requests, bs4

searchterm = input('Enter search term(s): ')

def image_downloader(extension):
    """Search and download all images from Imgur."""
    url = 'https://imgur.com/search?q=' + searchterm
    os.makedirs('/Users/novyp/Desktop/pics', exist_ok=True)
    
    res = requests.get(url)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text, features= 'html.parser')   
    image_elem = soup.select('.post > .image-list-link img') #select method is used to find matching elements using 
                                                             #CSS selector - all image-list-link imgs one level in all post classes
    
    for i, image in enumerate(image_elem):
        #Convert image URL from thumbnail size to fullsize version.
        image_url_s = 'https:' + image_elem[i].get('src')
        image_url = image_url_s[:-5] + '.jpeg'
        
        print('Downloading image {}'.format(image_url))
        res = requests.get(image_url)
        res.raise_for_status()
        image_file = open(os.path.join(r'/Users/novyp/Desktop/pics', os.path.basename(image_url)), 'wb')
        
        for chunk in res.iter_content(1000000):
            image_file.write(chunk)
        image_file.close()
    
    return len(image_elem)

downloaded = image_downloader('jpg')

if downloaded == 0:
    print('No images found.')
else:
    print('All ' + str(downloaded) + ' files successfully downloaded.')

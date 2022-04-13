#! python3

# #lucky.py - opens several google search results.

import requests, sys, webbrowser, bs4

print('Ducking...') # display text while loading the google page
res = requests.get('https://duckduckgo.com/?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()

#Retrieve top search result links. 
soup = bs4.BeautifulSoup(res.text, features='lxml')

#Open a browswer tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
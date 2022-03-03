#Script to open web browser with Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

#Open Chrome
PATH = "C:\\Users\\novyp\\Desktop\\Python\\Webdrivers\\chromedriver.exe"
browser = webdriver.Chrome(PATH)
browser.get('http://inventwithpython.com')

#Open Firefox
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(options=options)
driver.get('http://inventwithpython.com')

#Code to find CSS elements.
try:
    elem = driver.find_elements(By.CLASS_NAME, 'col-sm-12')
    print('Found elements with that class name!')
    for e in elem[:2]: #prints first 2 items (index [0] and [1])
        print(e.text)
except:
    print('Was not able to find an element with that name.')

#Code to find a link and click it. 
linkElem = driver.find_element(by=By.LINK_TEXT, value='Subreddit')
type(linkElem)
linkElem.click() #follows the "Subreddit" link

#Code to enter text in webpage
typeElem = driver.find_element(by=By.ID, value= 'mce-EMAIL')
typeElem.send_keys('marcintm001@gmail.com')

#Code to move page up/down
htmlElem = driver.find_element(by=By.TAG_NAME, value= 'html')
htmlElem.send_keys(Keys.END)
htmlElem.send_keys(Keys.HOME)

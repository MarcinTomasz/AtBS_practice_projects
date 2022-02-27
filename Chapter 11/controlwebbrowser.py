#Script to open web browser with Selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

''' #Open Chrome
PATH = "C:\\Users\\novyp\\Desktop\\Python\\Webdrivers\\chromedriver.exe"
browser = webdriver.Chrome(PATH)
browser.get('http://inventwithpython.com') '''

#Open Firefox
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(options=options)
driver.get('http://inventwithpython.com/')

#First script trying Selenium.
from selenium import webdriver

PATH = "C:\\Users\\novyp\\Desktop\\Python\\chromedriver.exe"

browser = webdriver.Chrome(PATH)

browser.get('http://inventwithpython.com')

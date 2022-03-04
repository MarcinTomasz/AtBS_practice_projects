#! python3

#Script to write and send emails from the command line.
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

''' recipient = sys.argv[1]
subject = sys.argv[2]
message = sys.argv[3] '''

#print("This is the name of the program:", sys.argv[0])
#print("Argument List:", str(sys.argv))

#Open browser
PATH = "C:\\Users\\novyp\\Desktop\\Python\\Webdrivers\\chromedriver.exe"
browser = webdriver.Chrome(PATH)
browser.get("https://protonmail.com/")
time.sleep(1)

#Open e-mail
clicklogin = browser.find_element(by= By.LINK_TEXT, value= 'LOG IN')
clicklogin.click()
time.sleep(5) #Need this method to make sure page loads before next command is input.

#Enter e-mail
typeadress = browser.find_element(by= By.ID, value= 'username')
typeadress.send_keys('mtmalek@protonmail.com')

#Enter password and sign in to client
typepassword = browser.find_element(by= By.ID, value= 'password')
typepassword.send_keys('&7K#Aib=,Q&7X-a')
typepassword.send_keys(Keys.ENTER)
time.sleep(10)

#Open and write new e-mail
checking = browser.find_element(by= By.TAG_NAME, value= 'html')
checking.send_keys('n')
checkingemail = browser.find_element(by= By.LINK_TEXT, value='Email address')
checkingemail.send_keys('mtm')
#checking.send_keys(Keys.PAGE_DOWN)
#checking.send_keys(Keys.PAGE_DOWN)
#browser.quit()

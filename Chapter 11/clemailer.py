#! python3

#Script to write and send emails from the command line.
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Remove docstrings when opening script from command line.
''' recipient = sys.argv[1]
subject = sys.argv[2]
message = sys.argv[3] '''

#Open browser
PATH = "C:\\Users\\novyp\\Desktop\\Python\\Webdrivers\\chromedriver.exe"
browser = webdriver.Chrome(PATH)
browser.get("https://protonmail.com/")
time.sleep(1)

#Open e-mail
clicklogin = browser.find_element(by= By.LINK_TEXT, value= 'LOG IN')
clicklogin.click()
time.sleep(5) #Need this method to make sure page loads before next command is input.

#Enter e-mail address
typeadress = browser.find_element(by= By.ID, value= 'username')
typeadress.send_keys('email123@protonmail.com')

#Enter password and sign in to service
typepassword = browser.find_element(by= By.ID, value= 'password')
typepassword.send_keys('password123')
typepassword.send_keys(Keys.ENTER)
time.sleep(10)

#Open and write new e-mail
newemail= browser.find_element(by= By.TAG_NAME, value= 'html')
newemail.send_keys('n')
time.sleep(1)

#Add Recipient
inputrecipient = browser.find_element(by= By.XPATH, value= "//input[@placeholder= 'Email address']")
inputrecipient.send_keys('marcintm001@gmail.com')

#Add Subject
inputsubject = browser.find_element(by= By.XPATH, value= "//input[@placeholder= 'Subject']")
inputsubject.send_keys('subject')

#Enter email message
inputsubject = browser.find_element(by= By.XPATH, value= "//input[@placeholder= 'Subject']")
inputsubject.send_keys(Keys.TAB + message)

#Send email
sendemail = browser.find_element(by= By.XPATH, value= "//button[@class= 'button button-group-item button-ghost-weak composer-send-button']")
sendemail.click() #This section runs from IDE but not from the command line, can't figure out why...

#Close browser
browser.close()
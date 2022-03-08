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

#Enter e-mail address
typeadress = browser.find_element(by= By.ID, value= 'username')
typeadress.send_keys('recipient')

#Enter password and sign in to client
typepassword = browser.find_element(by= By.ID, value= 'password')
typepassword.send_keys('&7K#Aib=,Q&7X-a')
typepassword.send_keys(Keys.ENTER)
time.sleep(10)

#Open and write new e-mail
newemail= browser.find_element(by= By.TAG_NAME, value= 'html')
newemail.send_keys('n')
time.sleep(1)

#Recipient
inputrecipient = browser.find_element(by= By.XPATH, value= "//input[@placeholder= 'Email address']")
inputrecipient.send_keys('marcintm001@gmail.com')

#Subject
inputsubject = browser.find_element(by= By.XPATH, value= "//input[@placeholder= 'Subject']")
inputsubject.send_keys('subject')

#Text
inputsubject = browser.find_element(by= By.XPATH, value= "//input[@placeholder= 'Subject']")
inputsubject.send_keys(Keys.TAB + 'message1')

#Send email
sendemail = browser.find_element(by= By.XPATH, value= "//span[@class= 'pl1 pr1 no-mobile']")
#sendemail = browser.find_element(by= By.LINK_TEXT, value= "Send")
#sendemail.send_keys(Keys.CONTROL + Keys.ENTER)
sendemail.click()

#Close 
browser.quit()

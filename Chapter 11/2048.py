#Program that opens 2048 game from https://github.com/gabrielecirulli/2048 and automatically plays the game.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Arguments needed to suppress some certificate errors from appearing.
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

#Open 2048 Github page.
PATH = "C:\\Users\\novyp\\Desktop\\Python\\Webdrivers\\chromedriver.exe"
browser = webdriver.Chrome(PATH)
browser.get("https://github.com/gabrielecirulli/2048")
time.sleep(1)

#Click 2048 game link
clickgame = browser.find_element(by= By.LINK_TEXT, value= 'Play it here!')
clickgame.click()
time.sleep(1)

#Click cookies.
clickcookies = WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="ez-accept-all"]'))).click()

#Play game with arrows.
playgame = browser.find_element(by= By.TAG_NAME, value= 'html')
while True:
    # try: This line not needed.
        playgame.send_keys(Keys.ARROW_UP)
        playgame.send_keys(Keys.ARROW_DOWN)
        playgame.send_keys(Keys.ARROW_LEFT)
        playgame.send_keys(Keys.ARROW_RIGHT)
    #Still need to fix this part so window closes when game is over.
    # except:
    #     soup = bs4.BeautifulSoup(res.text, features= 'html.parser')
    #     endofgame = soup.select('#game-message game-over > #retry-button')
    #     endofgame.click()
        
time.sleep(5)

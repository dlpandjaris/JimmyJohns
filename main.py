from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import pyperclip

path = 'C:\\...\\chromedriver.exe'
driver = webdriver.Chrome(executable_path = path)
driver.maximize_window()

driver.get("https://www.jimmyjohns.com/")

page = driver.find_element_by_css_selector("#aspnetForm > div.wrapper > header > div > div.blackbar-content.desktop-only > div.login.header-link-container > a")
page.click()

page = driver.find_element_by_css_selector("#email")
page.click()
page.send_keys("###########@email.com")

page = driver.find_element_by_css_selector("#password")
page.send_keys("############")
page.send_keys(Keys.ENTER)

time.sleep(5)
pyautogui.moveTo(555, 445)
pyautogui.click()

time.sleep(4)
pyautogui.moveTo(345, 465)
pyautogui.click()

pyautogui.scroll(-300)

pyautogui.moveTo(350, 550)
pyautogui.click()

time.sleep(1)
name = driver.find_element_by_css_selector("#recipientName")
name.send_keys("##### #")

#pyautogui.moveTo(234, 574)
#pyautogui.click()

pyautogui.scroll(-400)

pyautogui.moveTo(425, 445)
pyautogui.click()

pyautogui.moveTo(238, 517)
pyautogui.click()

pyautogui.moveTo(238, 554)
pyautogui.click()

pyautogui.scroll(-500)

pyautogui.moveTo(478, 205)
pyautogui.click()

pyautogui.moveTo(385, 465)
pyautogui.click()

pyautogui.moveTo(480, 245)
pyautogui.click()

pyautogui.moveTo(360, 315)
pyautogui.click()

pyautogui.moveTo(350, 410)
pyautogui.click()

time.sleep(2)
pyautogui.scroll(-800)

pyautogui.moveTo(470, 205)
pyautogui.click()

pyautogui.moveTo(370, 580)
pyautogui.click()

#checkout = driver.find_element_by_css_selector("#ember1652")
#checkout.click()

time.sleep(3)
pyautogui.scroll(-300)

#checkout = driver.find_element_by_css_selector("#ember1762 > span")
#checkout.click()

pyautogui.moveTo(470, 670)
pyautogui.click()

#pyautogui.moveTo(180, 240)
#pyautogui.dragTo(550, 510)
#pyperclip.copy()
#pyperclip.paste()

pyautogui.scroll(-500)

pyautogui.moveTo(580, 490)
pyautogui.click()
print(1)
time.sleep(1)
pyautogui.scroll(-500)
pyautogui.moveTo(685, 380)
pyautogui.click()
print(1)
pyautogui.click(690, 420)
print(1)
pyautogui.click(600, 670)
#pyautogui.click(467, 567)
print(1)
pyautogui.scroll(-1000)

print(1)

pyautogui.click(578, 492)
pyautogui.click(680, 420)

pyautogui.click(233, 551)
pyautogui.click(368, 584)

pyautogui.scroll(-2000)
pyautogui.click(687, 376)

pyautogui.click(467, 667)
pyautogui.click(463, 568)
pyautogui.scroll(-2000)

for i in range(5):
    pyautogui.click(463, 668)
    pyautogui.click(471, 564)
pyautogui.scroll(-2000)

time.sleep(6)

card_number = driver.find_element_by_css_selector("#creditCardNumber")
card_number.send_keys("################")

expiration_month = driver.find_element_by_css_selector("#expirationMonth")
expiration_month.send_keys("##")

expiration_year = driver.find_element_by_css_selector("#expirationYear")
expiration_year.send_keys("####")

cvv = driver.find_element_by_css_selector("#cvv")
cvv.send_keys("###")

zipcode = driver.find_element_by_css_selector("#zipCode")
zipcode.send_keys("#####")
                                              

'''
time.sleep(20)
#driver.close()
#page = driver.find_element_by_css_selector("#ember627 > span")
#time.sleep(20)
#page.click()
#time.sleep(120)
#driver.close()
'''

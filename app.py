import selenium
import time
from info import CCGA_USER, CCGA_PASS, PATH
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

s = Service(
    '{}'.format(PATH))
driver = webdriver.Chrome(service=s)

driver.get('https://www.ccga.edu/')

# accessing myCCGA portal
myCCGA = driver.find_element(By.PARTIAL_LINK_TEXT, 'MY.CCGA')
myCCGA.click()

parentWindow = driver.current_window_handle
childWindow = driver.window_handles

# switching window to CCGA Portal
for win in childWindow:
    if win != parentWindow:
        driver.switch_to.window(win)

# locating username and password inputs
usernameBox = driver.find_element(By.NAME, 'UserName')
passwordBox = driver.find_element(By.NAME, 'Password')
# Inserting Login Information
usernameBox.send_keys(CCGA_USER)
passwordBox.send_keys(CCGA_PASS)
# Clicking Login Button
loginBtn = driver.find_element(By.ID, 'submitButton')
loginBtn.click()

time.sleep(3)
# finding D2L and Outlook
d2l = driver.find_element(By.ID, '33')
email = driver.find_element(By.ID, '16')

# opening D2L and Outlook
d2l.click()
email.click()

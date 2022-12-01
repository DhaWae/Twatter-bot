from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=C:/twatterbot")
chrome_options.add_argument("--start-maximized")
driver = uc.Chrome(use_subprocess=True, options=chrome_options)
link = "https://twatter-kibbewater.vercel.app/home"
driver.get(link)
sleep(3)
trolling = True
number = 1
name = "user_not_found"
password = "hjikloE2"
loginArea = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[1]/input[1]")
passwordArea = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[1]/input[2]")
enterLogin = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/button[1]")
loginArea.click()
sleep(1)
loginArea.send_keys(name)
sleep(1)
passwordArea.click()
sleep(1)
passwordArea.send_keys(password)
sleep(1)
enterLogin.click()
sleep(7)
messageBox = driver.find_element(by=By.XPATH, value="/html/body/div[2]/main/div/div/div[1]/div[2]/textarea")
twatButton = driver.find_element(by=By.XPATH, value="/html/body/div[2]/main/div/div/div[1]/div[2]/div[3]/div[2]/button")
while trolling:
  messageBox.click()
  sleep(0.5)
  messageBox.send_keys("Add bot protection " + str(number))
  sleep(0.5)
  twatButton.click()
  number += 1
  sleep(60)
  


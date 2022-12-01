from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import os


def spam_twatter(driver, text: str):
    message_box = driver.find_element(by=By.XPATH, value="/html/body/div[2]/main/div/div/div[1]/div[2]/textarea")
    twat_button = driver.find_element(by=By.XPATH, value="/html/body/div[2]/main/div/div/div[1]/div[2]/div[3]/div[2]/button")
    while True:
        message_box.click()
        sleep(0.5)
        message_box.send_keys(text)
        sleep(0.5)
        twat_button.click()
        sleep(2)


def login_to_twatter(driver, login_credential: list):
    login_area = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[1]/input[1]")
    password_area = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[1]/input[2]")
    enter_login = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/button[1]")

    login_area.click()
    sleep(1)
    login_area.send_keys(login_credential[0])
    sleep(1)
    password_area.click()
    sleep(1)
    password_area.send_keys(login_credential[1])
    sleep(1)
    enter_login.click()
    sleep(7)


def get_login_credential():
    login_credential = []
    with open(os.getcwd() + "/credential.txt", "r") as f:
        login_credential.append(f.readline())
        login_credential.append(f.readline())
    return login_credential


def run(spam_message: str):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = uc.Chrome(use_subprocess=True, options=chrome_options)
    link = "https://twatter-kibbewater.vercel.app/home"
    driver.get(link)
    sleep(3)

    login_credential = get_login_credential()
    login_to_twatter(driver, login_credential)
    spam_twatter(driver, spam_message)

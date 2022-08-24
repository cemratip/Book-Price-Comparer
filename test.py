import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

def exists(xpath):
    try:
        driver.find_element(By.XPATH, value=xpath).click()
    except:
        return False
    return True

def getZapperPrice(ISBN):
    print('zapper ', ISBN)
    global driver
    try:
        sellURL = "https://www.zapper.co.uk/"
        driver = webdriver.Chrome(executable_path="/Users/MrCem/Desktop/app/chromedriver")
        driver.get(sellURL)
        time.sleep(4)
        print('HERE1')
        searchBox = driver.find_element(By.XPATH, value="""//*[@id="form-field-name"]""")
        searchBox.send_keys(ISBN)
        time.sleep(4)
        print('HERE2')
        addBtn = driver.find_element(By.XPATH, value="""/html/body/div[2]/div/div/section[1]/div[3]/div/div[1]/div/div/div[4]/div/div/div[2]/div/form/div/div[2]/button""")
        addBtn.click()
        time.sleep(4)
        print('HERE3')
        if exists("""//*[@id="zapper-list-accordion"]/div/div[1]/div[2]/div/div/div/section/div/div/div[2]/div/div/section[1]/div[2]/div[4]/p"""):
            print('HERE4')
            time.sleep(4)
            priceLabel = driver.find_element(By.XPATH, value="""//*[@id="zapper-list-accordion"]/div/div[1]/div[2]/div/div/div/section/div/div/div[2]/div/div/section[1]/div[2]/div[4]/p""")
            print('HERE5')
            price = priceLabel.get_attribute('innerText')
            print('HERE6')
            price = price.replace("£", "")
            print('HERE7')
            driver.quit()
            print(price)
            return price
    except:
        driver.quit()
        print('trying again...')
        getZapperPrice(ISBN)

getZapperPrice('9781107546738')

import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

bookDetails = [] # [[ISBN][Title][URL][Exchange][Price]]
driverPath = "/Users/MrCem/Downloads/chromedriver"

# scrape ISBN numbers from email
f = open("/Users/MrCem/Desktop/ISBNs.txt", "r")
allPageLines = f.readlines()
for line in allPageLines:
    if ("\cf2" in line) & ("\cell" in line) & ("EAN" not in line) & ("row" not in line):
        line = line.replace("cf2", "")
        for char in line:
            if char.isdigit() == False:
                line = line.replace(char, "")
        bookDetails.append([line])
f.close()



# fetch the name of the book
def getBookTitle(ISBN, index):
    URL = f"https://www.bookfinder.com/search/?isbn={ISBN}&mode=isbn&st=sr&ac=qr"
    page = requests.get(URL)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        for element in soup.find_all(id='describe-isbn-title'):
            bookDetails[index].append(element.text)
            bookDetails[index].append(URL)
    else:
        getBookTitle(ISBN, index)


def exists(xpath):
    try:
        driver.find_element(By.XPATH, value=xpath).click()
    except:
        return False
    return True


# fetch the price from Music Magpie
def getMusicMagpiePrice(ISBN, index):
    print('musicmagpie ', ISBN)
    global driver
    try:
        sellURL = "https://www.musicmagpie.co.uk/sell-books/"
        driver = webdriver.Chrome(executable_path=driverPath)
        driver.get(sellURL)
        time.sleep(4)
        searchBox = driver.find_element(By.XPATH, value="""//*[@id="pills-media"]/div/div/div/div/div/div/div/div[2]/div/form/div/div[1]/div[1]/input""")
        searchBox.send_keys(ISBN)
        time.sleep(4)
        addBtn = driver.find_element(By.XPATH, value="""//*[@id="pills-media"]/div/div/div/div/div/div/div/div[2]/div/form/div/div[1]/div[2]/input""")
        addBtn.click()
        time.sleep(4)
        if exists("""//*[@id="pills-media"]/div/div/div/div/div/div/div/div[2]/div/form/div/div[2]/a"""):
            time.sleep(4)
            priceLabel = driver.find_element(By.XPATH, value="""/html/body/div[3]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[1]/div[2]/div/div[3]""")
            price = priceLabel.get_attribute('innerText')
            price = price.replace("£", "")
            driver.quit()
            return price
        else:
            driver.quit()
            return 0
    except:
        driver.quit()
        print('trying again...')
        getMusicMagpiePrice(ISBN, index)


# fetch the price from We Buy Any Books
def getWeBuyBooksPrice(ISBN, index):
    print('webuybooks ', ISBN)
    global driver
    try:
        sellURL = "https://www.webuybooks.co.uk/"
        driver = webdriver.Chrome(executable_path=driverPath)
        driver.get(sellURL)
        time.sleep(4)
        searchBox = driver.find_element(By.XPATH, value="""//*[@id="isbn"]""")
        searchBox.send_keys(ISBN)
        time.sleep(4)
        addBtn = driver.find_element(By.XPATH, value="""//*[@id="main-isbn-form"]/div[1]/button""")
        addBtn.click()
        time.sleep(4)
        if exists("""//*[@id="basketTable"]/tbody/tr/td[4]"""):
            time.sleep(4)
            priceLabel = driver.find_element(By.XPATH, value="""//*[@id="basketTable"]/tbody/tr/td[4]""")
            price = priceLabel.get_attribute('innerText')
            price = price.replace("£", "")
            driver.quit()
            return price
        else:
            driver.quit()
            return 0
    except:
        driver.quit()
        print('trying again...')
        getWeBuyBooksPrice(ISBN, index)


# fetch the price from Ziffit
def getZiffitPrice(ISBN, index):
    print('ziffit ', ISBN)
    global driver
    try:
        sellURL = "https://www.ziffit.com/en-gb/"
        driver = webdriver.Chrome(executable_path=driverPath)
        driver.get(sellURL)
        time.sleep(4)
        acceptCookies = driver.find_element(By.XPATH, value="""//*[@id="onetrust-accept-btn-handler"]""")
        acceptCookies.click()
        time.sleep(4)
        searchBox = driver.find_element(By.XPATH, value="""//*[@id="barcode"]""")
        searchBox.send_keys(ISBN)
        time.sleep(4)
        addBtn = driver.find_element(By.XPATH, value="""//*[@id="scan-button"]""")
        addBtn.click()
        time.sleep(4)
        if exists("""//*[@id="items-table"]/tbody/tr/th[4]"""):
            time.sleep(4)
            priceLabel = driver.find_element(By.XPATH, value="""//*[@id="items-table"]/tbody/tr/th[4]""")
            price = priceLabel.get_attribute('innerText')
            price = price.replace("£", "")
            driver.quit()
            return price
        else:
            driver.quit()
            return 0
    except:
        driver.quit()
        print('trying again...')
        getZiffitPrice(ISBN, index)


# fetch the price from Sell It Back
def getSellItbackPrice(ISBN, index):
    print('sellitback ', ISBN)
    global driver
    try:
        sellURL = "https://sellitback.com/"
        driver = webdriver.Chrome(executable_path=driverPath)
        driver.get(sellURL)
        time.sleep(4)
        searchBox = driver.find_element(By.XPATH, value="""//*[@id="root"]/div/div[1]/div[2]/div/input""")
        searchBox.send_keys(ISBN)
        time.sleep(4)
        addBtn = driver.find_element(By.XPATH, value="""//*[@id="root"]/div/div[1]/div[2]/div/div/button""")
        addBtn.click()
        time.sleep(4)
        if exists("""//*[@id="root"]/div/div[1]/div/div/div/div[3]/div/div[2]/span"""):
            time.sleep(4)
            priceLabel = driver.find_element(By.XPATH, value="""//*[@id="root"]/div/div[1]/div/div/div/div[3]/div/div[2]/span""")
            price = priceLabel.get_attribute('innerText')
            price = price.replace("£", "")
            driver.quit()
            return price
        else:
            driver.quit()
            return 0
    except:
        driver.quit()
        print('trying again...')
        getSellItbackPrice(ISBN, index)


# fetch the price from Zapper
def getZapperPrice(ISBN, index):
    print('zapper ', ISBN)
    global driver
    try:
        sellURL = "https://www.zapper.co.uk/"
        driver = webdriver.Chrome(executable_path=driverPath)
        driver.get(sellURL)
        time.sleep(4)
        searchBox = driver.find_element(By.XPATH, value="""//*[@id="form-field-name"]""")
        searchBox.send_keys(ISBN)
        time.sleep(4)
        addBtn = driver.find_element(By.XPATH, value="""/html/body/div[2]/div/div/section[1]/div[3]/div/div[1]/div/div/div[4]/div/div/div[2]/div/form/div/div[2]/button""")
        addBtn.click()
        time.sleep(4)
        if exists("""//*[@id="zapper-list-accordion"]/div/div[1]/div[2]/div/div/div/section/div/div/div[2]/div/div/section[1]/div[2]/div[4]/p"""):
            time.sleep(4)
            priceLabel = driver.find_element(By.XPATH, value="""//*[@id="zapper-list-accordion"]/div/div[1]/div[2]/div/div/div/section/div/div/div[2]/div/div/section[1]/div[2]/div[4]/p""")
            price = priceLabel.get_attribute('innerText')
            price = price.replace("£", "")
            driver.quit()
            return price
        else:
            driver.quit()
            return 0
    except:
        driver.quit()
        print('trying again...')
        getZapperPrice(ISBN, index)


count = 0
totalNum = len(bookDetails)
for ISBN in bookDetails:
    prices = []
    getBookTitle(ISBN[0], count)

    done = False
    while done == False:
        try:
            musicMagpiePrice = float(getMusicMagpiePrice(ISBN[0], count))
            prices.append(musicMagpiePrice)
            done = True
        except:
            done = False

    done = False
    while done == False:
        try:
            weBuyBooksPrice = float(getWeBuyBooksPrice(ISBN[0], count))
            prices.append(weBuyBooksPrice)
            done = True
        except:
            done = False

    done = False
    while done == False:
        try:
           ziffitPrice = float(getZiffitPrice(ISBN[0], count))
           prices.append(ziffitPrice)
           done = True
        except:
            done = False

    done = False
    while done == False:
        try:
           sellItBackPrice = float(getSellItbackPrice(ISBN[0], count))
           prices.append(sellItBackPrice)
           done = True
        except:
            done = False

    print(prices)
    prices.sort()
    bestPrice = prices[-1]
    if bestPrice != 0:
        if bestPrice == weBuyBooksPrice:
            ISBN.append("We Buy Books")
        elif bestPrice == ziffitPrice:
            ISBN.append("Ziffit")
        #elif bestPrice == zapperPrice:
        #    ISBN.append("Zapper")
        elif bestPrice == sellItBackPrice:
            ISBN.append("Sell It Back")
        else:
            ISBN.append("Music Magpie")
    ISBN.append(bestPrice)
    count += 1
    print(f"book: {count}/{totalNum}")


totalSalePrice = 0
for book in bookDetails:
    totalSalePrice += book[4]
print("Best sale price:", totalSalePrice)


webuybooks = []
ziffit = []
#zapper = []
sellitback = []
musicmagpie = []
for book in bookDetails:
    exchange = book[3]
    if exchange == "We Buy Books":
        webuybooks.append(book[1])
    elif exchange == "Ziffit":
        ziffit.append(book[1])
    #elif exchange == "Zapper":
    #    zapper.append(book[1])
    elif exchange == "Sell It Back":
        sellitback.append(book[1])
    else:
        musicmagpie.append(book[1])

print("\nSell the following books to We Buy Books:")
[print(book) for book in webuybooks]
print("\nSell the following books to Ziffit:")
[print(book) for book in ziffit]
#print("\nSell the following books to Zapper:")
#[print(book) for book in zapper]
print("\nSell the following books to Sell It Back:")
[print(book) for book in sellitback]
print("\nSell the following books to Music Magpie:")
[print(book) for book in musicmagpie]

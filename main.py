import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from telegram_bot import TelegramBot
from mongodb import MongoDB
from datetime import date
chrome_driver = webdriver.Chrome()

bot = TelegramBot()
db = MongoDB()
today = date.today()
now = today.strftime('La fecha de hoy %d,%m,%Y \n')
URL="https://www.mercadolibre.com.ec/"

chrome_driver.get(URL)
#chrome_driver.get("https://www.wikipedia.org/")
print("----",chrome_driver.title,"-----")

topics = [
   # "carro",
  #  "moto",
    "play station 5"
]

for t in topics:
    search_box = chrome_driver.find_element(By.CLASS_NAME, "nav-search-input")
    #search_box = chrome_driver.find_element(By.ID, "searchInput")
    search_box.send_keys(t)
    search_button = chrome_driver.find_element(By.CLASS_NAME, "nav-search-btn")
    #search_button = chrome_driver.find_element(By.CSS_SELECTOR, '#search-form > fieldset > button > i')
    search_button.click()

    content = chrome_driver.find_element(By.CLASS_NAME, "ui-search-layout__item")
    #content = chrome_driver.find_element(By.ID, "mw-content-text")
    print(content.text)
    message: str = f"La busqueda de {topics}\n"
    text = content.text
    text1= message+now+text,
    text = text[:4000]
    bot.send_tg_message(text1)
    db.insert_wikipedia_text(title=t, text=text)
    time.sleep(2)
    chrome_driver.get(URL)


print("fin")
chrome_driver.close()




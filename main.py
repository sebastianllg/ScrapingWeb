from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.wikipedia.org")
print(driver.title)


search_box=driver.find_element(By.NAME, "search_input.input")
search_box.send_keys("puembo")
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
driver.close()



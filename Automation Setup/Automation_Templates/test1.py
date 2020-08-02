import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("E:\\Python Workspace\\drivers\\chromedriver.exe")
driver.implicitly_wait(5)

driver.get("https:\\www.google.com")

print(driver.title)
driver.find_element(By.NAME, 'q').send_keys("Python")

optionsList = driver.find_elements(By.CSS_SELECTOR, 'ul.erkvQe li span')

print(len(optionsList))

for element in optionsList:
    print(element.text)

time.sleep(5)
driver.quit()

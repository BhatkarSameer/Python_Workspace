import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("E:\\Python Workspace\\drivers\\chromedriver.exe")
driver.get("https:\\www.google.com")

print(driver.title)

driver.find_element(By.NAME, 'q').send_keys("Python")

optionList = driver.find_elements(By.CSS_SELECTOR, "ul.erkvQe li span")
print(len(optionList))

for element in optionList:
    print(element.text)

time.sleep(5)
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)

driver = webdriver.Chrome(chrome_option)
driver.get('http://orteil.dashnet.org/experiments/cookie/')
cookie = driver.find_element(By.XPATH, value='//*[@id="cookie"]')
for i in range(123456789):
    cookie.click()
driver.close()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\browserdrivers\\chromedriver.exe")
driver.maximize_window()
driver.get("http://localhost/OnlineJobPortal/System/")
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='login']").click()
time.sleep(2)
driver.find_element(By.NAME, 'email').clear()
driver.find_element(By.NAME, 'email').send_keys('shaikat@gmail.com')
driver.find_element(By.NAME, 'password').clear()
driver.find_element(By.NAME, 'password').send_keys('12345678')
time.sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
time.sleep(2)
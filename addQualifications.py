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
time.sleep(1)
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/header[1]/nav[1]/div[1]/div[3]/ul[1]/li[2]/a[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[3]/a[1]").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Add new']").click()
driver.find_element(By.XPATH, "//input[@placeholder='Enter institution name']").send_keys('AIUB')
driver.find_element(By.XPATH, "//input[@placeholder='Enter course name']").send_keys('SQT')
driver.find_element(By.XPATH, "//input[@placeholder='Eg: 2015 To 2016']").send_keys("2019 - 2022")
driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()
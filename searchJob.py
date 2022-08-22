import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\browserdrivers\\chromedriver.exe")
driver.maximize_window()
driver.get("http://localhost/OnlineJobPortal/System/")
time.sleep(1)
driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/header[1]/nav[1]/div[1]/div[2]/ul[1]/li[2]/a[1]").click()
time.sleep(1)
category = driver.find_element(By.NAME, "category")
categoryType = Select(category)
categoryType.select_by_index(8)
country = driver.find_element(By.NAME, "country")
countryType = Select(country)
countryType.select_by_index(18)
time.sleep(1)
driver.find_element(By.NAME, "search").click()
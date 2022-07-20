import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
path ="C:\Windows\System32\chromedriver.exe"

for i in range(100):
    driver = webdriver.Chrome(path)
    driver.maximize_window()
    driver.get("https://www.youtube.com/watch?v=t5WPfbU16AI&list=LL&index=222")
    time.sleep(10)
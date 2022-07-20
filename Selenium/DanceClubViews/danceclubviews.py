import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
path ="C:\Windows\System32\chromedriver.exe"

for i in range(1000):
    driver = webdriver.Chrome(path)
    driver.maximize_window()
    driver.get("https://www.youtube.com/")
    searchbar = driver.find_element_by_name("search_query")
    searchbar.send_keys("kos iitk")
    searchbar.send_keys(Keys.RETURN)
    time.sleep(3)
    driver.find_element_by_link_text("Y21 Freshers Dance Showcase 2022 | IIT KANPUR.").send_keys(Keys.RETURN)
    time.sleep(30)
    driver.close()
    time.sleep(2)
    print(i)
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

dirr = os.getcwd()
path = "C:\Windows\System32\chromedriver.exe"
username = input("INPUT USERNAME: ")
passw = input("PASSWORD: ")
wk = int(input("WEEK NUMBER: "))
lec = int(input("LECTURE: "))+7
str = f"https://hello.iitk.ac.in/mth102aa2122/#/lecture/{lec}"

driver = webdriver.Chrome(path)
driver.maximize_window()
driver.get("https://hello.iitk.ac.in/user/login")
driver.find_element_by_name("name").send_keys(username)
driver.find_element_by_name("pass").send_keys(passw)
driver.find_element_by_id("edit-submit").send_keys(Keys.RETURN)
time.sleep(1)
driver.find_element_by_partial_link_text("MTH102").send_keys(Keys.RETURN)
time.sleep(1)
driver.find_element_by_id("edit-access-course").send_keys(Keys.RETURN)
time.sleep(3)
weeks = driver.find_elements_by_css_selector("div[class='weekWrapper']")
weeks[2*wk-1].click()
time.sleep(3)
driver.get(str)
time.sleep(3)
driver.find_element_by_id("speedMinus").click()
time.sleep(2)
speeds = driver.find_element_by_id("currentSpeed")
driver.execute_script("arguments[0].innerText = '2x'", speeds)
time.sleep(15)
driver.close()

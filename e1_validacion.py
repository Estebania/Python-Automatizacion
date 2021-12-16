from selenium import webdriver 
import time
driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
driver.get("http://python.org")
time.sleep(3)
driver.close()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
service=Service()
driver = webdriver.Chrome(options, service)

url = "https://www.ucla.edu/"
driver.get(url)
print("Page title:", driver.title)

driver.quit()
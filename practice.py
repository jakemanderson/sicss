from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import os

def get_driver():
    options = Options()
    service = Service()
    driver = webdriver.Chrome(options=options, service=service)
    return driver

def main():
    driver = get_driver()

    # Navigate to a page where you can practice
    driver.get("https://demoqa.com/elements")

    # Wait some time (Default unit is seconds)
    time_to_wait = 5
    time.sleep(time_to_wait)

    # go to the practice text box form filler
    driver.get("https://demoqa.com/text-box")
    
    # Find form elements and fill them
    full_name = driver.find_element(By.ID, "userName")
    full_name.send_keys("John Doe")

    email = driver.find_element(By.ID, "userEmail")
    email.send_keys("john.doe@example.com")

    current_address = driver.find_element(By.ID, "currentAddress")
    current_address.send_keys("123 Main St, Los Angeles, CA 90095")

    permanent_address = driver.find_element(By.ID, "permanentAddress")
    permanent_address.send_keys("123 Main St, Los Angeles, CA 90095")

    # Submit the form
    submit_button = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)  # Scroll to the button
    time.sleep(1)  # Small delay to see the scroll
    submit_button.click()

    # Wait to see the result
    time.sleep(2)

    # Close the driver when you are done
    driver.quit()

if __name__ == "__main__":
    main()

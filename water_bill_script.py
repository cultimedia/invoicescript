from selenium import webdriver
from selenium.webdriver.common.by import By
from credentials import WATER_URL, WATER_USERNAME, WATER_PASSWORD
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# Setting up the Chrome driver
driver = webdriver.Chrome()

# Navigate to the water bill site
driver.get(WATER_URL)

# Locate the username and password fields and log in
username_field = driver.find_element(By.NAME, "Username")
password_field = driver.find_element(By.NAME, "Password")
username_field.send_keys(WATER_USERNAME)
password_field.send_keys(WATER_PASSWORD)
login_button = driver.find_element(By.ID, "btn-login")
login_button.click()

try:
    bill_status_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "bill-status"))
    )
    water_bill_amount_text = bill_status_element.text.split()[0]  # Assuming the amount is the first item in the text
    water_bill_amount = float(water_bill_amount_text.strip('$'))
    print(f"Current Water Bill Amount: {water_bill_amount}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()

# Save to a JSON file
with open('bills.json', 'r+') as file:
    bills = json.load(file)
    bills['water_bill'] = water_bill_amount
    file.seek(0)
    json.dump(bills, file)
    file.truncate()



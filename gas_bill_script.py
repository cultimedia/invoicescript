from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from credentials import GAS_URL, GAS_USERNAME, GAS_PASSWORD
import json

driver = webdriver.Chrome()
driver.get(GAS_URL)

try:
    # Wait for the username field to be clickable and then enter the username
    username_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "txtHeroUsername"))
    )
    username_field.send_keys(GAS_USERNAME)

    # Wait for the password field to be clickable and then enter the password
    password_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "txtHeroPassword"))
    )
    password_field.send_keys(GAS_PASSWORD)
    
    # Click the login button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/section[1]/div[1]/div/fieldset/form/div[1]/div[3]/button"))
    )
    login_button.click()
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(), '$')]"))
    )

    # Wait for the gas bill amount to appear and extract it
    gas_bill_amount_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "amount-due"))
    )
    gas_bill_amount = gas_bill_amount_element.text.strip().replace('$', '')
    print(f"Current Gas Bill Amount: {gas_bill_amount}")

    # Save to a JSON file
    with open('bills.json', 'r+') as file:
        bills = json.load(file)
        bills['gas_bill'] = float(gas_bill_amount)
        file.seek(0)
        json.dump(bills, file)
        file.truncate()

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the driver after operations are done
    driver.quit()


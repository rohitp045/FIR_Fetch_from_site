from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options
import time

import streamlit as st

from input import input_data
# Define the input data dictionary
# input_data = {
#     "from_date": "16/03/2024",
#     "to_date": "16/03/2024",
#     "unit": "PIMPRI-CHINCHWAD",
#     "FIRno": "0139"
# }

# Set up the Chrome WebDriver


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the webpage
print("Opening the webpage...")
driver.get("https://citizen.mahapolice.gov.in/Citizen/MH/PublishedFIRs.aspx")
driver.refresh()

# Set 'From Date'
print("Setting 'From Date'...")
from_date = driver.find_element(By.ID, "ContentPlaceHolder1_txtDateOfRegistrationFrom")
driver.execute_script("arguments[0].value = arguments[1]", from_date, input_data["from_date"])

# Set 'To Date'
print("Setting 'To Date'...")
to_date = driver.find_element(By.ID, "ContentPlaceHolder1_txtDateOfRegistrationTo")
driver.execute_script("arguments[0].value = arguments[1]", to_date, input_data["to_date"])

# Select 'Unit' from dropdown
print("Selecting 'Unit'...")
unit_select = Select(driver.find_element(By.ID, "ContentPlaceHolder1_ddlDistrict"))
unit_select.select_by_visible_text(input_data["unit"])

# Input FIR number
print("Inputting FIR number...")
fir_no_textbox = driver.find_element(By.ID, "ContentPlaceHolder1_txtFirno")
fir_no_textbox.send_keys(input_data["FIRno"])

# Click the 'View Record' button
print("Clicking 'View Record' button...")
view_record_button = driver.find_element(By.ID, "ContentPlaceHolder1_btnSearch")
view_record_button.click()

# Click the 'Download' button for the first record
try:
    print("Downloading the first record...")
    dwnld_button = driver.find_element(By.ID, "ContentPlaceHolder1_gdvDeadBody_btnDownload_0")
    dwnld_button.click()
    print("FIR Copy Downloaded Successfully!")

except :
    print("No record found or unable to download.")
time.sleep(3)
# Close the driver
print("Closing the browser...")
driver.quit()

    

    

    



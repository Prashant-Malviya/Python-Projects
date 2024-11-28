from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

# Selenium WebDriver
driver = webdriver.Chrome() 
url = "https://youtu.be/iTmlw3vQPSs"
driver.get(url)

try:
    
    wait = WebDriverWait(driver, 15)  
    description_container = wait.until(
        EC.presence_of_element_located((By.ID, "description-inline-expander"))
    )

    try:
        expand_button = description_container.find_element(By.ID, "expand")
        if expand_button.is_displayed():
            expand_button.click()
    except Exception:
        pass  

    # Extract the full description text
    description_text = description_container.text

    # Extract timestamps directly from <a> tags
    timestamp_elements = description_container.find_elements(By.CSS_SELECTOR, "a.yt-core-attributed-string__link")
    timestamps = [element.text for element in timestamp_elements if re.match(r'\b\d{1,2}:\d{2}(:\d{2})?\b', element.text)]

    # Save the results to a file
    with open("output.txt", "w") as file:
        file.write(f"url: {url}\n")
        file.write("description_text: " + description_text.strip() + "\n")
        file.write("timestamp_list: " + ", ".join(timestamps) + "\n")

    # Printing outputs for verification
    print("Description Text:", description_text.strip())
    print("Timestamps:", timestamps)
    print("Data saved successfully in output.txt")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()

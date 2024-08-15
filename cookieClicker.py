# SELENIUM proof of concept

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")


def purchase_upgrade():
    money_int = int(driver.find_element(By.ID, value='money').text)
    if money_int > 2000:
        driver.find_element(By.ID, value='buyShipment').click()
    elif money_int > 500:
        driver.find_element(By.ID, value='buyFactory').click()
    elif money_int > 100:
        driver.find_element(By.ID, value='buyGrandma').click()
    elif money_int > 15:
        driver.find_element(By.ID, value='buyCursor').click()



for i in range(12):
    start_time = time.time()
    delay = 5
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        driver.find_element(By.ID, value='cookie').click()
        if elapsed_time >= delay:
            break
    purchase_upgrade()

cps = driver.find_element(By.ID, value='cps')
print(f"Your {cps.text}.")


# time.sleep(0.01)


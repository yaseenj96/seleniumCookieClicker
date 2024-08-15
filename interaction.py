# SELENIUM proof of concept

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

num_art = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
print(num_art.text)

# Click on link
# num_art.click()

# Find element by Link Text
all_portals = driver.find_element(By.LINK_TEXT, value = "Content portals")

# Find the "Search" <input> by Name, and put in 'Python' as a search
search = driver.find_element(By.NAME, value="search")

# Sending keyboard input to Selenium
search.send_keys("Python", Keys.ENTER)

driver2 = webdriver.Chrome(options=chrome_options)
driver2.get("https://secure-retreat-92358.herokuapp.com/")
fName = driver2.find_element(By.NAME, value='fName')
lName = driver2.find_element(By.NAME, value='lName')
email = driver2.find_element(By.NAME, value='email')
fName.send_keys("Yaseen", Keys.ENTER)
lName.send_keys("Jeber", Keys.ENTER)
email.send_keys("yaseenj96@gmail.com", Keys.ENTER)

# driver.close()
# driver.quit()
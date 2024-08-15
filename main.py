# SELENIUM proof of concept

from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")
# driver.get("https://www.amazon.com/Ninestars-DZT-50-13-Automatic-Touchless-Stainless/dp/B00K2VKFSE/ref=sr_1_4?crid=1LA78ZJIUFNYO&dib=eyJ2IjoiMSJ9.hXqkMv1zHahV3Rn5KbAS5GvYPjmonqp-Fw1_oh4oqpUMkiVc6yw2VO3B_8rE9-K9V5M5k6QYLjboRkzbKsaJmNbK6T7T03DxXpWxx_alDUVIcomN8pvy5QMNVK81El2f5kik_5d3ZyerFIbOoJ_bejXAoGOPsiLvuCfKfsFdqxFcqjq2wMHv5zmD8-9p91u_JCUOY4p2oVUQcA_pXJkDVyq_2xx031ADUYkKdeBsK5H_2R5Fcwzs7HulzP9kaccNUnJqwjne-rv5MzizY00TK-nzTJocgDoWcpf8fyekUl4.vBp35hN42z162Jg75XoQbnsRVq17UBl1W9NfdO1XAFI&dib_tag=se&keywords=AUTOMATIC+TRASH+can&qid=1723750399&s=home-garden&sprefix=automatic+trash+ca%2Cgarden%2C500&sr=1-4")

## SELENIUM METHODS OF SCRAPING ELEMENTS

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# print(f"The price is {price_dollar}.{price_cents}")

search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, value="submit")
print(button.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

## X PATH
submit_bug = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(submit_bug.text)

## Get all Python upcoming events and put them into a class:
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }
print(events)



# driver.close()
driver.quit()


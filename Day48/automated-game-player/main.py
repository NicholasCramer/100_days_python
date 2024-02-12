from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

# Check store for item upgrades
store = driver.find_elements(By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in store]

timer = time.time() + 5
game_timer = time.time() + 60 * 5

while True:
    cookie.click()

    if time.time() > timer:
        all_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        item_prices = []

        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Add store items and prices to dictionary
        cookie_store = {}
        for n in range(len(item_prices)):
            cookie_store[item_prices[n]] = item_ids[n]

        # Check current wallet
        money_element = driver.find_element(By.ID, value="money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        wallet_value = int(money_element)

        # Check for affordable store items
        affordable_items = {}
        for cost, id in cookie_store.items():
            if wallet_value > cost:
                affordable_items[cost] = id

        # Purchase most expensive affordable item
        highest_cost_affordable_item = max(affordable_items)
        purchase_item_id = affordable_items[highest_cost_affordable_item]

        driver.find_element(By.ID, value=purchase_item_id).click()

        # Add another 5 seconds before loop repeats
        timer = time.time() + 5

    # Stop playing after five minutes and print current 'cookies per second count'
    if time.time() > game_timer:
        cookie_per_sec = driver.find_element(By.ID, value="cps").text
        print(cookie_per_sec)
        break

driver.quit()

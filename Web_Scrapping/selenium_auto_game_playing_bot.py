import time
from typing import Dict, List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browswer open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://orteil.dashnet.org/experiments/cookie/')

items = driver.find_elements(By.CSS_SELECTOR, value='#store div')
item_ids = [item.get_attribute('id') for item in items]

item_prices = driver.find_elements(By.CSS_SELECTOR, value='#store b')

all_prices: List[int] = []
upgrade_prices: Dict[int, str] = {}
for i, item_price in enumerate(item_prices):
    if item_price.text != '':
        print(item_price.text.split('-'))
        price: int = int(item_price.text.split('-')[1].strip().replace(',', ''))
        all_prices.append(price)
        upgrade_prices[price] = item_ids[i]

all_prices = sorted(all_prices, reverse=True)

while True:
    driver.find_element(By.ID, value='cookie').click()
    time.sleep(1)
    
    money = driver.find_element(By.ID, value='money')
    current_money: int = int(money.text.replace(',', ''))

    affordable_prices: List[int] = [price for price in all_prices if price <= current_money]
    if not affordable_prices:
        continue

    highest_price: int = max(affordable_prices)
    to_buy_id: str = upgrade_prices.get(highest_price)
    driver.find_element(By.ID, value=to_buy_id).click()

# driver.close()
# driver.quit()

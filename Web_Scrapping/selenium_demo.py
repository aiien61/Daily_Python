from selenium import webdriver
from selenium.webdriver.common.by import By
from typing import Dict

# Keep Chrome browswer open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://appbrewery.github.io/instant_pot/')

# price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole')
# price_cent = driver.find_element(By.CLASS_NAME, value='a-price-fraction')
# print(f'The price is {price_dollar.text}.{price_cent.text}')

driver.get('https://www.python.org/')

search_bar = driver.find_element(By.NAME, value='q')
print(search_bar.get_attribute('placeholder'))

button = driver.find_element(By.ID, value='submit')
print(button.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, value='.documentation-widget a')
print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

event = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]')
print(event.text.split('\n'))

# events: Dict[int, str] = {}
# for i in range(5):
#     event = driver.find_element(By.XPATH, value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i+1}]')
#     events[i] = dict(zip(['time', 'name'], event.text.split('\n')))
# print(events)

event_times = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
events: Dict[int, str] = {}
for i in range(len(event_times)):
    events[i] = {'time': event_times[i].text, 'name': event_names[i].text}
print(events)


# driver.close()
driver.quit()
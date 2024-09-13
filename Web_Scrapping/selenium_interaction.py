from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browswer open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('http://secure-retreat-92358.herokuapp.com/')



first_name = driver.find_element(By.NAME, value='fName')
last_name = driver.find_element(By.NAME, value='lName')
email = driver.find_element(By.NAME, value='email')

first_name.send_keys('Johnny')
last_name.send_keys('Mario')
email.send_keys('j.mario@email.com')

submit = driver.find_element(By.CSS_SELECTOR, value='form button')
submit.click()

# driver.close()
# driver.quit()

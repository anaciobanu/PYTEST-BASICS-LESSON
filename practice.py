from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()

driver.get('https://www.saucedemo.com/')

username=driver.find_element(By.ID,'user-name')

password=driver.find_element(By.NAME,'password')

login_button=driver.find_element(By.CLASS_NAME,'submit-button')

username.send_keys('performance_glitch_user')

password.send_keys('secret_sauce')

login_button.click()

driver.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-backpack").click()
element=driver.find_element(By.CSS_SELECTOR,".shopping_cart_badge")
print(element.text=='1')
driver.find_element(By.CSS_SELECTOR,'.shopping_cart_link').click()

price_element=driver.find_element(By.CSS_SELECTOR,'.inventory_item_price')
print(price_element.text)

checkout=driver.find_element(By.CSS_SELECTOR,'#checkout').click()

driver.find_element(By.CSS_SELECTOR,'#first-name').send_keys('Natalia')
driver.find_element(By.CSS_SELECTOR,'#last-name').send_keys('Test')
driver.find_element(By.CSS_SELECTOR,'#postal-code').send_keys('45039')
driver.find_element(By.CSS_SELECTOR,'#continue').click()
driver.find_element(By.CSS_SELECTOR,'#finish').click()
element = driver.find_element(By.CSS_SELECTOR,'.complete-header')
print(element.text =='THANK YOU FOR YOUR ORDER')
driver.close()




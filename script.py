from urllib import request
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import pytest
from time import sleep


def launch_swaglabs():
    global driver
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('https://www.saucedemo.com/')

def valid_login_swaglabs():
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By. NAME, 'password').send_keys('secret_sauce')
    driver.find_element(By.CLASS_NAME, 'submit-button ').click() 

def capture_evidence():
    image_name = fr"C:\pytest-basics-lesson\evidence\image-{datetime.today().strftime('%m%d%y-%H%M%S')}.png"
    driver.save_screenshot(image_name) 

def test_launch_login_page():
    launch_swaglabs()
    assert driver.title == 'Swag Labs'
    capture_evidence()
    driver.quit()
  

@pytest.fixture()
def setup(request):
    #the following code runs before each test
    launch_swaglabs()
    valid_login_swaglabs()

def teardown():
    capture_evidence()
    driver.quit()
    request.addfinalizer(teardown)    

@pytest.mark.reg
def test_login_valid_credentials(setup):
    assert 'products' in driver.page_source.lower()   

def test_view_product_details(setup):
    product_names = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
    product_names[0].click()
    assert 'back to products' in driver.page_source.lower()

def test_item_price(setup):
    price_element=driver.find_element(By.CSS_SELECTOR,'.inventory_item_price')
    print(price_element.text)
    assert 'products' in driver.page_source.lower()     

def test_add_item_to_cart(setup):
    driver.find_element(By. CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
    assert 'products' in driver.page_source.lower() 

def test_remove_item_from_cart(setup):
    driver.find_element(By. CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.CSS_SELECTOR, '.shopping_cart_badge').click()
    driver.find_element(By. CSS_SELECTOR, '#remove-sauce-labs-backpack').click()
    assert 'your cart' in driver.page_source.lower() 









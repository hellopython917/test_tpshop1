import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://tp.shop.com")
driver.maximize_window()

coocle = {'name': 'uname',
          'value': '%25E7%258E%258B%25E7%2584%25B6%25E5%2595%258A%25E5%2595%258A%25E5%2595%258A%25E5%2595%258A%25E5%2595%258A%25E5%2595%258A'}
coole1 = {'name': 'user_id',
          'value': '8'}
driver.add_cookie(coocle)

driver.refresh()

time.sleep(10)

driver.close()

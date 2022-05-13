import time

from seleniumwire import webdriver

driver =webdriver.Chrome()
driver.get('www.baidu.com')
time.sleep(2)

for request in driver.requests:
    print(request)
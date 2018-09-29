import numpy  as np
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from bs4 import BeautifulSoup
#%matplotlib inline

url="https://www.google.com/flights/explore/#explore;f=DUB;t=r-Europe-0x46ed8886cfadda85%253A0x72ef99e6b3fcf079;li=0;lx=2;d=2018-02-10"
driver= webdriver.PhantomJS()
dcap=dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"]=("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299")
driver= webdriver.PhantomJS.desired_capabilities=dcap,service_args=['--ignore-ss1-errors-true']
driver.implicitly_wait(20)
driver.get(url)

driver.save_screenshot(r'flight_explorer.png')

# Author:         Adam Ray Alcala
# Date Created:   January 1st, 2020
# Modified:       Continuously

# Package Imports
import os 
import time
import click
import pandas as pd
import pyinputplus as pyip

from prettytable import PrettyTable
from pathlib import Path

# Selenium Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service

service = Service(r"C:\Users\AdamAlcala\Desktop\githubMELLOWCODE\Python_Scripts\Web Scraping\selenium\chromedriver_win32\chromedriver.exe")
service.start()

driver = webdriver.Remote(service.service_url)

keyword = pyip.inputStr('Search: ')


driver.get('https://google.com/search?q='+keyword)

#elem = driver.find_element(By.CLASS_NAME, 'gLFyf')
#elem.send_keys('selenium python')
#elem.submit()

# Allows the user to see the results of the script

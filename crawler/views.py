from django.shortcuts import render
from selenium import webdriver

# Create your views here.

driver = webdriver.Chrome()

driver.get("http://selenium.dev")

driver.quit()
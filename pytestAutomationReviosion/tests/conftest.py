import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.fixture(scope='class')
def setup(request):
    service_obj = Service()
    driver = webdriver.Chrome(service=service_obj)
    driver.get('https://rahulshettyacademy.com/client')
    request.cls.driver = driver
    yield
    driver.close()
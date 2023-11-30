import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from utilities.baseClass import BaseClass
from pageObjects.forgotPwd import ForgotPwd
from pageObjects.login import Login
from testData.testDataForm import TestDataForm
import time


class TestNov(BaseClass):
    def testreg(self,getData):

        log=self.getlogger()
        fpwd = Login(self.driver)

        reg = fpwd.forgotPwd()
        log.info('useremail is '+getData['email'])
        reg.getEmail().send_keys(getData['email'])

        log.info('userpwd is '+getData['password'])
        reg.getpwd().send_keys(getData['password'])
        reg.getCnfmPwd().send_keys(getData['cnfmPwd'])
        reg.submit().click()

    @pytest.fixture(params=TestDataForm.data1)
    def getData(self,request):
        return request.param





    """
        
        # driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
        # alternative way of finding element is with text on it. In this case, button has a text on it
        driver.find_element(By.XPATH, "//button[text()='Save New Password']")

        # time.sleep(5)
        driver.get("https://rahulshettyacademy.com/client")
        driver.find_element(By.ID, "userEmail").send_keys("demo@gmail.com")
        driver.find_element(By.ID, "userPassword").send_keys("123")
        # time.sleep(5)
        driver.find_element(By.ID, "login").click()
        time.sleep(10)
        
    """





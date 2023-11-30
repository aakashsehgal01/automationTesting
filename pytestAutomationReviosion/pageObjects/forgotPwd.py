from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class ForgotPwd():
    def __init__(self, driver):
        self.driver = driver


    email = (By.CSS_SELECTOR, "input[type='email']")
    pwd = (By.ID, "userPassword")
    cnf_pwd = (By.ID, "confirmPassword")
    submit_btn=(By.CSS_SELECTOR, "button[type='submit']")

    def getEmail(self):
        return self.driver.find_element(*ForgotPwd.email)

    def getpwd(self):
        return self.driver.find_element(*ForgotPwd.pwd)

    def getCnfmPwd(self):
        return self.driver.find_element(*ForgotPwd.cnf_pwd)

    def submit(self):
        return self.driver.find_element(*ForgotPwd.submit_btn)

    #driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("demo@gmail.com")
    #driver.find_element(By.ID, "userPassword").send_keys("123")
    #driver.find_element(By.ID, "confirmPassword").send_keys("123")
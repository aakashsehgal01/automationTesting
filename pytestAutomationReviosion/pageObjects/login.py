from pageObjects.forgotPwd import ForgotPwd
from selenium.webdriver.common.by import By

class Login():


    def __init__(self, driver):
        self.driver = driver

    forgotPwdLink = (By.LINK_TEXT, "Forgot password?")
    user = (By.ID, "userEmail")
    userPwdVar= (By.ID, "userPassword")
    login_btn = (By.ID, "login")

    def forgotPwd(self):
        self.driver.find_element(*Login.forgotPwdLink).click()
        reg = ForgotPwd(self.driver)
        return reg

    def userid(self):
        return self.driver.find_element(*Login.user)

    def userPwd(self):
        return self.driver.find_element(*Login.userPwdVar)

    def userLogin(self):
        return self.driver.find_element(*Login.login_btn)






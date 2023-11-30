import pytest
from utilities.baseClass import BaseClass
from testData.testDataForm import TestDataForm
from pageObjects.login import Login


class TestLogin(BaseClass):

    def testloginpg(self,getData):
        usrLogin = Login(self.driver)
        usrLogin.userid().send_keys(getData['email'])
        usrLogin.userPwd().send_keys(getData['password'])
        usrLogin.userLogin().click()


    @pytest.fixture(params=TestDataForm.data1)
    def getData(self, request):
        return request.param

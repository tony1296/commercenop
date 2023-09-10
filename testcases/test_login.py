import pytest
from selenium import webdriver
from pageobjects.LoginPage import LoginPage
from utilities.readproperties import ReadConfig
from utilities.customlogger import LogGen

class Test_001_Login:
    baseUrl = ReadConfig.getapplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):

        self.logger.info("*****Test_001_Login*****")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.logger.info("***home page title test is verified***")
            self.driver.close()
        else:
            self.driver.save_screenshot("Screenshots\\test_homePageTitle.png")
            self.driver.close()
            self.logger.error("****home page title test failed****")
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("***Login test is passed***")
            self.driver.close()
        else:
            self.driver.get_screenshot_as_file("C:\\Users\\info\\PycharmProjects\\srikanth\\Screenshots\\test.login.png")
            self.driver.close()
            self.logger.error("***Login test is failed***")
            assert False

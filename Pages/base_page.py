from selenium import webdriver


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(20)

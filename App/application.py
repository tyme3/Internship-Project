from Pages.main_page import MainPage
from Pages.settings_page import SettingsPage
from Pages.contact_us_page import ContactUsPage


class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.settings_page = SettingsPage(driver)
        self.contact_us = ContactUsPage(driver)

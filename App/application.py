from Pages.main_page import MainPage
from Pages.settings_page import SettingsPage
from Pages.contact_us_page import ContactUsPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(driver)
        self.settings_page = SettingsPage(driver)
        self.contact_us_page = ContactUsPage(driver)

    def open_main_page(self):
        self.main_page.open()

    def login(self, email, password):
        self.main_page.login(email, password)

    def open_settings_page(self):
        self.settings_page.open_settings_page()

    def open_contact_us(self):
        self.settings_page.click_contact_us()

    def verify_contact_us_page_open(self):
        self.contact_us_page.verify_page_open()

    def verify_social_media_icons(self):
        self.contact_us_page.verify_social_media_icons()

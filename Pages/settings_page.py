from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Pages.base_page import BasePage


class SettingsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_settings_page(self, is_mobile=True):
        wait = WebDriverWait(self.driver, 10)

        if is_mobile:
            # Use mobile locator
            settings_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[wized='mobileTabProfile']")))
        else:
            # Use desktop locator
            settings_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/settings']")))

        settings_option.click()

    def click_contact_us(self):
        wait = WebDriverWait(self.driver, 10)
        contact_us_locator = (By.XPATH, "//div[@class='setting-text' and text()='Contact us']")

        contact_us_option = wait.until(EC.element_to_be_clickable(contact_us_locator))
        contact_us_option.click()


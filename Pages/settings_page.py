from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class SettingsPage:
    def __init__(self, driver):
        self.driver = driver

    def open_contact_us(self):
        wait = WebDriverWait(self.driver, 20)
        settings_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/settings']")))
        settings_option.click()
        contact_us_option = self.driver.find_element(By.XPATH, "//div[@class='setting-text' and text()='Contact us']")
        contact_us_option.click()
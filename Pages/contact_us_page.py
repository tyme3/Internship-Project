from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ContactUsPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_page_open(self):
        expected_url = "https://soft.reelly.io/contact-us"
        current_url = self.driver.current_url
        assert current_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {current_url}"

    def verify_social_media_icons(self):
        wait = WebDriverWait(self.driver, 10)
        social_media_icons = self.driver.find_elements(By.XPATH, "//a[contains(@class, 'contact-button')]")
        assert len(
            social_media_icons) >= 4, f"Expected at least 4 social media icons, Actual: {len(social_media_icons)}"

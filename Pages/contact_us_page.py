from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Pages.base_page import BasePage


class ContactUsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_page_open(self):
        expected_url = "https://soft.reelly.io/contact-us"
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_to_be(expected_url))
        current_url = self.driver.current_url
        assert current_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {current_url}"

    def verify_social_media_icons(self):
        wait = WebDriverWait(self.driver, 10)
        social_media_icons = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@class, 'contact-button')]"))
        )
        assert len(
            social_media_icons) >= 4, f"Expected at least 4 social media icons, Actual: {len(social_media_icons)}"

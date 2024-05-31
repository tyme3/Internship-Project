from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://soft.reelly.io/sign-in")

    def login(self, email, password):
        wait = WebDriverWait(self.driver, 10)
        email_input = wait.until(EC.presence_of_element_located((By.ID, "email-2")))
        email_input.send_keys(email)

        password_input = self.driver.find_element(By.ID, "field")
        password_input.send_keys(password)

        continue_button = self.driver.find_element(By.XPATH, "//a[@wized='loginButton']")
        continue_button.click()

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('I am on the main page')
def step_given_main_page(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://soft.reelly.io/sign-in")


@when('I log in')
def step_when_login(context):
    wait = WebDriverWait(context.driver, 10)
    email_input = wait.until(EC.presence_of_element_located((By.ID, "email-2")))
    email_input.send_keys("demias2@gmail.com")

    password_input = context.driver.find_element(By.ID, "field")
    password_input.send_keys("@Zz56qk96")

    continue_button = context.driver.find_element(By.XPATH, "//a[@wized='loginButton']")
    continue_button.click()


@when('I click on the settings option')
def step_when_click_settings(context):
    wait = WebDriverWait(context.driver, 20)
    settings_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/settings']")))
    settings_option.click()


@when('I click on the Contact Us option')
def step_when_click_contact_us(context):
    contact_us_option = context.driver.find_element(By.XPATH, "//div[@class='setting-text' and text()='Contact us']")
    contact_us_option.click()


@then('the Contact Us page should open')
def step_then_contact_us_page_open(context):
    expected_url = "https://soft.reelly.io/contact-us"
    current_url = context.driver.current_url
    assert current_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {current_url}"


@then('there should be at least 4 social media icons')
def step_then_social_media_icons(context):
    social_media_icons = context.driver.find_elements(By.XPATH, "//a[contains(@class, 'contact-button')]")
    assert len(social_media_icons) >= 4, f"Expected at least 4 social media icons, Actual: {len(social_media_icons)}"





from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Pages.main_page import MainPage
from Pages.settings_page import SettingsPage
from Pages.contact_us_page import ContactUsPage
import allure


@given('I am on the main page')
@allure.step('Given I am on the main page')
def step_given_main_page(context):
    context.app.open_main_page()


@when('I log in')
@allure.step('When I log in')
def step_when_login(context):
    context.app.login("demias2@gmail.com", "@Zz56qk96")


@when('I click on the settings option')
@allure.step('When I click on the settings option')
def step_when_click_settings(context):
    context.driver.implicitly_wait(4)
    context.app.open_settings_page()


@when('I click on the Contact Us option')
@allure.step('When I click on the Contact Us option')
def step_when_click_contact_us(context):
    context.driver.implicitly_wait(4)
    context.app.open_contact_us()


@then('The Contact Us page should open')
@allure.step('Then The Contact Us page should open')
def step_then_contact_us_page_open(context):
    context.app.verify_contact_us_page_open()


@then('There should be at least 4 social media icons')
@allure.step('Then there should be at least 4 social media icons')
def step_then_social_media_icons(context):
    context.driver.implicitly_wait(4)
    context.app.verify_social_media_icons()

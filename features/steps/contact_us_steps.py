from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Pages.main_page import MainPage
from Pages.settings_page import SettingsPage
from Pages.contact_us_page import ContactUsPage


@given('I am on the main page')
def step_given_main_page(context):
    context.driver.maximize_window()
    context.main_page = MainPage(context.driver)
    context.main_page.open()


@when('I log in')
def step_when_login(context):
    context.main_page.login("demias2@gmail.com", "@Zz56qk96")


@when('I click on the settings option')
def step_when_click_settings(context):
    context.settings_page = SettingsPage(context.driver)
    context.settings_page.open_contact_us()


@when('I click on the Contact Us option')
def step_when_click_contact_us(context):
    context.settings_page = SettingsPage(context.driver)
    context.settings_page.open_contact_us()


@then('the Contact Us page should open')
def step_then_contact_us_page_open(context):
    context.contact_us_page = ContactUsPage(context.driver)
    context.contact_us_page.verify_page_open()


@then('there should be at least 4 social media icons')
def step_then_social_media_icons(context):
    context.contact_us_page.verify_social_media_icons()

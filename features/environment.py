from selenium import webdriver
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from App.application import Application
from selenium.webdriver.chrome.options import Options


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """


    # driver_path = ChromeDriverManager().install()
    # service = ChromeService(driver_path)
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--window-size=1920,1080")
    # context.driver = webdriver.Chrome(service=service, options=chrome_options)

    # BROWSERSTACK
    bs_username = 'dimitrikoger_zer4fC'
    bs_access_key = 'ocBGtnnQypGzqVqxPceo'
    url = f'http://{bs_username}:{bs_access_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        'os': 'OS X',
        'osVersion': 'Big Sur',
        'browserName': 'Safari',
        'sessionName': scenario_name
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)


    # driver_path = GeckoDriverManager().install()
    # service = FirefoxService(driver_path)
    # firefox_options = webdriver.FirefoxOptions()
    # firefox_options.add_argument("--headless")
    # firefox_options.add_argument("--disable-gpu")
    # firefox_options.add_argument("--window-size=1920,1080")
    # context.driver = webdriver.Firefox(service=service, options=firefox_options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, scenario):
    context.driver.delete_all_cookies()
    context.driver.quit()


import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
#

# supported_browsers = {
#     'chrome': webdriver.Chrome,
#     'firefox': webdriver.Firefox
# }
#
#
# def pytest_addoption(parser):
#     parser.addoption('--browser_name', action='store', default='chrome',
#                      help="Choose browser: chrome or firefox")
#
#
# @pytest.fixture(scope="function")
# def browser(request):
#     browser_name = request.config.getoption("browser_name")
#
#     if browser_name in supported_browsers:
#         supported_browsers.get(browser_name)()
#         print(f"\nstart {browser_name} browser for test..")
#     else:
#         joined_browsers = ', '.join(supported_browsers.keys())
#         raise pytest.UsageError(f"--browser_name is invalid, supported browsers: {joined_browsers}")
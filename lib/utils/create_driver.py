from selenium.webdriver import Chrome,Firefox
import pytest
def get_browser_instance():
    browser_info=pytest.config.option.type.lower()
    url=pytest.config.option.env.lower()
    if browser_info=='chrome':
        driver=Chrome('browser_exe/chromedriver.exe')
    elif browser_info=='firefox':
        driver=Firefox('browser_exe/geckodriver.exe')
    driver.maximize_window()
    driver.implicitly_wait(30)
    if url=='local':
        driver.get('https://localhost/login.do')
    elif url=='prod':
        driver.get('https://demo.actitime.com/login.do')
    return driver
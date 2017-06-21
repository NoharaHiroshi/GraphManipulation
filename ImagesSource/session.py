# coding=utf-8
import contextlib
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@contextlib.contextmanager
def get_session(url):
    cap = webdriver.DesiredCapabilities.PHANTOMJS
    cap["phantomjs.page.settings.loadImages"] = False
    cap["phantomjs.page.settings.localToRemoteUrlAccessEnabled"] = False
    browser = webdriver.PhantomJS(desired_capabilities=cap)
    browser.get(url)
    try:
        yield browser
    except Exception as e:
        print e
    finally:
        browser.quit()

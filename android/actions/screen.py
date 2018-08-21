from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from appium.webdriver import Remote
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from ..utils import helper
from ..utils import custom_logger
import string
import random

class Screen():
    def __init__(self, driver: R):
        self.driver = driver

    def wait_element_visible(self, by, locator):
        self.driver.find_and_input
        pass

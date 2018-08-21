from appium.webdriver import Remote
from .screen import Screen
from ..utils import config


class Login(object):
    def __init__(self):
        self.email = config.Get.base_config()['bbmCredentials']['username']
        self.password = config.Get.base_config()['bbmCredentials']['password']

    def tap_start_button(self):
        self.screen.click_element('xpath', r'//*[@resource-id="com.bbm:id/btStart"]', 30)

    def tap_continue_button(self):
        if self.screen.wait_until_element_visible('xpath', r'//*[@resource-id="com.bbm:id/contentPanel"]', 5):
            return self.screen.click_element('xpath', r'//*[@resource-id="android:id/button1"]')
        else:
            return False

    def tap_allow_call_permission(self):
        return self.screen.click_element('xpath', r'//*[@resource-id="com.android.packageinstaller:id/permission_allow_button"]', 5)

    def tap_allow_sms_permission(self):
        return self.screen.click_element('xpath', r'//*[@resource-id="com.android.packageinstaller:id/permission_allow_button"]', 5)

    def tap_login_with_email(self):
        return self.screen.click_element('xpath', '//*[@resource-id="com.bbm:id/tvSigninEmail"]', 5)

    def input_email(self):
        return self.screen.find_element_and_input('xpath', r'//*[@resource-id="com.bbm:id/etEmail"]', 10, self.email)

    def input_password(self):
        return self.screen.find_element_and_input('xpath', r'//*[@resource-id="com.bbm:id/etPassword"]', 10, self.password)

    def tap_next(self):
        return self.screen.click_element('xpath', r'//*[@resource-id="com.bbm:id/action_setup_next"]', 5)

    # tap continue
    def tap_allow_contact_permission(self):
        return self.screen.click_element('xpath', r'//*[@resource-id="com.android.packageinstaller:id/permission_allow_button"]', 5)

    def tap_allow_file_permission(self):
        return self.screen.click_element('xpath', r'//*[@resource-id="com.android.packageinstaller:id/permission_allow_button"]', 5)
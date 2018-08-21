from appium.webdriver import Remote
from urllib.error import URLError
import os
import time


class Appium(object):
    def __init__(self, driver=Remote):
        self.driver = driver

    @staticmethod
    def driver(port: int, capabilities: dict):
        try:
            return Remote(command_executor="http://localhost:{0}/wd/hub".format(str(port)), desired_capabilities=capabilities)
        except URLError as e:
            exit(e)


import subprocess


class CProcess():

    def __init__(self):
        pass
    '''
    Make sure this process as a variable
    '''
    @staticmethod
    def open_process_in_background(cmd: str, text=False, limit=100):
        p = subprocess.Popen(cmd, shell=True, stdin=None, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, close_fds=True, universal_newlines=True)
        if text:
            print(p.stdout.readlines(limit))
        return p.pid


class Package():
    def __init__(self):
        pass

    def install(self):
        pass

    def reinstall(self):
        pass

    def uninstall(self):
        pass


if __name__ == '__main__':
    # desired_caps = dict()
    # desired_caps['app'] = "com.bbm"
    # desired_caps['udid'] = "192.168.56.101:5555"
    # desired_caps['platformName'] = "Android"
    # desired_caps['deviceName'] = "Genymotion"
    # desired_caps['appActivity'] = "com.bbm.ui.activities.StartupActivity"
    # api = Appium.driver(4000, desired_caps)
    # print(api.current_package)
    # api.quit()
    a = CProcess.open_process_in_background(cmd="ping 8.8.8.8", text=True)
    b = CProcess.open_process_in_background(cmd="ping 8.8.8.8", text=True)
    os.kill(a, 9)
    os.kill(b, 9)

from os.path import join
from pathlib import Path

from appium import webdriver as a
from robot.libraries.BuiltIn import BuiltIn
from selenium import webdriver as web_driver
from var.config_variables import *


class AppuimSessionHandler:
    __driver = None

    def __init__(self):
        bi = BuiltIn()
        bi.log_to_console("Appium session handler log")
        pass

    @staticmethod
    def open_application(appium_host='http://127.0.0.1:8888/wd/hub') -> web_driver:
        app_path = Path(__file__).parent.parent
        app_path = join(str(app_path), 'app', 'GOWeather.apk')
        caps = {'platformName': "android", 'fullReset': full_reset, 'deviceName': device_name,
                'automationName': 'UiAutomator2',
                'skipServerInstallation': True, 'appActivity': app_acctivity, 'noReset': no_reset,
                'udid': udid, 'newCommandTimeout': 1200, 'autoGrantPermissions': True,
                'appPackage': app_package, 'disableWindowAnimation': True, 'app': app_path}
        AppuimSessionHandler.__driver = a.Remote(str(appium_host), desired_capabilities=caps)
        return AppuimSessionHandler.__driver

    @staticmethod
    def get_session_instance() -> web_driver:
        if not AppuimSessionHandler.__driver:
            raise Exception('no application is open')
        return AppuimSessionHandler.__driver

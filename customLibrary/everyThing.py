from pathlib import Path
from os.path import join
from customLibrary.AppuimSessionHandler import AppuimSessionHandler
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from var.Locations import *
from customLibrary.Actions import Actions


class everyThing(Actions):
    def __init__(self):
        super().__init__()


    def scrool_to_find_precipitation(self):
        actions = TouchAction(self.driver)
        actions.scroll_from_element(forecastButton, x=90, y=1330)
        actions.scroll(x=90, y=170)
        actions.perform()


    def scrool29(self):
        el1 = self.driver.find(by=By.XPATH, locator=forecastButton)
        el2 = self.driver.find(by=By.XPATH, locator=precipitationText)
        self.driver.scroll(el1, el2)


    def click_main_menu(self):
        self.find(By.ID, mainMenu).click()


    def open_app(self):
        self.session_handler.open_application()


    def forecast_tab_Click(self):
        self.find(By.XPATH, forecastButton).click()


    def add_city(self):
        self.find(By.ID, addLocation).click()


    def popular_city(self):
        self.find(by=By.XPATH, locator=firstPopularCity).click()


    def find_degree_more_than_50(self):
        degree = self.find(by=By.ID, locator=currentPageWeather)
        if degree >= 50:
            return 1
        else:
            return 0


    def screenshot(self):
        screenshot_dir = Path(__file__).parent.parent
        screenshot_dir = join(str(screenshot_dir), 'screenshots')
        driver = AppuimSessionHandler.get_session_instance()
        Path(screenshot_dir).mkdir(parents=True, exist_ok=True)
        image_file = join(screenshot_dir, f'{"screen"}.png')

        driver.save_screenshot(image_file)

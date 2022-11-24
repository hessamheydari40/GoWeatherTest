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

    def scrooll(self):
        el1 = self.find(by=By.XPATH, locator=forecastButton)
        el2 = self.find(by=By.XPATH, locator=precipitationText)
        driver = AppuimSessionHandler.get_session_instance()
        driver.scroll(el2, el1)

    def click_main_menu(self):
        self.find(By.ID, mainMenu).click()

    def open_app(self):
        self.session_handler.open_application()

    def forecast_tab_Click(self):
        self.find(By.XPATH, forecastButton).click()

    def add_city(self):
        self.find(By.ID, addLocation).click()

    def popular_city(self):
        self.finds(by=By.ID, locator="addcity_list_item")[0].click()

    def find_degree_is_50(self):
        degree = int((self.find(by=By.ID, locator=currentPageWeather).text).split("°")[0])

        if degree != 50:
            return True
        else:
            return False

    def screenshot(self):
        screenshot_dir = Path(__file__).parent.parent
        screenshot_dir = join(str(screenshot_dir), 'screenshots')
        driver = AppuimSessionHandler.get_session_instance()
        Path(screenshot_dir).mkdir(parents=True, exist_ok=True)
        image_file = join(screenshot_dir, f'{"screen"}.png')

        driver.save_screenshot(image_file)

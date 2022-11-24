from customLibrary.AppuimSessionHandler import AppuimSessionHandler

class Actions():
    def __init__(self):
        self.session_handler = AppuimSessionHandler()
        pass

    def find(self, by , locator= None, timeout=3 ):
        driver = self.session_handler.get_session_instance()
        driver.implicitly_wait(timeout)
        el = driver.find_element(by=by, value=locator)
        return el
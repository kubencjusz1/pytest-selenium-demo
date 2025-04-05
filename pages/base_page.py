from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    """
  The Purpose Of A BasePage Is To Contain Methods Common To All Page Objects
  """

    def __init__(self, driver):
        self.driver = driver

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def find_multiple(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        #self.find(*locator).click()
        WebDriverWait(self.driver, timeout=5).until(ec.presence_of_element_located(locator)).click()

    def set(self, locator, value):
        self.find(*locator).clear()
        self.find(*locator).send_keys(value)

    def get_text(self, locator):
        return self.find(*locator).text

    def get_title(self):
        return self.driver.title

    def get_rid_off_cookies(self):
        try:
            self.driver.get("https://www.lambdatest.com/selenium-playground/")
            self.click((By.ID, "CybotCookiebotDialogBodyLevelButtonPreferences"))
            self.click((By.ID, "CybotCookiebotDialogBodyLevelButtonStatistics"))
            self.click((By.ID, "CybotCookiebotDialogBodyLevelButtonMarketing"))
            self.click((By.ID, "CybotCookiebotDialogBodyButtonDecline"))
        except TimeoutError:
            pass

    def drag_from_drop_to(self, source_location, target_location):
        source = self.find(*source_location)
        target = self.find(*target_location)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()

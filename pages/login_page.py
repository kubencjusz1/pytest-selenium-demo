from selenium.webdriver.common.by import By
from pages.account_page import AccountPage
from pages.base_page import BasePage
from utilities.test_data import TestData


class LoginPage(BasePage):
    """
  The Purpose Of A LoginPage Is To Contain Methods Used In Login Tests
  """

    email_textbox_locator = (By.ID, "input-email")
    password_textbox_locator = (By.ID, "input-password")
    login_button_locator = (By.XPATH, "//input[@value='Login']")

    def __init__(self, driver):
        super().__init__(driver)
        #self.get_rid_off_cookies()
        driver.get(TestData.ecommerce_playground_url)

    def set_email(self, email):
        self.set(self.email_textbox_locator, email)

    def set_password(self, password):
        self.set(self.password_textbox_locator, password)

    def click_login_button(self):
        self.click(self.login_button_locator)
        return AccountPage(self.driver)


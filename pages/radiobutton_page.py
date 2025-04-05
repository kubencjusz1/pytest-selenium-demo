from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RadiobuttonDemoPage(BasePage):
    """
  The Purpose Of A RadiobuttonDemoPage Is To Contain Methods To Test Radio Buttons
  """
    radio_button_demo_location = (By.XPATH, "//a[contains(text(),'Radio Buttons Demo')]")
    first_radio_button_xpath = "//p[contains(text(),'Click on button to get the selected value.')]" \
                               "/parent::div//input[@value='{gender}']"
    second_radio_button_xpath = ("//h4[contains(text(),'Gender')]/following::input[@value='{gender}']",
                                 "//h4[contains(text(),'Age')]/following::input[@value='{age}']")
    confirmation_location = ((By.ID, "buttoncheck"), (By.XPATH, "//button[text()='Get values']"))
    first_response_location = (By.CLASS_NAME, "radiobutton")
    second_response_location = ((By.CSS_SELECTOR, ".genderbutton"), (By.CSS_SELECTOR, ".groupradiobutton"))

    def __init__(self, driver):
        super().__init__(driver)
        self.get_rid_off_cookies()

    def change_to_radio_button_page(self):
        self.click(self.radio_button_demo_location)

    def use_first_radio_button(self, gender):
        self.click((By.XPATH, self.first_radio_button_xpath.format(gender=gender)))
        self.click(self.confirmation_location[0])

    def use_second_radio_button(self, gender, age):
        self.click((By.XPATH, self.second_radio_button_xpath[0].format(gender=gender)))
        self.click((By.XPATH, self.second_radio_button_xpath[1].format(age=age)))
        self.click(self.confirmation_location[1])

    def get_first_response(self):
        response = self.get_text(self.first_response_location)
        return response

    def get_second_response(self):
        response = (f"{self.get_text(self.second_response_location[0])} "
                    f"{self.get_text(self.second_response_location[1])}")
        return response

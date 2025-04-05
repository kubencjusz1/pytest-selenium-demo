from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DragNDropPage(BasePage):
    """
  The Purpose Of A DragNDropPage Is To Contain Methods Used In Drag And Drop Tests
  """
    radio_button_demo_location = (By.XPATH, "//a[contains(text(),'Drag and Drop')]")
    first_draggable_xpath = "//span[contains(text(),'Draggable {number}')]"
    first_dropzone_location = (By.ID, "mydropzone")
    second_draggable_location = (By.XPATH, "//p[contains(text(),'target')]")
    second_dropzone_location = (By.ID, "droppable")
    first_confirmation_location = (By.XPATH, "//div[contains(@id, 'droppedlist')]//span")
    second_confirmation_location = (By.XPATH, "//div[contains(@class, 'highlight')]//p")

    def __init__(self, driver):
        super().__init__(driver)
        self.get_rid_off_cookies()

    def change_to_drag_and_drop_page(self):
        self.click(self.radio_button_demo_location)

    def drag_and_drop_first(self, number):
        if number == "all":
            self.drag_from_drop_to((By.XPATH, self.first_draggable_xpath.format(number="1")),
                                   self.first_dropzone_location)
            self.drag_from_drop_to((By.XPATH, self.first_draggable_xpath.format(number="2")),
                                   self.first_dropzone_location)
        else:
            self.drag_from_drop_to((By.XPATH, self.first_draggable_xpath.format(number=number)),
                                   self.first_dropzone_location)

    def drag_and_drop_second(self):
        self.drag_from_drop_to(self.second_draggable_location, self.second_dropzone_location)

    def confirm_first_drop(self):
        elements = self.find_multiple(self.first_confirmation_location)
        elements_text = [element.text for element in elements]
        return elements_text

    def confirm_second_drop(self):
        text = self.get_text(self.second_confirmation_location)
        return text

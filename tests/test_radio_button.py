import pytest
from tests.base_test import BaseTest
from pages.radiobutton_page import RadiobuttonDemoPage


class TestRadioButton(BaseTest):
    """
  The Purpose Of A TestRadioButton Is To Contain Methods That Test Radio Button Feature
  """
    @pytest.mark.skip
    @pytest.mark.parametrize("gender, expected_response",
                             [("Female", "Radio button 'Female' is checked"),
                              ("Male", "Radio button 'Male' is checked")])
    def test_radiobutton_demo_value_1(self, gender, expected_response):
        radio_button_page = RadiobuttonDemoPage(self.driver)
        radio_button_page.change_to_radio_button_page()
        radio_button_page.use_first_radio_button(gender)
        first_response = radio_button_page.get_first_response()
        assert first_response == expected_response

    @pytest.mark.skip
    @pytest.mark.parametrize("gender, age, expected_response",
                             [("Female", "5 - 15", "Female 5 - 15"),
                              ("Male", "5 - 15", "Male 5 - 15")])
    def test_radiobutton_demo_value_2(self, gender, age, expected_response):
        radio_button_page = RadiobuttonDemoPage(self.driver)
        radio_button_page.change_to_radio_button_page()
        radio_button_page.use_second_radio_button(gender, age)
        second_response = radio_button_page.get_second_response()
        assert second_response == expected_response

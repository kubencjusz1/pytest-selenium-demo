import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utilities.test_data import TestData

options = Options()
options.add_argument("--no-default-browser-check")
options.add_argument("--disable-default-apps")
options.add_argument("--no-first-run")
options.add_argument("--disable-search-engine-choice-screen")


# @pytest.fixture(params=["chrome", "firefox", "edge"])
@pytest.fixture(params=["chrome"])
def initialize_driver(request):
    """
  The Purpose Of A initialize_driver Is To Contain Options And Fixtures Of Tests
  """
    if request.param == "chrome":
        driver = webdriver.Chrome(options=options)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "edge":
        driver = webdriver.Edge(options=options)
    request.cls.driver = driver
    print("Browser: ", request.param)
    yield
    print("Close Driver")
    driver.close()

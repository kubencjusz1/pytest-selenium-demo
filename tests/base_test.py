import pytest


@pytest.mark.usefixtures("initialize_driver")
class BaseTest:
    """
  The Purpose Of A BaseTest Is To Contain Fixtures Common To All Test Objects
  """
    pass

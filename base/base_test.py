import pytest

@pytest.mark.usefixtures("setup_driver")
class BaseTest:
    """
    Tất cả các class Test (như TestLogin) sẽ kế thừa class này 
    để tự động được khởi tạo WebDriver (setup) và đóng trình duyệt (teardown).
    """
    pass

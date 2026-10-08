import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    """
    Setup webdriver cho mỗi test case.
    Sau khi test xong sẽ tự động đóng trình duyệt.
    """
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless') # Bỏ comment dòng này nếu không muốn hiện giao diện trình duyệt khi chạy test
    options.add_argument('--start-maximized')
    
    # Khởi tạo driver bằng webdriver-manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    driver.implicitly_wait(10) # Thời gian chờ ngầm định 10s cho các element
    
    yield driver
    
    # Teardown
    driver.quit()

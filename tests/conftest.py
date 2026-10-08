import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def setup_driver(request):
    """
    Setup webdriver cho mỗi test case và gán vào class BaseTest.
    """
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless') # Bỏ comment dòng này nếu muốn chạy ngầm
    options.add_argument('--start-maximized')
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    driver.implicitly_wait(10)
    
    # Gán driver vào class test kế thừa BaseTest
    request.cls.driver = driver
    
    yield
    
    # Teardown: Đóng trình duyệt
    driver.quit()

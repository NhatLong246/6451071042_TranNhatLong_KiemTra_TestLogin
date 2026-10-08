from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10 # Thời gian chờ mặc định là 10 giây

    def wait_for_element(self, locator):
        """Đợi một element xuất hiện trên DOM"""
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            print(f"Không tìm thấy element trong {self.timeout}s: {locator}")
            return None

    def wait_for_element_visible(self, locator):
        """Đợi một element hiển thị trên màn hình"""
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            print(f"Element không hiển thị trong {self.timeout}s: {locator}")
            return None

    def click_element(self, locator):
        """Click vào một element"""
        element = self.wait_for_element_visible(locator)
        if element:
            element.click()

    def enter_text(self, locator, text):
        """Nhập text vào một ô input (type)"""
        element = self.wait_for_element_visible(locator)
        if element:
            element.clear()
            element.send_keys(text)

    def get_text(self, locator):
        """Lấy text của một element"""
        element = self.wait_for_element_visible(locator)
        return element.text if element else ""

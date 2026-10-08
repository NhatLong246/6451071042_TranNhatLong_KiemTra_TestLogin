from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    """
    Chứa các Web Elements (Locators) và các thao tác nghiệp vụ đặc thù trên trang Đăng nhập.
    """
    
    URL = "https://vanphongdientu.utc.edu.vn/Login"
    
    # --- Định nghĩa các Locators (Các phần tử trên trang) ---
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "userpwd")
    LOGIN_BUTTON = (By.XPATH, "//input[@type='submit' and @value='Đăng nhập']")
    REMEMBER_CHECKBOX = (By.ID, "persistent")
    SSO_BUTTON = (By.XPATH, "//a[contains(text(), 'Đăng nhập bằng e-mail UTC')]")
    FORGOT_PWD_LINK = (By.XPATH, "//a[contains(text(), 'Bạn quên mật khẩu đăng nhập')]")
    
    # (Các locator cho phần mã bảo mật CAPTCHA và Thông báo lỗi theo HTML thực tế)
    CAPTCHA_INPUT = (By.NAME, "captcha")
    CAPTCHA_IMAGE = (By.ID, "captcha")
    RELOAD_CAPTCHA_LINK = (By.XPATH, "//a[contains(@onclick, 'captcha')]")
    ERROR_MSG = (By.CSS_SELECTOR, "div.error")

    def __init__(self, driver):
        super().__init__(driver)

    # --- Các hàm thao tác nghiệp vụ (Page Actions) ---
    
    def open_page(self):
        """Mở trang đăng nhập"""
        self.driver.get(self.URL)

    def enter_username(self, username):
        """Nhập tên đăng nhập"""
        self.enter_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        """Nhập mật khẩu"""
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        """Click nút Đăng nhập"""
        self.click_element(self.LOGIN_BUTTON)

    def login_with_credentials(self, username, password):
        """Hàm gộp: Nhập user, pass và click đăng nhập"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def click_sso_login(self):
        """Click nút Đăng nhập bằng e-mail UTC"""
        self.click_element(self.SSO_BUTTON)

    def click_forgot_password(self):
        """Click link Quên mật khẩu"""
        self.click_element(self.FORGOT_PWD_LINK)

    def get_forgot_password_href(self):
        """Lấy giá trị đường dẫn (href) của link Quên mật khẩu"""
        element = self.wait_for_element_visible(self.FORGOT_PWD_LINK)
        if element:
            return element.get_attribute("href")
        return None

    def login_with_enter(self, username, password):
        """Nhập xong user, pass thì ấn phím Enter trên bàn phím"""
        from selenium.webdriver.common.keys import Keys
        self.enter_username(username)
        # Tìm lại ô password, điền pass rồi ấn phím Enter
        element = self.wait_for_element_visible(self.PASSWORD_INPUT)
        if element:
            element.clear()
            element.send_keys(password)
            element.send_keys(Keys.ENTER)

    def enter_captcha(self, captcha_code):
        """Nhập mã CAPTCHA"""
        self.enter_text(self.CAPTCHA_INPUT, captcha_code)

    def login_with_captcha(self, username, password, captcha_code):
        """Hàm gộp: Đăng nhập đầy đủ gồm cả CAPTCHA"""
        self.enter_username(username)
        self.enter_password(password)
        self.enter_captcha(captcha_code)
        self.click_login()

    def get_alert_text(self):
        """Lấy text từ popup cảnh báo (Alert JS) nếu hệ thống dùng Alert"""
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.common.exceptions import TimeoutException
        try:
            alert = WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            text = alert.text
            alert.accept()
            return text
        except TimeoutException:
            return ""

    def get_error_message(self):
        """Lấy text báo lỗi từ thẻ div.error (Theo HTML thực tế) hoặc Alert JS nếu có"""
        try:
            # Ưu tiên lấy từ thẻ <div class="error">
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC
            element = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(self.ERROR_MSG))
            return element.text
        except:
            # Fallback nếu hệ thống dùng Popup Alert
            return self.get_alert_text()

    def get_page_source(self):
        """Lấy toàn bộ HTML của trang để tìm text lỗi (nếu lỗi in thẳng ra màn hình)"""
        return self.driver.page_source

    def is_captcha_displayed(self):
        """Kiểm tra xem trường Mã bảo mật (ô input name='captcha') đã hiển thị hay chưa"""
        element = self.wait_for_element_visible(self.CAPTCHA_INPUT)
        return element is not None

    def force_captcha_appear(self):
        """Hàm tiện ích: Cố tình đăng nhập sai 3 lần để ép hệ thống hiện CAPTCHA"""
        for _ in range(3):
            self.login_with_credentials("user_sai", "pass_sai")
            # Cực kỳ quan trọng: Phải chờ hệ thống tải lại trang và hiện thông báo lỗi
            # rồi mới được nhập tiếp, nếu không tool chạy quá nhanh sẽ bị lỗi StaleElement
            self.get_error_message()

    def click_reload_captcha(self):
        """Click vào thẻ <a> chữ 'đây' để yêu cầu mã mới thay vì click vào ảnh"""
        self.click_element(self.RELOAD_CAPTCHA_LINK)

    def get_captcha_image_src(self):
        """Lấy giá trị src của ảnh CAPTCHA để so sánh xem ảnh đã đổi hay chưa"""
        element = self.wait_for_element_visible(self.CAPTCHA_IMAGE)
        if element:
            return element.get_attribute("src")
        return None

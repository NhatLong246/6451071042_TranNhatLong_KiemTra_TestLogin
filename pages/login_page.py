from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    """
    Tương đương LoginPage.java
    Chứa các Web Elements (Locators) và các thao tác nghiệp vụ đặc thù trên trang Đăng nhập.
    """
    
    URL = "https://vanphongdientu.utc.edu.vn/Login"
    
    # --- Định nghĩa các Locators (Các phần tử trên trang) ---
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "userpwd")
    LOGIN_BUTTON = (By.XPATH, "//input[@type='submit' and @value='Đăng nhập']")
    REMEMBER_CHECKBOX = (By.XPATH, "//input[@name='persistent']")
    SSO_BUTTON = (By.XPATH, "//a[contains(text(), 'Đăng nhập bằng e-mail UTC')]")
    FORGOT_PWD_LINK = (By.XPATH, "//a[contains(text(), 'Bạn quên mật khẩu đăng nhập')]")
    
    # (Các locator cho phần mã bảo mật CAPTCHA sẽ được bổ sung sau khi làm đến test case đó)

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

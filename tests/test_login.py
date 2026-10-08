import pytest
import time
from pages.login_page import LoginPage

class TestLoginBase:
    """
    Tương đương LoginE2ETest.java
    Class chứa các test case cơ bản (Phần 1)
    """
    
    # TC01: Để trống Username và Password
    def test_tc01_empty_both(self, driver):
        # 1. Khởi tạo đối tượng đại diện cho trang Login
        login_page = LoginPage(driver)
        
        # 2. Các bước test
        login_page.open_page()
        login_page.login_with_credentials("", "")
        
        # 3. Assert (Kiểm tra kết quả) - Tạm thời để pass chờ viết code kiểm tra thông báo lỗi
        time.sleep(2) # Tạm dừng 2s để bạn quan sát trên trình duyệt trước khi test tự động tắt
        pass

    # TC02: Để trống Username, có nhập Password
    def test_tc02_empty_username(self, driver):
        pass # Sẽ implement sau

    # TC03: Có nhập Username, để trống Password
    def test_tc03_empty_password(self, driver):
        pass # Sẽ implement sau

    # TC04: Đăng nhập bằng phím Enter
    def test_tc04_login_with_enter(self, driver):
        pass # Sẽ implement sau

    # TC05: Đăng nhập qua "E-mail UTC" (SSO)
    def test_tc05_sso_login(self, driver):
        pass # Sẽ implement sau

    # TC06: Chức năng "Quên mật khẩu"
    def test_tc06_forgot_password(self, driver):
        pass # Sẽ implement sau


class TestLoginCaptcha:
    """
    Class chứa các test case liên quan đến CAPTCHA (Phần 2)
    """
    
    # TC07: Kích hoạt cơ chế Mã bảo mật
    def test_tc07_trigger_captcha(self, driver):
        pass # Sẽ implement sau

import pytest
from pages.login_page import LoginPage
from base.base_test import BaseTest

class TestLogin(BaseTest):
    """
    Kế thừa BaseTest để tự động có sẵn self.driver
    """
    
    # TC01: Để trống Username và Password
    def test_tc01_empty_both(self):
        # 1. Khởi tạo đối tượng đại diện cho trang Login
        login_page = LoginPage(self.driver)
        
        # 2. Các bước test
        login_page.open_page()
        
        # Để trống cả user và pass rồi click Đăng nhập
        login_page.login_with_credentials("", "")
        
        # 3. Kiểm tra kết quả
        alert_text = login_page.get_alert_text()
        if alert_text:
            assert "Bạn chưa nhập tên đăng nhập" in alert_text, f"Lỗi hiển thị trên Alert không đúng: {alert_text}"
        else:
            page_text = login_page.get_page_source()
            assert "Bạn chưa nhập tên đăng nhập" in page_text, "Không tìm thấy thông báo lỗi mong đợi trên trang."

    # TC02: Để trống Username, có nhập Password
    def test_tc02_empty_username(self):
        login_page = LoginPage(self.driver)
        login_page.open_page()
        
        # Bỏ trống username, chỉ nhập password
        login_page.login_with_credentials("", "matkhau_batky")
        
        # Kiểm tra kết quả (Mong đợi giống hệt TC01: Báo lỗi chưa nhập tên đăng nhập)
        alert_text = login_page.get_alert_text()
        if alert_text:
            assert "Bạn chưa nhập tên đăng nhập" in alert_text, f"Lỗi hiển thị trên Alert không đúng: {alert_text}"
        else:
            page_text = login_page.get_page_source()
            assert "Bạn chưa nhập tên đăng nhập" in page_text, "Không tìm thấy thông báo lỗi mong đợi trên trang."

    # TC03: Có nhập Username, để trống Password
    def test_tc03_empty_password(self):
        login_page = LoginPage(self.driver)
        login_page.open_page()
        
        # Nhập username hợp lệ nhưng bỏ trống password
        login_page.login_with_credentials("masinhvien_cuaban", "")
        
        # Kiểm tra kết quả
        alert_text = login_page.get_alert_text()
        if alert_text:
            assert "Bạn chưa nhập mật khẩu" in alert_text, f"Lỗi hiển thị trên Alert không đúng: {alert_text}"
        else:
            page_text = login_page.get_page_source()
            assert "Bạn chưa nhập mật khẩu" in page_text, "Không tìm thấy thông báo lỗi mong đợi trên trang."

    # TC04: Đăng nhập bằng phím Enter
    def test_tc04_login_with_enter(self):
        login_page = LoginPage(self.driver)
        login_page.open_page()
        
        # Nhập username hợp lệ và password, sau đó ấn phím Enter
        login_page.login_with_enter("masinhvien", "matkhau")
        
        # Kiểm tra đăng nhập thành công: Chờ và kiểm tra URL thay đổi (không còn là trang Login nữa)
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        import pytest
        try:
            # Explicit wait chờ URL thay đổi (có thể đăng nhập thành công sẽ chuyển hướng)
            WebDriverWait(self.driver, 5).until(EC.url_changes(login_page.URL))
            assert "Login" not in self.driver.current_url, f"Đăng nhập thất bại, vẫn kẹt ở: {self.driver.current_url}"
        except:
            pytest.fail("Test thất bại do không thể chuyển trang (bạn cần thay thông tin thật vào code để test pass).")

    # TC05: Đăng nhập qua "E-mail UTC" (SSO)
    def test_tc05_sso_login(self):
        pytest.skip("Sẽ implement sau")

    # TC06: Chức năng "Quên mật khẩu"
    def test_tc06_forgot_password(self):
        pytest.skip("Sẽ implement sau")

    # TC07: Kích hoạt cơ chế Mã bảo mật
    def test_tc07_trigger_captcha(self):
        pytest.skip("Sẽ implement sau")

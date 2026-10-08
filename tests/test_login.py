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
        login_page = LoginPage(self.driver)
        login_page.open_page()
        
        # Click nút đăng nhập bằng Email UTC
        login_page.click_sso_login()
        
        # Chờ và kiểm tra xem URL có chuyển hướng khỏi trang đăng nhập nội bộ không
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        import pytest
        try:
            # Explicit wait chờ URL thay đổi (hệ thống sẽ gọi sang trang SSO của Google/Microsoft)
            WebDriverWait(self.driver, 5).until(EC.url_changes(login_page.URL))
            assert "Login" not in self.driver.current_url, f"Không chuyển hướng được sang SSO, vẫn ở: {self.driver.current_url}"
        except:
            pytest.fail("Test thất bại do không thể click nút SSO hoặc trang không phản hồi.")

    # TC06: Chức năng "Quên mật khẩu"
    def test_tc06_forgot_password(self):
        login_page = LoginPage(self.driver)
        login_page.open_page()
        
        # Thay vì click để tránh văng ra ứng dụng Mail của máy tính (Outlook, Mail app),
        # ta sẽ kiểm tra xem thuộc tính href có chứa mailto:hotrokythuat@utc.edu.vn hay không
        href_value = login_page.get_forgot_password_href()
        
        assert href_value is not None, "Không tìm thấy link Quên mật khẩu trên trang."
        assert "mailto:" in href_value, f"Link không trỏ đến ứng dụng email, thực tế là: {href_value}"
        assert "hotrokythuat@utc.edu.vn" in href_value, f"Email hỗ trợ không đúng, thực tế là: {href_value}"

    # TC07: Kích hoạt cơ chế Mã bảo mật
    def test_tc07_trigger_captcha(self):
        login_page = LoginPage(self.driver)
        login_page.open_page()
        
        # Đăng nhập sai 3 lần liên tiếp để ép CAPTCHA xuất hiện (Sử dụng hàm helper)
        login_page.force_captcha_appear()
            
        # Kiểm tra xem nhãn "Mã bảo mật" (CAPTCHA) có hiện ra trên màn hình không
        is_captcha_visible = login_page.is_captcha_displayed()
        
        assert is_captcha_visible, "Lỗi: Đã đăng nhập sai 3 lần nhưng hệ thống không hiển thị tính năng Mã bảo mật (CAPTCHA) như dự kiến."

    # TC08: Chức năng tải lại Mã bảo mật (Click vào ảnh)
    def test_tc08_reload_captcha(self):
        login_page = LoginPage(self.driver)
        login_page.open_page()
        
        # 1. Ép hiển thị CAPTCHA
        login_page.force_captcha_appear()
        
        # 2. Lấy link ảnh (src) hiện tại
        src_truoc = login_page.get_captcha_image_src()
        assert src_truoc is not None, "Không tìm thấy ảnh CAPTCHA trên trang"
        
        # 3. Click vào ảnh để đổi mã
        login_page.click_captcha_image()
        
        # Đợi 1 chút để ảnh mới được tải về
        import time
        time.sleep(2)
        
        # 4. Lấy link ảnh sau khi click
        src_sau = login_page.get_captcha_image_src()
        
        # So sánh 2 src xem có khác nhau không (Thông thường hệ thống sẽ thêm chuỗi random/timestamp vào src)
        assert src_truoc != src_sau, f"Ảnh CAPTCHA không thay đổi sau khi click. SRC vẫn là: {src_truoc}"

    # TC09: Để trống ô Mã bảo mật
    def test_tc09_empty_captcha(self):
        login_page = LoginPage(self.driver)
        login_page.open_page()
        
        login_page.force_captcha_appear()
        
        # Nhập username, password đúng (hoặc sai) nhưng bỏ trống CAPTCHA
        login_page.login_with_captcha("masinhvien", "matkhau", "")
        
        # Kiểm tra kết quả (thường sẽ bật alert hoặc báo chữ đỏ yêu cầu nhập mã bảo mật)
        alert_text = login_page.get_alert_text()
        if alert_text:
            assert "mã bảo mật" in alert_text.lower(), f"Lỗi hiển thị trên Alert không liên quan đến mã bảo mật: {alert_text}"
        else:
            page_text = login_page.get_page_source()
            assert "mã bảo mật" in page_text.lower(), "Không tìm thấy thông báo lỗi liên quan đến Mã bảo mật trên trang."

    # TC10: Nhập sai Mã bảo mật
    def test_tc10_wrong_captcha(self):
        login_page = LoginPage(self.driver)
        login_page.open_page()
        
        # 1. Ép hiển thị CAPTCHA
        login_page.force_captcha_appear()
        
        # Lấy src của ảnh CAPTCHA trước khi ấn Đăng nhập
        src_truoc = login_page.get_captcha_image_src()
        
        # 2. Nhập username, password và cố tình nhập sai CAPTCHA
        login_page.login_with_captcha("masinhvien_cuaban", "matkhau_cuaban", "MA_SAI_CO_TINH_123")
        
        # 3. Kiểm tra thông báo lỗi
        alert_text = login_page.get_alert_text()
        if alert_text:
            assert "mã bảo mật" in alert_text.lower() or "sai" in alert_text.lower(), f"Lỗi hiển thị trên Alert không đúng: {alert_text}"
        else:
            page_text = login_page.get_page_source()
            assert "mã bảo mật" in page_text.lower() or "sai" in page_text.lower(), "Không tìm thấy thông báo lỗi sai mã bảo mật trên trang."
            
        # 4. Đợi một chút và kiểm tra xem hệ thống có tự động đổi ảnh CAPTCHA mới không
        import time
        time.sleep(2)
        src_sau = login_page.get_captcha_image_src()
        assert src_truoc != src_sau, "Lỗi: Ảnh CAPTCHA không được tự động tải lại (src không thay đổi) sau khi nhập sai."

    # TC11: Nhập đúng Mã bảo mật, nhưng sai User/Pass
    def test_tc11_correct_captcha_wrong_credentials(self):
        pytest.skip("Sẽ implement sau")

    # TC12: Đăng nhập thành công khi có Mã bảo mật
    def test_tc12_login_success_with_captcha(self):
        pytest.skip("Sẽ implement sau")

# Dự án Kiểm thử Tự động E2E - Đăng nhập Văn phòng điện tử UTC

Dự án này sử dụng mô hình **Page Object Model (POM)** kết hợp với **Selenium WebDriver** và **Pytest** để tự động hóa quá trình kiểm thử tính năng đăng nhập của trang web Văn phòng điện tử UTC.

## 1. Cấu trúc thư mục (Page Object Model)

- `pages/`: Chứa các Page Object.
  - `base_page.py`: Các thao tác chung với Selenium (Explicit Wait, click, send_keys...).
  - `login_page.py`: Định nghĩa các Element (Locator) và các hành động cụ thể trên trang Đăng nhập.
- `tests/`: Chứa các Test Script.
  - `conftest.py`: Cấu hình Pytest, tự động khởi tạo và đóng trình duyệt cho mỗi Test Case.
  - `test_login.py`: File chứa mã kiểm thử E2E tương ứng với các Test Case.
- `TEST_CASES.md` / `TEST_CASES.xlsx`: Danh sách kịch bản kiểm thử.

## 2. Cách cài đặt

1. Đảm bảo đã cài đặt Python (phiên bản 3.x).
2. Mở Terminal tại thư mục dự án và cài đặt thư viện:
```bash
pip install -r requirements.txt
```

## 3. Cách chạy Test

Chạy toàn bộ các test case và xem kết quả trực tiếp trên Terminal:
```bash
pytest -v
```

Để chạy ngầm (Headless mode) không hiển thị UI trình duyệt, hãy bỏ comment dòng `options.add_argument('--headless')` trong file `tests/conftest.py`.

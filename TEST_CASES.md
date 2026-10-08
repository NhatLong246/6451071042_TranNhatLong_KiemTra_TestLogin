# Danh sách Test Case: Đăng nhập Văn phòng điện tử UTC
**URL:** https://vanphongdientu.utc.edu.vn/Login

## Phần 1: Các Test Case đăng nhập cơ bản

| STT | ID | Tên Test Case | Các bước thực hiện | Kết quả mong đợi |
|:---|:---|:---|:---|:---|
| 1 | TC01 | Để trống Username và Password | 1. Mở trang web đăng nhập<br>2. Để trống cả 2 ô "Tên đăng nhập" và "Mật khẩu"<br>3. Click nút "Đăng nhập" | Hệ thống cảnh báo: "Bạn chưa nhập tên đăng nhập" (hoặc focus trỏ chuột vào ô trống). |
| 2 | TC02 | Để trống Username, có nhập Password | 1. Mở trang web đăng nhập<br>2. Bỏ trống ô "Tên đăng nhập"<br>3. Nhập mật khẩu<br>4. Click "Đăng nhập" | Hệ thống cảnh báo: "Bạn chưa nhập tên đăng nhập". |
| 3 | TC03 | Có nhập Username, để trống Password | 1. Mở trang web đăng nhập<br>2. Nhập "Tên đăng nhập"<br>3. Bỏ trống ô "Mật khẩu"<br>4. Click "Đăng nhập" | Hệ thống cảnh báo: "Bạn chưa nhập mật khẩu". |
| 4 | TC04 | Đăng nhập bằng phím Enter | 1. Nhập đúng Tên đăng nhập và Mật khẩu<br>2. Nhấn phím `Enter` trên bàn phím thay vì click chuột | Đăng nhập thành công, hệ thống chuyển hướng vào trang chủ. |
| 5 | TC05 | Đăng nhập qua "E-mail UTC" (SSO) | 1. Mở trang đăng nhập<br>2. Click nút "Đăng nhập bằng E-mail UTC" | Chuyển hướng sang cổng xác thực đăng nhập của Google (accounts.google.com). |
| 6 | TC06 | Chức năng "Quên mật khẩu" | 1. Mở trang đăng nhập<br>2. Click vào dòng chữ "Bạn quên mật khẩu đăng nhập ?" | Chuyển sang màn hình khôi phục/đặt lại mật khẩu (`/Login/GetPass`). |

## Phần 2: Các Test Case về cơ chế bảo mật (Sai 3 lần & CAPTCHA)

| STT | ID | Tên Test Case | Các bước thực hiện | Kết quả mong đợi |
|:---|:---|:---|:---|:---|
| 7 | TC07 | Kích hoạt cơ chế Mã bảo mật | 1. Mở trang đăng nhập<br>2. Nhập sai Tên đăng nhập hoặc Mật khẩu liên tục 3 lần | Màn hình tải lại, hiển thị dòng chữ đỏ **"Tài khoản hoặc mật khẩu không đúng."**.<br>Giao diện xuất hiện thêm: Hình ảnh CAPTCHA, dòng link *"Click vào đây để thay đổi mã bảo mật khác"* và **ô nhập "Mã bảo mật" (nằm trên ô Tên đăng nhập)**. |
| 8 | TC08 | Thay đổi (Làm mới) mã bảo mật | 1. Ở màn hình đang có CAPTCHA, click vào chữ "đây" trong dòng *"Click vào đây để thay đổi mã..."* | Hình ảnh mã bảo mật (CAPTCHA) tải lại và hiển thị một chuỗi ký tự mới. |
| 9 | TC09 | Để trống ô Mã bảo mật | 1. Ở màn hình có CAPTCHA, nhập User và Pass<br>2. **Để trống** ô "Mã bảo mật"<br>3. Click "Đăng nhập" | Hệ thống cảnh báo yêu cầu nhập mã bảo mật (ví dụ: "Bạn chưa nhập mã bảo mật"). Không cho phép đăng nhập. |
| 10 | TC10 | Nhập sai Mã bảo mật | 1. Nhập User và Pass hợp lệ (đúng)<br>2. **Nhập sai** chuỗi ký tự hiển thị trên hình vào ô "Mã bảo mật"<br>3. Click "Đăng nhập" | Hệ thống thông báo lỗi sai mã bảo mật.<br>Hình ảnh CAPTCHA **tự động tải lại mã mới**. |
| 11 | TC11 | Nhập đúng Mã bảo mật, nhưng sai User/Pass | 1. **Nhập sai** User hoặc Pass<br>2. Nhập chính xác mã CAPTCHA vào ô "Mã bảo mật"<br>3. Click "Đăng nhập" | Thông báo chữ đỏ: *"Tài khoản hoặc mật khẩu không đúng."*.<br>Hình ảnh CAPTCHA **tự động tải lại mã mới**. |
| 12 | TC12 | Đăng nhập thành công khi có Mã bảo mật | 1. Nhập **đúng** User và Pass<br>2. Nhập **chính xác** các ký tự trên hình vào ô "Mã bảo mật"<br>3. Click "Đăng nhập" | Đăng nhập thành công, hệ thống chuyển hướng vào trang chủ Văn phòng điện tử. |

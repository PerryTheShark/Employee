Assignment 2 practice odoo
1. Kế thừa Model Employee
Mô tả: Kế thừa model hr.employee để thêm một trường mới, ví dụ: years_of_experience (số năm kinh nghiệm). Trường này sẽ được dùng để lưu số năm kinh nghiệm của nhân viên.
Điểm đánh giá: 10 điểm.
Yêu cầu:
Kế thừa model hr.employee.
Thêm trường mới years_of_experience (kiểu dữ liệu Integer).
Đảm bảo trường này có thể được lưu trữ và hiển thị trên form view của nhân viên.
2. Tạo Wizard
Mô tả: Tạo wizard để cập nhật giá trị của trường years_of_experience cho nhiều nhân viên cùng lúc.
Điểm đánh giá: 20 điểm.
Yêu cầu:
Tạo một wizard mới để cho phép người dùng chọn nhiều nhân viên và nhập số năm kinh nghiệm.
Thực hiện cập nhật dữ liệu cho trường years_of_experience của các nhân viên đã chọn.
Wizard phải có đầy đủ view giao diện để người dùng tương tác.
Thực hiện xử lý logic khi bấm nút cập nhật.
3. Thêm Quyền Mới
Mô tả: Tạo một nhóm quyền mới, ví dụ: "Employee Experience Manager", có quyền truy cập vào trường years_of_experience.
Điểm đánh giá: 10 điểm.
Yêu cầu:
Tạo nhóm người dùng mới trong hệ thống với tên "Employee Experience Manager".
Cấu hình quyền truy cập cho nhóm này, đảm bảo rằng chỉ nhóm này mới có quyền chỉnh sửa trường years_of_experience.
Định nghĩa quyền trong tệp ir.model.access.csv và security.xml.
4. Kế thừa Quyền
Mô tả: Kế thừa quyền của nhóm "Employee Experience Manager" để mở rộng quyền truy cập vào các thông tin khác trong employee.
Điểm đánh giá: 10 điểm.
Yêu cầu:
Kế thừa quyền của nhóm "Employee Experience Manager" để mở rộng truy cập vào các trường khác của nhân viên.
Ví dụ: thêm quyền truy cập vào các trường liên quan đến thông tin công việc hoặc địa chỉ của nhân viên.
Đảm bảo quyền truy cập được định nghĩa rõ ràng trong tệp cấu hình.
5. Kế thừa View
Mô tả: Kế thừa form view của hr.employee để hiển thị trường years_of_experience.
Điểm đánh giá: 10 điểm.
Yêu cầu:
Kế thừa form view mặc định của employee (form view hr.employee).
Thêm trường years_of_experience vào đúng vị trí hợp lý trên form view (ví dụ, sau phần thông tin cá nhân hoặc thông tin công việc).
Đảm bảo trường này được hiển thị và có thể chỉnh sửa bởi nhóm quyền đã được cấu hình.
6. Thêm Smartbutton
Mô tả: Thêm một smartbutton vào form view của employee để thực hiện một hành động liên quan đến kinh nghiệm của nhân viên.
Điểm đánh giá: 10 điểm.
Yêu cầu:
Thêm smartbutton vào view của employee để mở wizard cập nhật số năm kinh nghiệm (hoặc thực hiện một hành động khác liên quan).
Smartbutton phải có biểu tượng và chức năng rõ ràng, dễ sử dụng.
Khi bấm vào smartbutton, hệ thống phải mở wizard hoặc thực hiện hành động tương ứng.
7. Xử Lý Record
Mô tả: Xử lý dữ liệu của trường years_of_experience khi có thay đổi, ví dụ: giới hạn số năm kinh nghiệm tối đa, hoặc thực hiện các hành động phụ thuộc vào giá trị của trường này.
Điểm đánh giá: 20 điểm.
Yêu cầu:
Kế thừa phương thức write hoặc create của model hr.employee để xử lý dữ liệu.
Ví dụ: nếu số năm kinh nghiệm vượt quá 30, hiển thị cảnh báo cho người dùng.
Đảm bảo rằng việc xử lý dữ liệu diễn ra một cách hợp lý và không gây xung đột với các logic khác trong hệ thống.


When you install this module you must set the module name "Employee"

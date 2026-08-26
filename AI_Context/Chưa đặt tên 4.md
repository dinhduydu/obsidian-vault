Mình vừa học được cách thiết kế Data Model để không mất lịch sử thay đổi khi data trên phần mềm được update

Tuần trước mình có share lại project build data system cho CRM thì nhận được một comment góp ý là: với bảng Dimension mình có thể design theo hướng SCD (Slowly Changing Dimension) thay vì chỉ giữ thông tin mới nhất.

Lúc này mình mới nhìn lại nhận ra cách mình đang build dim_customer khá bất ổn. Hiện tại mỗi Customer trong dim_customer của mình chỉ có một record. Nếu Job Title hay Location của họ thay đổi, thông tin mới sẽ ghi đè lên thông tin cũ.

Nghe thì có vẻ không ảnh hưởng gì, vì thông tin hiện tại vẫn đúng. Nhưng vấn đề sẽ xuất hiện khi mình muốn quay lại phân tích dữ liệu trong quá khứ.

Ví dụ năm 2026, bạn A vẫn đang là Sinh viên và đăng ký học khóa Database System của công ty mình. Đến năm 2027, bạn ấy đã đi làm với vị trí Data Analyst và quay lại học thêm một khóa khác. Lúc này Job Title trên CRM được update từ Sinh viên thành Data Analyst.

Đến lúc mình quay lại phân tích: “Những người từng học Database System là Sinh viên hay Người đi làm?”

Bạn A sẽ được classify vào nhóm Người đi làm, vì Job Title hiện tại đã là Data Analyst. Trong khi lúc đăng ký Database System, bạn ấy vẫn đang là Sinh viên. Nói cách khác mình đang lấy thông tin của Customer ở hiện tại để giải thích cho một hành vi của họ trong quá khứ.

Nếu có nhiều trường hợp như vậy thì insight về chân dung khách hàng của mình hoàn toàn có thể bị lệch. Mình có thể nhìn vào data và ưu tiên target Người đi làm nhiều hơn, trong khi thực tế Sinh viên mới có thể là nhóm phù hợp hơn với khóa học tại thời điểm đó.

Thế là mình đã đi research kỹ hơn về SCD rồi quay về design lại Data Model và sửa luôn Data Mart vừa build.

Với mình đây là một practice khá hay mà trước giờ chưa ai chỉ mình :))) nên mình share lại mong là nó sẽ hữu ích cho mn  Mình có viết lại chi tiết quá trình fix trong bài viết dưới cmt 👇

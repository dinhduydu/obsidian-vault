##### **[ Tóm Gọn 16 Khái Niệm Concurrency Từ Một Bài Toán Bán Vé Duy Nhất ]**

**TL;DR:**

Mọi lỗi Concurrency đều bắt nguồn từ khoảng trống giữa bước Đọc (Read) và bước Ghi (Write) trên dữ liệu dùng chung. Bài viết này tóm gọn 16 khái niệm cốt lõi từ tầng hệ điều hành, ứng dụng cho đến hệ thống phân tán để anh chị em dễ dàng tra cứu và chọn đúng công cụ khi thiết kế hệ thống.

===============================  

Chào mọi người, chắc anh chị em làm Backend đều quen thuộc với bài toán kinh điển này: Hệ thống bán vé chỉ còn đúng 1 ghế trống. Hai người cùng bấm mua một lúc. Do giao dịch trước chưa kịp ghi xuống Database, cả hai luồng cùng đọc thấy "còn 1 ghế", cùng xuất vé thành công và kho vé bị âm (-1).  

Từ đúng một chiếc bug này, kênh System Design School đã hệ thống hóa thành 16 khái niệm cốt lõi. Mình tóm tắt lại thật cô đọng theo từng tầng kiến trúc để mọi người nắm trọn bản chất chỉ trong vài phút đọc nhé.

###### **1. Nền tảng thực thi và gốc rễ của lỗi**

- **Process và Thread:** **Process** là một chương trình đang chạy với vùng nhớ riêng biệt. **Thread** là luồng thực thi nằm trong Process. Các Thread trong cùng một Process dùng chung bộ nhớ nên giao tiếp rất nhanh, nhưng cũng vì thế mà dễ dẫm chân lên nhau khi cùng sửa một biến.
    

- **Concurrency và Parallelism:** **Concurrency** là xử lý nhiều việc đan xen nhau (chỉ cần 1 nhân CPU chuyển đổi qua lại thật nhanh giữa các Thread là đủ tạo ra Concurrency và gây lỗi bán lố vé). **Parallelism** là chạy song song thực sự tại cùng một khoảnh khắc trên nhiều nhân CPU.
    

- **Race Condition và Lost Update:** **Race Condition** xảy ra khi kết quả phụ thuộc vào việc luồng nào chạy nhanh hơn. Ví dụ khi tăng bộ đếm Like từ 41: cả hai Thread cùng đọc được 41, cùng cộng 1 và ghi đè số 42 xuống. Hai lượt Like nhưng tổng chỉ tăng 1, hiện tượng mất dữ liệu này gọi là **Lost Update**.
    

- **Critical Section:** Là đoạn code nhạy cảm trực tiếp đọc/ghi dữ liệu dùng chung (như đoạn kiểm tra số ghế rồi trừ kho). Để không lỗi, đoạn code này bắt buộc phải chạy trọn vẹn, không cho phép luồng khác xen ngang.
    

###### **2. Cách bảo vệ dữ liệu trên một máy chủ (Single Server)**

- **Lock (Mutex - Mutual Exclusion):** Cơ chế khóa chỉ cho phép đúng 1 Thread bước vào Critical Section tại một thời điểm, các Thread khác phải xếp hàng đợi. Vì phải đợi nhau nên đoạn code nằm trong Lock cần viết ngắn nhất có thể.
    

- **Deadlock:** Xảy ra khi Thread A giữ khóa 1 chờ khóa 2, còn Thread B giữ khóa 2 lại chờ khóa 1, khiến cả hai đứng hình mãi mãi. Cáchแก้ đơn giản nhất là bắt buộc mọi Thread luôn lấy khóa theo cùng một thứ tự cố định (ví dụ: luôn khóa ID nhỏ trước, ID lớn sau).
    

- **Semaphore:** Thay vì chỉ cho 1 Thread đi vào như Lock, Semaphore giữ một số lượng giấy phép (permits) nhất định để giới hạn số Thread tối đa được chạy cùng lúc (ví dụ: giới hạn đúng 10 Thread được lấy kết nối từ Database Connection Pool, Thread thứ 11 phải đợi).
    

- **Atomic Operation và Compare-And-Swap (CAS):** Thay vì dùng Lock bắt các luồng phải đợi, phần cứng hoặc Database hỗ trợ gộp bước kiểm tra và bước ghi thành một thao tác nguyên tử duy nhất (Atomic). Với **CAS**, hệ thống chỉ cập nhật giá trị mới nếu giá trị hiện tại vẫn giữ nguyên như lúc mới đọc. Nếu luồng khác đã nhanh tay sửa trước, lệnh cập nhật sẽ báo lỗi ngay lập tức mà không cần khóa.
    

###### **3. Tối ưu luồng và kiến trúc ứng dụng**

- **Thread Pool:** Tạo mới Thread cho mỗi request sẽ làm sập server khi tải tăng vọt. Thread Pool tạo sẵn một số lượng Worker Thread cố định từ đầu để tái sử dụng, các request đến sau sẽ nằm chờ trong Queue.
    

- **Event Loop và Async/Await:** Dùng một Thread duy nhất để xử lý công việc. Khi gặp tác vụ phải chờ I/O (đợi mạng, đợi DB) tại các điểm đánh dấu `await`, luồng sẽ tạm gác việc đó lại để đi xử lý request khác. Lưu ý là tại mỗi điểm `await`, một tác vụ khác có thể xen vào, nên nếu bạn kiểm tra dữ liệu xong rồi gọi `await` trước khi ghi xuống, lỗi Race Condition vẫn xảy ra như thường.
    

- **Producer-Consumer Pattern:** Thay vì để nhiều luồng cùng tranh nhau sửa dữ liệu, ta đẩy toàn bộ yêu cầu mua vé vào một hàng đợi (Queue) và chỉ dùng duy nhất 1 Consumer lấy ra xử lý tuần tự từng đơn. Không còn tranh chấp, đổi lại người dùng phải chờ xử lý bất đồng bộ (nhận thông báo "Đang xử lý đơn hàng" thay vì có kết quả ngay).
    

###### **4. Giải quyết bài toán trên hệ thống phân tán (Distributed Systems)**

Khi chạy nhiều Server cùng trỏ về 1 Database, chiếc Lock nằm trên RAM của Server nào chỉ có tác dụng trên Server đó. Lúc này ta phải dời cơ chế bảo vệ xuống tầng dùng chung:

- **Pessimistic Locking (Khóa bi quan):** Giả định xung đột rất dễ xảy ra nên khóa cứng dòng dữ liệu trong DB ngay khi đọc bằng lệnh `SELECT ... FOR UPDATE` cho đến khi Transaction kết thúc. Phù hợp khi tỷ lệ tranh chấp cực cao, nhưng dễ gây nghẽn và Deadlock.
    

- **Optimistic Locking (Khóa lạc quan):** Giả định ít khi có xung đột nên không khóa lúc đọc. Mỗi dòng dữ liệu có thêm cột `version`. Khi ghi sẽ kiểm tra `WHERE version = 7` (phiên bản lúc đọc). Ai cập nhật trước sẽ đẩy version lên 8, người đến sau không khớp version sẽ thất bại. Cách này rất nhẹ nhàng cho hệ thống có ít tranh chấp, nhưng nếu hàng ngàn người cùng săn 1 chiếc vé thì đa số sẽ bị lỗi và phải retry liên tục.
    

- **Distributed Lock và Fencing Token:** Khi cần đồng bộ tác vụ nằm ngoài một dòng DB (như gọi cổng thanh toán, chạy Cron Job), ta phải dùng khóa phân tán (như trên Redis) có gắn thời gian hết hạn (TTL) để tránh trường hợp Server giữ khóa bị sập. Tuy nhiên, nếu Server A lấy khóa xong bị treo tạm thời (như dính Garbage Collection pause dài) làm khóa hết hạn, Server B nhảy vào lấy khóa mới, lúc sau Server A tỉnh dậy vẫn tưởng mình còn khóa và ghi đè dữ liệu thì sẽ gây lỗi. Giải pháp là dùng **Fencing Token**: mỗi lần cấp khóa sẽ kèm một con số tăng dần (A nhận 33, B nhận 34). Hệ thống lưu trữ thấy số 34 của B rồi thì sẽ từ chối thẳng các lệnh ghi mang số 33 cũ kỹ của A.
    

- **Idempotency:** Không một loại Lock nào đỡ được trường hợp khách đã mua vé thành công nhưng rớt mạng làm mất phản hồi, khiến App tự động gửi lại request mua vé lần 2. Giải pháp là tính **Idempotency**: Client gửi kèm một mã định danh duy nhất (Idempotency Key) cho mỗi giao dịch. Server lưu lại key này, nếu thấy gửi lại lần hai thì chỉ trả về kết quả cũ chứ không trừ tiền hay xuất vé mới.
    

###### **Điểm cốt lõi cần nhớ**

Mỗi khi thiết kế hệ thống hay review code, anh chị em chỉ cần nhìn vào khoảng trống giữa lệnh Đọc (Read) và lệnh Ghi (Write) trên dữ liệu dùng chung. Phát hiện được khoảng trống đó rồi thì tùy vào quy mô hệ thống (1 server hay nhiều server, ít đụng độ hay tranh chấp cao) mà nhặt đúng 1 trong 16 công cụ trên ra dùng là giải quyết gọn gàng bài toán.

  
-----------------

Trong 16 khái niệm này, anh chị em hay sử dụng cơ chế nào nhất trong dự án thực tế của mình, cùng bình luận chia sẻ thêm ở dưới nhé!
Mình đang xây AI Agent Runtime theo một hướng khá lớn là tự xây một AI Agent Runtime từ đầu.

Xây phần Graph Engineering bên dưới để kiểm soát toàn bộ quá trình một request được hiểu, điều phối và thực thi.

Mình muốn Runtime có sức mạnh theo hướng của OpenClaw hay Hermes, nhưng mình không thiết kế theo kiểu một coding agent.

AutronAI tập trung vào các Agent chuyên biệt cho bài toán thực tế:
Document Agent xử lý tài liệu.
SQL Agent làm việc với database.
Tool Agent sử dụng tools và integrations.
Custom Agent cho những bài toán đặc thù.
Bên cạnh đó là các System Agent có sẵn trong lõi như Automation Agent, Web Search Agent, Memory Agent,...

Ví dụ một doanh nghiệp cần phân tích tình hình vận hành:
Document Agent đọc báo cáo, hợp đồng và tài liệu nội bộ → SQL Agent phân tích dữ liệu từ database → Tool Agent lấy thêm dữ liệu từ các hệ thống khác → Custom Agent đối chiếu các quy tắc nghiệp vụ (Agent được thiết kế quanh những nghiệp vụ, dữ liệu và hệ thống thực tế hơn là các coding agent).

Không phải coding agent không làm được, mà vấn đề là nó không được tối ưu cho những nghiệp vụ cụ thể này. Agent chuyên biệt có phạm vi rõ ràng, context đúng, tool đúng nên có thể giảm chi phí và đạt hiệu năng tốt hơn.

Điểm mình hướng tới là không để một Agent phải biết tất cả.
Đúng Agent + Đúng Tool + Đúng Model + Đúng Execution
Mình muốn AutronAI không chỉ là nơi tạo AI Agent, mà là một Runtime nơi nhiều Agent chuyên biệt có thể phối hợp để giải quyết những bài toán thực tế.

Đây là phần lõi mình đang tập trung xây.

AutronAI vẫn đang trong quá trình xây dựng và mình muốn tìm thêm những người cùng quan tâm đến AI Agent, Automation và bài toán AI thực tế để cùng thử nghiệm, góp ý hoặc hợp tác.

Nếu mn thấy hướng này thú vị, rất vui nếu được mọi người ủng hộ, góp ý hoặc cùng mình xây tiếp. 🚀

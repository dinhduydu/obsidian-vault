Phân tích chuyên sâu ngữ pháp JLPT N2, xuất Markdown thuần cho Obsidian gồm: Summary, Error Analysis, Knowledge Extracted, Learning Profile, Weak Points, Action Next.

**Knowledge Extracted** chia category: Vocabulary, Kanji, Katakana, Grammar, Particle, Reading, CompoundVerb, Adverb, Conjunction, FixedExpression, Collocation, Keigo, Kenjougo, Demonstratives.

Mỗi item dùng đúng format `### CATEGORY | ITEM_NAME`, không gộp nhiều kiến thức.

Mọi item gồm:
- **Meaning:** Nghĩa tiếng Việt, thêm tiếng Anh nếu hữu ích.
- **Trigger:** Cấu trúc, điều kiện và ngữ cảnh sử dụng.
- **Contrast:** So sánh ngữ pháp gần nghĩa.
- **One-line Summary:** Tóm tắt dễ nhớ.

Riêng Grammar bổ sung:
- **Semantic Field:** Nhóm ngữ nghĩa.
- **Confusion Index:** Các ngữ pháp dễ nhầm.
- **Why Wrong:** Nguyên nhân nhầm lẫn và cách tránh.

**Phân tích ngữ pháp:**
- Dựa trên file *Phân Loại Ngữ pháp JLPT* và *JLPT Grammar Confusion Index (N3–N1)* đính kèm.
- Chủ động tìm các ngữ pháp N2–N1–N3 gần nghĩa, dễ nhầm; ví dụ `〜からといって ↔ 〜とは限らない`, `〜を通じて ↔ 〜を通して`, `〜ものの ↔ 〜とはいえ`.
- Với mỗi cặp, nêu điểm giống/khác về nghĩa, sắc thái, cấu trúc, ngữ cảnh; khả năng thay thế; ví dụ tiếng Nhật kèm dịch tiếng Việt và mẹo làm bài JLPT.
- Nếu không có bài làm gốc, chỉ phân tích **Common Mistake**, không bịa lỗi thực tế.
- Không chỉ liệt kê tên ngữ pháp; phải giải thích sự khác biệt cụ thể.

**Learning Profile:** Tạo cho 100% item trong Knowledge Extracted, giữ nguyên tên và format:

### CATEGORY | ITEM_NAME
- **Correct:** +N
- **Wrong:** +N
- **Last Seen:** YYYY-MM-DD
- **Mastery:** High / Medium / Low
- **Priority:** High / Medium / Low

Item chưa có dữ liệu lịch sử: mặc định Correct +0, Wrong +1, Last Seen là ngày phân tích, Mastery Low, Priority High. Không tự tạo số liệu lịch sử cho item đã có dữ liệu.

Với Adverb, Katakana, CompoundVerb, FixedExpression, Collocation, Demonstratives, bổ sung **Meaning, Usage, Example**.

**Quy tắc đầu ra:**
- Giải thích chủ yếu bằng tiếng Việt, Markdown thuần tương thích Obsidian.
- Không thêm lời dẫn, không viết `Grammar:` hoặc `ITEM:`.
- Mỗi kiến thức có item riêng; mọi ngữ pháp được đề cập phải có mặt trong cả Knowledge Extracted và Learning Profile.
- Không tạo item chung chung, không trùng lặp nội dung.
- Summary tổng hợp điểm phân biệt; Error Analysis nêu lỗi thực tế hoặc lỗi phổ biến; Weak Points xác định cặp dễ nhầm; Action Next đề xuất nội dung ôn tập.
- Chỉ khẳng định cấp độ JLPT khi có căn cứ.
- Ưu tiên chất lượng phân biệt ngữ pháp, không mở rộng lan man.
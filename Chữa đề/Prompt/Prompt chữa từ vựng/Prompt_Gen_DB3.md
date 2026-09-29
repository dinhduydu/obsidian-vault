Phân tích toàn bộ bài làm tiếng Nhật và xuất Markdown thuần cho Obsidian gồm:  
Summary, Error Analysis, Knowledge Extracted, Learning Profile, Weak Points, Action Next.  
  
Knowledge Extracted bắt buộc chia category:  
Vocabulary, Kanji, Katakana, Grammar, Particle, Reading, CompoundVerb, Adverb, Conjunction, FixedExpression, Collocation, Keigo, Kenjougo, Demonstratives.  
  
Mỗi item trong Knowledge Extracted bắt buộc viết đúng format:  
### CATEGORY | ITEM_NAME  
Ví dụ: 
### Grammar | 〜ざるを得ない  
hoặc 
### Grammar | 〜を通じて

- **Meaning:** Thông qua (phương tiện/trung gian) / Suốt (khoảng thời gian).
- **Trigger:** N (phương tiện truyền tin như 本, ニュース) hoặc N (thời gian như 一年間).
- **Contrast:** `〜によって` (nhấn mạnh phương thức/công cụ trực tiếp).
- **Semantic Field:** G1 Grammar Confusion.
- **Confusion Index:** `〜を通して ↔ 〜を通じて`.
- **Why Wrong:** Người làm đúng câu này, nhận diện được "sách" là trung gian của tri thức.
- **One-line Summary:** Diễn tả việc đạt được gì đó qua trung gian hoặc một trạng thái suốt một thời gian.


Không viết "Grammar:" hoặc "ITEM:" hoặc gộp nhiều kiến thức trong 1 item.  
Mọi item phải có: Meaning, Trigger, Contrast, One-line Summary.

Với mỗi item là Vocabulary thêm: Correct Synonym, Distractor1–3, Explanation (cùng từ loại, ưu tiên JLPT N1–N3, tránh từ hiếm).
Với mỗi item là Grammar, dựa trên file Phân Loại Ngữ pháp JLPT đính kèm, liệt kê 1 vài ngữ pháp có cùng trường nghĩa
Dựa trên file JLPT Grammar Confusion Index (N3–N1), chỉ ra những ngữ pháp đi kèm, ví dụ:
からといって　とはかぎらない
Với mỗi item là Grammar, giải thích chi tiết vì sao người làm chọn sai ngữ pháp 

Learning Profile phải tạo cho 100% item đã xuất hiện ở Knowledge Extracted, bắt buộc giữ nguyên tên item và format:  
### CATEGORY | ITEM_NAME  
- Correct: +N  
- Wrong: +N  
- Last Seen: YYYY-MM-DD  
- Mastery:  
- Priority:  
Ví dụ: 

Grammar | 〜ないことには

- Correct: +1
- Wrong: +0
- Last Seen: 2026-06-28
- Mastery: High
- Priority: Low

Adverb, Katakana, CompoundVerb, FixedExpression, Collocation, Demonstratives phải ghi thêm Meaning, Usage, Example.  
Không tạo item chung như "& Kiến thức liên quan", "Cụm từ cố định N2"; phải dùng đúng tên kiến thức Nhật cụ thể.
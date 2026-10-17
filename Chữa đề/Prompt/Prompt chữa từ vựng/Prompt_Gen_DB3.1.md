Phân tích toàn bộ bài làm tiếng Nhật và xuất Markdown thuần cho Obsidian, gồm đúng 6 section theo thứ tự: Summary, Error Analysis, Knowledge Extracted, Learning Profile, Weak Points, Action Next.

**Ngôn ngữ:** Giải thích chủ yếu bằng tiếng Việt  để dễ hiểu và ghi nhớ, có thể thêm nghĩa tiếng Anh khi cần. Giữ nguyên cách viết và capitalization của section, category, field và Japanese item name. Không dùng tên section hoặc field ở dạng lowercase.

**Knowledge Extracted** bắt buộc chia theo các category: Vocabulary, Kanji, Katakana, Grammar, Particle, Reading, CompoundVerb, Adverb, Conjunction, FixedExpression, Collocation, Keigo, Kenjougo, Demonstratives.

Mỗi item phải có heading theo đúng format:

### CATEGORY | ITEM_NAME

Ví dụ: `### Grammar | 〜を通じて`

Mỗi item bắt buộc có:

- **Meaning:** Meaning in English, optionally with Vietnamese translation.
    
- **Trigger:** Contextual clues, usage conditions, or sentence patterns.
    
- **Contrast:** Differences from similar words or grammar.
    
- **One-line Summary:** A concise English summary for memorization.
    

Không viết `Grammar:` hoặc `ITEM:`, không gộp nhiều kiến thức vào một item, không tạo item chung như `Related Knowledge` hoặc `Fixed Expressions N2`. Mỗi kiến thức cụ thể chỉ xuất hiện một lần.

Với mỗi **Vocabulary**, thêm `Correct Synonym`, `Distractor1`, `Distractor2`, `Distractor3`, `Explanation`. Các từ thay thế phải cùng từ loại, ưu tiên JLPT N1–N3, phổ biến và có giải thích rõ sự khác biệt.

Với mỗi **Grammar**, thêm `Formation`, `Semantic Field`, `Related Grammar`, `Confusion Index`, `Why Wrong`, `Why Correct`, `Example`. Dựa trên file `Phân Loại Ngữ pháp JLPT` để tìm ngữ pháp cùng trường nghĩa và file `JLPT Grammar Confusion Index (N3–N1)` để tìm các cặp dễ nhầm, ví dụ `からといって` và `とは限らない`. Giải thích chi tiết bằng tiếng Anh vì sao lựa chọn sai không phù hợp và vì sao đáp án đúng phù hợp ngữ cảnh. Chỉ sử dụng thông tin từ file khi có thể xác minh; không tự bịa dữ liệu.

Với mỗi item thuộc **Adverb, Katakana, CompoundVerb, FixedExpression, Collocation, Demonstratives**, thêm `Usage` và `Example` bằng tiếng Nhật kèm bản dịch tiếng Anh.

**Learning Profile** phải tạo cho 100% item duy nhất trong Knowledge Extracted, giữ nguyên category, tên tiếng Nhật và format heading:

### CATEGORY | ITEM_NAME

- **Correct:** +N
    
- **Wrong:** +N
    
- **Last Seen:** YYYY-MM-DD
    
- **Mastery:** High / Medium / Low / Unknown
    
- **Priority:** High / Medium / Low
    

Chỉ ghi số lần đúng/sai và ngày khi có dữ liệu xác minh; nếu thiếu, ghi `Unknown`. Đánh giá Mastery và Priority dựa trên bằng chứng thực tế, không suy diễn rằng một câu đúng đồng nghĩa đã thành thạo. Không bỏ sót item hoặc tạo item mới trong Learning Profile.

**Error Analysis** phải phân tích từng lỗi, đặc biệt là lỗi ngữ pháp: đáp án đã chọn, đáp án đúng, nguyên nhân sai, dấu hiệu nhận biết và cách phân biệt.

**Weak Points** tổng hợp điểm yếu dựa trên lỗi thực tế, nêu nguyên nhân và mức độ ưu tiên. **Action Next** đưa ra kế hoạch ôn tập, bài tập đối chiếu kiến thức dễ nhầm và tiêu chí đánh giá tiến bộ.

Cuối cùng, kiểm tra tính nhất quán giữa Knowledge Extracted và Learning Profile, loại bỏ nội dung trùng lặp, giữ Markdown tương thích với Obsidian. Nếu thiếu dữ liệu hoặc file đính kèm, ghi rõ giới hạn thay vì tự tạo thông tin. Chỉ xuất Markdown hoàn chỉnh, không thêm lời dẫn hoặc code fence.
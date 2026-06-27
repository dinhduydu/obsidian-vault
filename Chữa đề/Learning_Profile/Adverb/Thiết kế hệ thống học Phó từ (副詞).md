Dựa trên danh sách phó từ và các phân loại ban đầu từ tài liệu "Adverb Navigation.pdf", dưới đây là thiết kế hệ thống học Phó từ (副詞) toàn diện trong Obsidian. Hệ thống này được tối ưu hóa để kết nối với các thành phần khác như Vocabulary, Grammar và các ghi chép từ bài tập (Knowledge Extracted).

1. Cấu trúc Thư mục và Phân loại (Taxonomy)

Để đảm bảo tính mở rộng và khả năng tra cứu, hệ thống sẽ được phân cấp như sau:

- **01_Adverb_Library/**: Chứa các note chi tiết cho từng từ (Word notes).
- **02_Adverb_Groups/**: Các note phân loại theo sắc thái/chức năng (Category notes). Dựa trên tài liệu, chúng ta có các nhóm như:
    - `Sắc thái Thay đổi theo thời gian.md` (ví dụ: 徐々に, だんだん, 次第に).
    - `Phó từ đi kèm phủ định.md` (ví dụ: めったに, ろくに, 決して, ちっとも).
    - `Trạng thái/Cảm xúc (Onomatopoeia).md` (ví dụ: いらいら, うとうと, がっかり).
    - `Mức độ/Số lượng.md` (ví dụ: かなり, ごく, たっぷり).
- **03_Adverb_Comparisons/**: Các note so sánh cặp từ dễ nhầm lẫn (Compare notes).
- **04_Adverb_Collocations/**: Các note tập trung vào cụm từ cố định (Fixed Expressions).

---

2. Template Chi tiết cho Phó từ (Adverb Word Template)

Mẫu này sử dụng Properties (YAML) để tương thích với Dataview và liên kết tự động với các hệ thống khác.

```
---
type: Adverb
word: "{{title}}"
reading: 
meaning: 
level: # JLPT N1/N2/N3
nuance_group: "[[Sắc thái Thay đổi theo thời gian]]" # WikiLink đến Category
related_grammar: [] # Link đến [[Grammar Note]]
related_vocab: [] # Link đến [[Vocabulary Note]]
tags: #Adverb #JapaneseLearning
---

# Phó từ: {{title}}

> [!abstract] **Quick View**
> - **Ý nghĩa chính:** 
> - **Sắc thái:** 
> - **Tần suất dùng:** ⭐⭐⭐

## 📖 Meaning & Usage
- **Giải nghĩa:** 
- **Cách dùng:** (Ví dụ: Thường đi với thể phủ định, hoặc dùng trong văn viết/văn nói).

## ⚖️ Contrast (So sánh)
- **So sánh với:** [[Đối thủ của từ này]]
- **Điểm khác biệt:** 

## 🔗 Collocation & Fixed Expressions
- **Cụm từ hay đi kèm:**
    - `{{title}}` + V/Adj: 
    - Biểu thức cố định: 

## ⚠️ Common Mistakes
- **Lỗi thường gặp:** (Ví dụ: Nhầm lẫn về mức độ hoặc nhầm với từ có âm đọc gần giống).

## 📝 Examples
1. (Câu ví dụ từ nguồn tài liệu hoặc bài đọc)
2. (Câu ví dụ tự đặt)

## 🏗️ Knowledge Extracted (Liên kết bài tập)
- Nguồn: [[Tên Note phân tích bài làm]]
- Ngữ cảnh đã gặp: 

## 📓 Personal Practice & Review
- [ ] Đã đặt câu với từ này?
- [ ] Đã nghe/thấy trong thực tế?
- **Ghi chú thêm:** 
```

---

3. Phương pháp Phân loại theo Chức năng & Sắc thái

Dựa trên tài liệu "Adverb Navigation.pdf", hệ thống sẽ nhóm các từ có cùng "hành vi" ngữ pháp:

1. **Nhóm thay đổi dần dần:** Tập hợp các từ như `徐々に` (Dần dần), `だんだん` (Dần dần), `次第に` (Dần theo thứ tự).
2. **Nhóm đi kèm phủ định (Chin-haku):** Đây là nhóm quan trọng nhất cho thi JLPT, bao gồm `めったに` (Hiếm khi), `ろくに` (Chẳng ra hồn), `決して` (Quyết không).
3. **Nhóm chỉ thái độ/tâm trạng:** `いらいら` (Sốt ruột), `うとうと` (Mơ màng), `がっかり` (Thất vọng).

---

4. Khả năng Liên kết và Tương thích (Connectivity)

Để hệ thống không bị tách biệt, chúng ta sử dụng **WikiLinks/Backlinks**:

- **Với Grammar:** Nếu phó từ `決して` thường đi với mẫu câu `〜ない`, trong note phó từ sẽ có thuộc tính `related_grammar: [[Grammar_Nai_Form]]`.
- **Với Knowledge Extracted:** Khi bạn phân tích một câu sai trong bài tập, prompt phân tích sẽ sinh ra một liên kết dạng `[[Phó từ]]`. Obsidian sẽ tự động liệt kê các bài tập đó trong phần **Backlinks** của note phó từ, giúp bạn thấy ngay ngữ cảnh thực tế mình từng làm sai.
- **Với Compound Verb/Collocation:** Sử dụng mục `Collocation` để liên kết trực tiếp, ví dụ: `[[徐々に]]` + `[[変化する]]`.

---

5. Obsidian Canvas cho "Adverb Map" (Visual Learning)

Bạn nên tạo một **Obsidian Canvas** để học phó từ theo trực quan:

- **Trục Mức độ:** Sắp xếp các phó từ chỉ mức độ từ thấp đến cao (ví dụ: `少し` < `かなり` < `非常に` < `極めて`).
- **Vòng tròn Sắc thái:** Nhóm các từ tượng hình (Onomatopoeia) có cùng âm tiết đầu (ví dụ: nhóm `ふ` - `ふわふわ`, `ふらふら`, `ふいに関`).
- **Cây quyết định:** Dùng cho các phó từ dễ nhầm lẫn như `いよいよ` vs `とうとう` vs `ついに`.

Chiến lược Triển khai:

1. **Tạo Note mục lục (MOC):** Sử dụng danh sách từ trong tài liệu (từ `あいかわらず` đến `頻繁`) để làm checklist tổng.
2. **Tự động hóa:** Khi đọc một bài đọc (Reading) và gặp phó từ, hãy nhấn `Alt + Click` vào WikiLink của từ đó để tạo note mới dựa trên Template đã thiết kế.
3. **Review:** Sử dụng plugin "Periodic Notes" hoặc "Spaced Repetition" để truy cập lại mục `Personal Practice` trong mỗi note.
# Japanese Learning Flow

## 1. Learning loop (overview)

```mermaid
sequenceDiagram
    actor User as 👤 Learner
    participant Inbox as Obsidian Inbox
    participant KB as Knowledge Base
    participant Review as Review Note<br/>(*Phân Tích*.md)
    participant AI as NotebookLM / AI
    participant Tool as Python Tool<br/>(generate_dashboard.py)
    participant Dash as Dashboard.md

    User->>Inbox: Gặp từ / câu mới
    User->>Inbox: Phân loại & tạo note
    Note over Inbox,KB: Vocabulary · Kanji · Grammar · Reading · ...

    User->>Review: Tạo đề ôn tập (Markdown)
    User->>AI: Upload đề review
    AI-->>User: Bài tập / giải thích

    User->>Review: Làm bài & ghi Learning Profile
    Note over Review: Correct / Wrong / Mastery / Priority

    User->>Tool: Chạy script
    Tool->>Review: Đọc & parse Learning Profile
    Tool->>KB: Cập nhật Learning_Profile/*.md
    Tool->>Dash: Tạo Dashboard (điểm yếu, review queue)
    User->>Dash: Xem thống kê & chọn mục cần ôn
```

## 2. Python tool pipeline

`generate_dashboard.py` quét vault, gộp dữ liệu từ mọi bài review, rồi sinh profile + dashboard.

```mermaid
sequenceDiagram
    participant Main as generate_dashboard.py
    participant Scanner as scanner
    participant Parser as parser
    participant Merge as knowledge dict
    participant Profiles as profile_generator
    participant Dashboard as dashboard_generator
    participant Vault as Obsidian Vault

    Main->>Scanner: find_review_files(VAULT_ROOT)
    Note over Scanner: Tìm *.md có "Phân Tích"<br/>bỏ qua Dashboard
    Scanner-->>Main: danh sách file review

    loop mỗi file review
        Main->>Scanner: extract_date(file)
        Scanner-->>Main: ngày review (thư mục DDMMYYYY)

        Main->>Parser: parse_review_file(file, date)
        Parser->>Parser: extract_category_map()
        Note over Parser: Đọc dòng "Category | keyword"<br/>strip wiki-link [[Page|Alias]]
        Parser->>Parser: parse_profiles()
        Note over Parser: Tách block theo heading<br/>đọc Correct / Wrong / Mastery / Priority
        Parser-->>Main: KnowledgeItem[]
    end

    Main->>Merge: gộp theo name
    Note over Merge: Cộng correct & wrong<br/>giữ last_seen mới nhất

    Main->>Profiles: generate_profiles(knowledge)
    Profiles->>Vault: Learning_Profile/{Category}/{name}.md
    Note over Profiles: Ghi stats + Related Reviews<br/>giữ vùng USER_START/USER_END

    Main->>Dashboard: generate_dashboard(knowledge, reviews)
    Dashboard->>Vault: Dashboard.md
    Note over Dashboard: Overall · Review Queue<br/>Weak Points · Category stats
```

## 3. Parser detail (keyword extraction)

```mermaid
flowchart LR
    A["Heading line<br/>Adverb | [[ともかく]]"] --> B[split_heading_category]
    B --> C[clean_name]
    C --> D[normalize_text]
    D --> E[strip prefix<br/>Adverb: · Vocabulary: ...]
    E --> F[strip_wikilink]
    F --> G["keyword: ともかく"]

    H["Adverb | ともかく"] --> B
    I["Adverb | [[Page|Alias]]"] --> B
    B --> J["keyword: Alias"]
```

---
cssclasses:
  - handwritten-note
---

# making it fair

## 100,000,000

> **ways to write the same API × 8 languages**

### Questions to consider

- ORM or raw SQL?
- async or threads?
- pool size?
- how many workers?

- add a cache?
- which JSON library?
- GC / JIT flags?
- native image?

- which framework?
- which DB driver?
- prepared statements?
- HTTP/2?

---

## Quick takeaway

> **Same API ≠ same implementation.**

The result can change dramatically depending on the runtime,
framework, database driver, concurrency model, and deployment choices.

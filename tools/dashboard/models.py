from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class KnowledgeItem:

    # tên kiến thức
    name: str

    # Grammar / Vocabulary / Kanji / Reading / Topics
    category: str

    # tổng số lần đúng
    correct: int = 0

    # tổng số lần sai
    wrong: int = 0

    # lần xuất hiện gần nhất
    last_seen: datetime = datetime.min

    # 🔴 Low / 🟠 Medium / 🟢 High
    mastery: str = ""

    # 🔴 High / 🟠 Medium / 🟢 Low
    priority: str = ""

    # backlink review
    reviews: set = field(default_factory=set)

    @property
    def total(self):

        return self.correct + self.wrong

    @property
    def accuracy(self):

        if self.total == 0:
            return 0

        return round(
            self.correct / self.total * 100,
            1
        )

    @property
    def review_score(self):

        score = self.wrong * 5

        priority = self.priority.lower()
        mastery = self.mastery.lower()

        # Priority bonus
        if "high" in priority:
            score += 10

        elif "medium" in priority:
            score += 5

        # Mastery penalty
        if "low" in mastery:
            score += 5

        elif "medium" in mastery:
            score += 2

        return score
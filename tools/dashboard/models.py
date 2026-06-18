from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class KnowledgeItem:

    name: str

    # Vocabulary / Grammar / Kanji / ...
    category: str

    correct: int = 0

    wrong: int = 0

    last_seen: datetime = field(
        default_factory=lambda: datetime.min
    )

    mastery: str = ""

    priority: str = ""

    reviews: set = field(
        default_factory=set
    )


    @property
    def total(self):

        return (
            self.correct
            + self.wrong
        )


    @property
    def accuracy(self):

        if self.total == 0:
            return 0

        return round(
            self.correct
            / self.total
            * 100,
            1
        )


    @property
    def review_score(self):

        score = (
            self.wrong * 5
        )

        priority = (
            self.priority.lower()
        )

        mastery = (
            self.mastery.lower()
        )


        if "high" in priority:
            score += 10

        elif "medium" in priority:
            score += 5


        if "low" in mastery:
            score += 5

        elif "medium" in mastery:
            score += 2


        return score
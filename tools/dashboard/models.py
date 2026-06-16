from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class KnowledgeItem:

    name: str

    category: str

    correct: int = 0

    wrong: int = 0

    last_seen: datetime = datetime.min

    mastery: str = ""

    priority: str = ""

    reviews: set = field(
        default_factory=set
    )

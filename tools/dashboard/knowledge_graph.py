from dataclasses import dataclass, field

@dataclass
class KnowledgeGraph:

    compound_verbs: set = field(
        default_factory=set
    )

    adverbs: set = field(
        default_factory=set
    )

    conjunctions: set = field(
        default_factory=set
    )

    collocations: set = field(
        default_factory=set
    )
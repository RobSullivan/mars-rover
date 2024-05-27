from collections.abc import Sequence
from dataclasses import dataclass, field


@dataclass
class Surface:
    rows: int
    columns: int
    robots: Sequence = field(default_factory=list)

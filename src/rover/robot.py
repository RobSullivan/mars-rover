from collections.abc import Sequence
from dataclasses import dataclass, field
from enum import Enum

from rover import gps as rover_gps


class Status(Enum):
    LOST = "LOST"
    ACTIVE = "ACTIVE"
    IDLE = "IDLE"


@dataclass
class Robot:
    starting_position: rover_gps.Coordinates
    orientation: rover_gps.Orientation
    gps: rover_gps.Gps
    steps: Sequence[rover_gps.Step] = field(default_factory=list)

    status: Status = Status.IDLE

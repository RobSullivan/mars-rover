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

    def start(self, *, directions: str, gps: rover_gps.Gps):
        """
        Start the Robot.

        Create a plan of steps for the Robot to follow.

        Then "move" the Robot by iterating over the steps.
        """

        # Get the steps the robot is going to take
        plan = gps.get_plan(
            directions=directions,
            position=self.starting_position,
            orientation=self.orientation,
        )

        for step in plan:
            self.steps.append(step)
            self.orientation = step.orientation
            self.status = Status.ACTIVE

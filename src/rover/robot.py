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

    def __init__(self, starting_position, gps, orientation) -> None:

        self.starting_position = starting_position
        self.orientation = orientation
        self.gps = gps
        self.steps = []
        self.gps.surface.add_robot(self)

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
            try:
                gps.destination_available(step.destination)
            except rover_gps.OutOfBounds:
                self.status = Status.LOST
                break
            except rover_gps.DestinationUnavailable:
                # TODO: handle this. For now do nothing except sit IDLE
                self.status = Status.IDLE
                break

            self.steps.append(step)
            self.orientation = step.orientation
            self.status = Status.ACTIVE

    def get_latest_position(self) -> rover_gps.Coordinates:
        try:
            last_step = self.steps[-1]
        except IndexError:
            return self.starting_position
        else:
            return last_step.destination

    def report(self) -> tuple[tuple, Status]:
        latest_position = self.get_latest_position()
        x, y = latest_position.x, latest_position.y
        return f"({x}, {y}, {self.orientation.value}) {self.status.value}"

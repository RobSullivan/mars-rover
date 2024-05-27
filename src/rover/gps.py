from collections.abc import Sequence
from dataclasses import dataclass
from enum import Enum

from rover import surface as rover_surface


class Orientation(Enum):
    NORTH = "N"
    EAST = "E"
    SOUTH = "S"
    WEST = "W"


class Direction(Enum):
    FORWARD = "F"
    RIGHT = "R"
    LEFT = "L"
    BACKWARD = "B"


@dataclass
class Coordinates:
    x: int
    y: int


INCREMENT = 1
DECREMENT = 1


@dataclass
class Step:
    destination: Coordinates
    orientation: Orientation
    direction: Direction


@dataclass
class Gps:
    surface: rover_surface.Surface

    def get_coordinates_and_orientation(
        self, *, direction: str, position: Coordinates, orientation: Orientation
    ) -> tuple[Coordinates, Orientation]:
        """
        Given a direction, position and orientation return new coordinates and orientation.
        """

        match (orientation, direction):
            case (
                (Orientation.NORTH, Direction.FORWARD)
                | (Orientation.SOUTH, Direction.BACKWARD)
                | (Orientation.EAST, Direction.LEFT)
                | (Orientation.WEST, Direction.RIGHT)
            ):
                return (
                    Coordinates(x=position.x, y=position.y + INCREMENT),
                    Orientation.NORTH,
                )
            case (
                (Orientation.SOUTH, Direction.FORWARD)
                | (Orientation.EAST, Direction.RIGHT)
                | (Orientation.WEST, Direction.LEFT)
            ):
                return (
                    Coordinates(x=position.x, y=position.y - DECREMENT),
                    Orientation.SOUTH,
                )
            case (
                (Orientation.SOUTH, Direction.LEFT)
                | (Orientation.EAST, Direction.FORWARD)
                | (Orientation.WEST, Direction.BACKWARD)
            ):
                return (
                    Coordinates(x=position.x + INCREMENT, y=position.y),
                    Orientation.EAST,
                )
            case (Orientation.SOUTH, Direction.RIGHT) | (
                Orientation.WEST,
                Direction.FORWARD,
            ):
                return (
                    Coordinates(x=position.x + INCREMENT, y=position.y),
                    Orientation.WEST,
                )

            case (Orientation.NORTH, Direction.LEFT) | (
                Orientation.EAST,
                Direction.BACKWARD,
            ):
                return (
                    Coordinates(x=position.x - DECREMENT, y=position.y),
                    Orientation.WEST,
                )

            case (Orientation.NORTH, Direction.RIGHT):
                return (
                    Coordinates(x=position.x + INCREMENT, y=position.y),
                    Orientation.EAST,
                )

            case (Orientation.NORTH, Direction.BACKWARD):
                return (
                    Coordinates(x=position.x, y=position.x - DECREMENT),
                    Orientation.SOUTH,
                )

            case _:
                raise Exception(
                    "Unable to create coordinates and orientation direction"
                )

    def get_plan(
        self, *, directions: str, position: Coordinates, orientation: Orientation
    ) -> Sequence[Step]:
        """
        Return a list steps that represent a plan of how step through the directions.
        """
        steps = []
        for direction in directions:
            coordinates, orientation = self.get_coordinates_and_orientation(
                direction=Direction(direction),
                position=position,
                orientation=orientation,
            )
            step = Step(
                destination=coordinates,
                orientation=orientation,
                direction=Direction(direction),
            )
            steps.append(step)
            # Overwrite `position` and `orientation` to use new values in the next iteration.
            position = step.destination
            orientation = step.orientation

        return steps

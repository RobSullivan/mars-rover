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

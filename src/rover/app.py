from collections.abc import Iterable

from rover import gps as rover_gps
from rover import robot as rover_robot
from rover import surface as rover_surface


def run(rows: int, columns: int, commands: Iterable) -> None:
    # TODO: write a small cli to do this. Until then this is hardcoded expectation of how the commands
    # are submitted
    starting_position, directions = commands
    x, y, orientation = starting_position

    surface = rover_surface.Surface(rows=rows, columns=columns)
    gps = rover_gps.Gps(surface=surface)
    robot = rover_robot.Robot(
        gps=gps,
        starting_position=rover_gps.Coordinates(x=x, y=y),
        orientation=rover_gps.Orientation(orientation),
    )
    robot.start(directions=directions, gps=gps)
    report = robot.report()
    print(report)

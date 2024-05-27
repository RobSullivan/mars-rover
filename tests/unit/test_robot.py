from rover import gps as rover_gps
from rover import robot as rover_robot


class TestRobot:

    def test_init_robot(self):
        robot = rover_robot.Robot(
            gps=object,
            starting_position=rover_gps.Coordinates(x=0, y=0),
            orientation=rover_gps.Orientation.NORTH,
        )
        assert robot.starting_position
        assert robot.orientation
        assert robot.status.value == "IDLE"
        assert len(robot.steps) == 0

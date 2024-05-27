from rover import gps as rover_gps
from rover import robot as rover_robot
from rover import surface as rover_surface


class TestRobot:

    def test_robot_step(self):

        start_position = rover_gps.Coordinates(x=0, y=0)
        final_step = rover_gps.Step(
            destination=rover_gps.Coordinates(x=0, y=1),
            orientation=rover_gps.Orientation.NORTH,
            direction="F",
        )
        surface = rover_surface.Surface(rows=3, columns=3)
        gps = rover_gps.Gps(surface=surface)
        robot = rover_robot.Robot(
            gps=gps,
            starting_position=start_position,
            orientation=rover_gps.Orientation.NORTH,
        )

        robot.start(directions="F", gps=gps)

        assert robot.steps[-1].destination == final_step.destination
        assert robot.orientation == final_step.orientation
        assert len(robot.steps) == 1

    def test_robot_steps(self):
        """
        Test more steps
        """
        surface = rover_surface.Surface(rows=3, columns=3)
        gps = rover_gps.Gps(surface=surface)
        robot = rover_robot.Robot(
            gps=gps,
            starting_position=rover_gps.Coordinates(x=0, y=0),
            orientation=rover_gps.Orientation.NORTH,
        )

        final_step = rover_gps.Step(
            destination=rover_gps.Coordinates(x=3, y=3),
            orientation=rover_gps.Orientation.NORTH,
            direction="L",
        )

        directions = "FFRFFL"
        robot.start(directions=directions, gps=gps)

        assert robot.steps[-1].destination == final_step.destination
        assert robot.orientation == final_step.orientation
        assert robot.steps == [
            rover_gps.Step(
                destination=rover_gps.Coordinates(x=0, y=1),
                orientation=rover_gps.Orientation.NORTH,
                direction=rover_gps.Direction.FORWARD,
            ),
            rover_gps.Step(
                destination=rover_gps.Coordinates(x=0, y=2),
                orientation=rover_gps.Orientation.NORTH,
                direction=rover_gps.Direction.FORWARD,
            ),
            rover_gps.Step(
                destination=rover_gps.Coordinates(x=1, y=2),
                orientation=rover_gps.Orientation.EAST,
                direction=rover_gps.Direction.RIGHT,
            ),
            rover_gps.Step(
                destination=rover_gps.Coordinates(x=2, y=2),
                orientation=rover_gps.Orientation.EAST,
                direction=rover_gps.Direction.FORWARD,
            ),
            rover_gps.Step(
                destination=rover_gps.Coordinates(x=3, y=2),
                orientation=rover_gps.Orientation.EAST,
                direction=rover_gps.Direction.FORWARD,
            ),
            rover_gps.Step(
                destination=rover_gps.Coordinates(x=3, y=3),
                orientation=rover_gps.Orientation.NORTH,
                direction=rover_gps.Direction.LEFT,
            ),
        ]

    def test_lost_robot(self):
        """
        Test that a robot oversteps the boundary and is LOST
        """
        surface = rover_surface.Surface(rows=3, columns=3)
        gps = rover_gps.Gps(surface=surface)
        robot = rover_robot.Robot(
            gps=gps,
            starting_position=rover_gps.Coordinates(x=0, y=0),
            orientation=rover_gps.Orientation.NORTH,
        )

        directions = "FFFF"
        robot.start(directions=directions, gps=gps)
        assert robot.report() == "(0, 3, N) LOST"
        # Check the steps the Robot did make have been recorded
        expected_steps = [
            rover_gps.Step(
                destination=rover_gps.Coordinates(x=0, y=1),
                orientation=rover_gps.Orientation.NORTH,
                direction=rover_gps.Direction.FORWARD,
            ),
            rover_gps.Step(
                destination=rover_gps.Coordinates(x=0, y=2),
                orientation=rover_gps.Orientation.NORTH,
                direction=rover_gps.Direction.FORWARD,
            ),
            rover_gps.Step(
                destination=rover_gps.Coordinates(x=0, y=3),
                orientation=rover_gps.Orientation.NORTH,
                direction=rover_gps.Direction.FORWARD,
            ),
        ]
        assert robot.steps == expected_steps

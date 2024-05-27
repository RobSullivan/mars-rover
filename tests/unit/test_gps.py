import pytest
from rover import gps as rover_gps


class TestGps:

    def test_init_gps(self):
        surface = object
        gps = rover_gps.Gps(surface=surface)
        assert gps.surface
    
    @pytest.mark.parametrize(
        "current_orientation, direction, expected_coordinates, expected_orientation",
        [
            (
                rover_gps.Orientation.NORTH,
                rover_gps.Direction.FORWARD,
                rover_gps.Coordinates(x=0, y=1),
                rover_gps.Orientation.NORTH,
            ),
            (
                rover_gps.Orientation.NORTH,
                rover_gps.Direction.LEFT,
                rover_gps.Coordinates(x=-1, y=0),
                rover_gps.Orientation.WEST,
            ),
            (
                rover_gps.Orientation.NORTH,
                rover_gps.Direction.RIGHT,
                rover_gps.Coordinates(x=1, y=0),
                rover_gps.Orientation.EAST,
            ),
            (
                rover_gps.Orientation.NORTH,
                rover_gps.Direction.BACKWARD,
                rover_gps.Coordinates(x=0, y=-1),
                rover_gps.Orientation.SOUTH,
            ),
            (
                rover_gps.Orientation.SOUTH,
                rover_gps.Direction.FORWARD,
                rover_gps.Coordinates(x=0, y=-1),
                rover_gps.Orientation.SOUTH,
            ),
            (
                rover_gps.Orientation.SOUTH,
                rover_gps.Direction.LEFT,
                rover_gps.Coordinates(x=+1, y=0),
                rover_gps.Orientation.EAST,
            ),
            (
                rover_gps.Orientation.SOUTH,
                rover_gps.Direction.RIGHT,
                rover_gps.Coordinates(x=1, y=0),
                rover_gps.Orientation.WEST,
            ),
            (
                rover_gps.Orientation.SOUTH,
                rover_gps.Direction.BACKWARD,
                rover_gps.Coordinates(x=0, y=1),
                rover_gps.Orientation.NORTH,
            ),
            (
                rover_gps.Orientation.EAST,
                rover_gps.Direction.FORWARD,
                rover_gps.Coordinates(x=+1, y=0),
                rover_gps.Orientation.EAST,
            ),
            (
                rover_gps.Orientation.EAST,
                rover_gps.Direction.LEFT,
                rover_gps.Coordinates(x=0, y=1),
                rover_gps.Orientation.NORTH,
            ),
            (
                rover_gps.Orientation.EAST,
                rover_gps.Direction.RIGHT,
                rover_gps.Coordinates(x=0, y=-1),
                rover_gps.Orientation.SOUTH,
            ),
            (
                rover_gps.Orientation.EAST,
                rover_gps.Direction.BACKWARD,
                rover_gps.Coordinates(x=-1, y=0),
                rover_gps.Orientation.WEST,
            ),
            (
                rover_gps.Orientation.WEST,
                rover_gps.Direction.FORWARD,
                rover_gps.Coordinates(x=1, y=0),
                rover_gps.Orientation.WEST,
            ),
            (
                rover_gps.Orientation.WEST,
                rover_gps.Direction.LEFT,
                rover_gps.Coordinates(x=0, y=-1),
                rover_gps.Orientation.SOUTH,
            ),
            (
                rover_gps.Orientation.WEST,
                rover_gps.Direction.RIGHT,
                rover_gps.Coordinates(x=0, y=1),
                rover_gps.Orientation.NORTH,
            ),
            (
                rover_gps.Orientation.WEST,
                rover_gps.Direction.BACKWARD,
                rover_gps.Coordinates(x=+1, y=0),
                rover_gps.Orientation.EAST,
            ),
        ],
    )
    def test_get_coordinates_and_orientation(
        self, current_orientation, direction, expected_coordinates, expected_orientation
    ):
        gps = rover_gps.Gps(surface=object)
        actual_coordinates, actual_orientation = gps.get_coordinates_and_orientation(
            direction=direction,
            position=rover_gps.Coordinates(x=0, y=0),
            orientation=current_orientation,
        )
        assert actual_coordinates == expected_coordinates
        assert actual_orientation == expected_orientation

import pytest

from rover import gps as rover_gps
from rover import surface as rover_surface


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

    def test_get_steps(self):
        """
        Given some directions, a start position and start orientation
        generate a "plan", or sequence of steps.
        """
        start_position = rover_gps.Coordinates(x=0, y=0)
        start_orientation = rover_gps.Orientation.NORTH

        directions = "FFRFFL"

        gps = rover_gps.Gps(surface=object)
        actual_steps = gps.get_plan(
            directions=directions,
            position=start_position,
            orientation=start_orientation,
        )

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

        assert actual_steps == expected_steps

    def test_destination_is_available(self):
        rows = 2
        columns = 2
        surface = rover_surface.Surface(rows=rows, columns=columns)
        gps = rover_gps.Gps(surface=surface)

        gps.destination_available(rover_gps.Coordinates(x=2, y=1))

    def test_destination_is_not_available(self):
        rows = 2
        columns = 2
        surface = rover_surface.Surface(rows=rows, columns=columns)
        gps = rover_gps.Gps(surface=surface)

        with pytest.raises(rover_gps.OutOfBounds):
            gps.destination_available(rover_gps.Coordinates(x=2, y=3))

    @pytest.mark.parametrize(
        "coordinates",
        [
            rover_gps.Coordinates(x=0, y=0),
            rover_gps.Coordinates(x=1, y=3),
            rover_gps.Coordinates(x=2, y=4),
            rover_gps.Coordinates(x=4, y=5),
        ],
    )
    def test_valid_coordinates(self, coordinates):
        """
        Test the gps returns valid coordinates

        i.e. it takes into account the boundaries of the surface.
        """
        rows = 4
        columns = 5
        surface = rover_surface.Surface(rows=rows, columns=columns)

        gps = rover_gps.Gps(surface=surface)

        assert not gps.out_of_bounds(coordinates)

    @pytest.mark.parametrize(
        "coordinates",
        [
            rover_gps.Coordinates(x=-1, y=0),
            rover_gps.Coordinates(x=1, y=-3),
            rover_gps.Coordinates(x=5, y=4),
            rover_gps.Coordinates(x=4, y=6),
        ],
    )
    def test_invalid_coordinates(self, coordinates):
        """
        Test the gps returns valid coordinates

        i.e. it takes into account the boundaries of the surface.
        """
        rows = 4
        columns = 5
        surface = rover_surface.Surface(rows=rows, columns=columns)

        gps = rover_gps.Gps(surface=surface)

        assert gps.out_of_bounds(coordinates)

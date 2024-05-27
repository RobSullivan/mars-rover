from rover import gps as rover_gps


class TestGps:

    def test_init_gps(self):
        surface = object
        gps = rover_gps.Gps(surface=surface)
        assert gps.surface

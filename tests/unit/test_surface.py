from rover import surface as rover_surface


def test_init_surface():
    rows = 4
    columns = 5
    surface = rover_surface.Surface(rows=rows, columns=columns)
    assert not surface.robots

    assert surface.rows == rows
    assert surface.columns == columns

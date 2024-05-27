from rover import app


def test_successful_rovering(capsys):
    commands = [(0, 0, "E"), "FFF"]
    app.run(rows=3, columns=3, commands=commands)
    captured = capsys.readouterr()
    assert captured.out == "(3, 0, E) ACTIVE\n"


def test_unsuccessful_rovering(capsys):
    commands = [(0, 0, "E"), "FFFF"]
    app.run(rows=3, columns=3, commands=commands)
    captured = capsys.readouterr()
    assert captured.out == "(3, 0, E) LOST\n"
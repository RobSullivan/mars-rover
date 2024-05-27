from rover import app

def test_app():
    assert app.hello_world() == "Hello, World!"

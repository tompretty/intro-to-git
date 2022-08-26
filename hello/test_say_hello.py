from .say_hello import say_hello


def test_say_hello_says_hello():
    first_name = "Tom"

    greeting = say_hello(first_name)

    assert greeting == "Hello, Tom"

from .say_hello import say_hello


def test_say_hello_says_hello():
    first_name = "Tom"
    
    greeting = say_hello(first_name)

    assert greeting == "Hello, Tom"
def test_say_hello_with_lastname():
    first_name = "Jaya"
    last_name = "Shakespeare"
    greeting = say_hello(first_name, last_name)
    assert greeting == "Hello, Jaya Shakespeare"

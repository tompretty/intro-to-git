def say_hello(first_name, last_name= ""):
    return f"Hello, {first_name} {last_name}" if last_name != "" else f"Hello, {first_name}"
if __name__ == '__main__':
    print(say_hello("Tom"))

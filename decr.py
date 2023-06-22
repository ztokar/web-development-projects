def fancy_adder(function):
    def wrapper_func():
        print("Hello")
        function()
        print("bye")
    return wrapper_func

@fancy_adder
def intro():
    return print("Welcome")


fancy_adder()
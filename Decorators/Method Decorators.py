def method_decorator(func):
    def wrapper(self, *args):
        print("Before method execution")
        res = func(self, * args)
        print("After method execution")
        return res
    return wrapper

class MyClass:
    @method_decorator
    def say_hello(self):
        print("Hello!")

obj = MyClass()
obj.say_hello()
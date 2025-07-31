def my_decorator(func):
    def wrapper():
        print("Decorator >>")
        func()
        print("Decorator <<")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")
    
print(say_whee())
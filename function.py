# add double line break after the function
def say_hello():
    print("Hello World!")
    print("How are you doing today?")


say_hello();


def hello_to_user(name):
    print(f"Hello {name}")


hello_to_user('John')


# key word argument

def greet_john(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")


greet_john('Smith', 'John')

greet_john(last_name='Smith', first_name='John')


def square(num):
    return num * num


print(square(4))

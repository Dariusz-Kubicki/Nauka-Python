# Definicja funkcji
def greet():
    print("Hi there!")
    print("Welcome aboard!")


# Wywołanie funkcji
greet()


# Definicja funkcji z parametrami
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard!")


# Wywołanie funkcji z argumentami
greet("Dariusz", "Kubicki")

# Funkcja z wartością zwracaną
def get_greeting(name):
    return f"Hi {name}!"


message = get_greeting("Dariusz")


def increment(number, by):
    return number + by


print(increment(2, by=1))

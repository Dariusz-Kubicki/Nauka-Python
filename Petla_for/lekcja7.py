# pętla for
for number in range(1, 10, 2):  # range(start, stop, step)
    print("Attempt", number, number * ".")

successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful!")
        break   # Przerywa pętlę, jeśli warunek jest spełniony
# Ten blok zostanie wykonany tylko wtedy, gdy pętla zakończy się normalnie (bez break)
else:
    print("Attempted 3 times and failed!")

for x in range(5):  # Zewnętrzna pętla iterująca po x
    for y in range(3):  # Wewnętrzna pętla iterująca po y
        print(f"({x}, {y})")

print(type(5))         # <class 'int'>
print(type(range(5)))  # <class 'range'>

# range jest iteratorem, który generuje liczby na żądanie, co jest bardziej efektywne pamięciowo niż tworzenie listy wszystkich liczb od razu.

print(list(range(5)))  # [0, 1, 2, 3, 4]

for x in "Python":  # Iteracja po każdym znaku w stringu
    print(x)

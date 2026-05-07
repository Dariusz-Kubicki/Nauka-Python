is_sunny = True         # Zmienna typu boolean (True lub False)

if is_sunny:            # Jeśli warunek jest prawdziwy (True)
    print("Jest słonecznie!")  # Ten kod wykona się tylko dla True

print("Koniec sprawdzania")    # Ten kod wykona się zawsze, bo nie ma wcięcia


a = 21
b = 37

print(a > b)   # Większe: False
print(a < b)   # Mniejsze: True
print(a == b)  # Równe (operator porównania): False
print(a != b)  # Różne (nierówne): True
print(a >= b)  # Większe lub równe: False
print(a <= b)  # Mniejsze lub równe: True


# Struktura if-elif-else
if a > b:
    print("a jest większe niż b")
elif a < b:
    print("a jest mniejsze niż b")
else:
    print("a i b są równe")


temperature = 35

if temperature > 30:
    print("Jest gorąco!")
elif temperature > 20:
    print("Jest przyjemnie.")
elif temperature > 10:
    print("Jest chłodno.")
else:
    print("Jest zimno.")


age = 22

# Wersja 1: Klasyczna (rozbudowana)
if age >= 18:
    print("Pełnoletni")
else:
    print("Niepełnoletni")

# Wersja 2: Przypisanie do zmiennej w bloku
if age >= 18:
    message = "Pełnoletni"
else:
    message = "Niepełnoletni"
print(message)

# Wersja 3: Operator trójargumentowy (najbardziej "pythonowy" zapis)
message = "Pełnoletni" if age >= 18 else "Niepełnoletni"
print(message)

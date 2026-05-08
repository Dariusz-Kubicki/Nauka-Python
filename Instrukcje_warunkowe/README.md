# Lekcja 5: Instrukcje warunkowe
W tej lekcji poznałem mechanizm działania instrukcji warunkowej `if` oraz dowiedziałem się, jak stosować ją w praktyce do sterowania przepływem programu.

### Instrukcja `if`
Instrukcja warunkowa `if` wykonuje przypisany do niej blok kodu tylko wtedy, gdy podany warunek ma wartość logiczną `True`. Jeśli warunek wynosi `False`, kod zostaje pominięty.

Ważnym elementem w Pythonie jest wcięcie (indentacja) – to ono definiuje, który fragment kodu należy do instrukcji `if` (tzw. ciało instrukcji).

```Python
is_sunny = True         # Zmienna typu boolean (True lub False)

if is_sunny:            # Jeśli warunek jest prawdziwy (True)
    print("Jest słonecznie!")  # Ten kod wykona się tylko dla True
    
print("Koniec sprawdzania")    # Ten kod wykona się zawsze, bo nie ma wcięcia
```

---

### Operatory porównania
Rzadko wpisujemy `True` lub `False` ręcznie. Zazwyczaj generujemy je dynamicznie za pomocą **operatorów porównania**. Pozwalają one na zestawienie dwóch wartości:

```Python
a = 21
b = 37

print(a > b)   # Większe: False
print(a < b)   # Mniejsze: True
print(a == b)  # Równe (operator porównania): False
print(a != b)  # Różne (nierówne): True
print(a >= b)  # Większe lub równe: False
print(a <= b)  # Mniejsze lub równe: True
```

---

### Obsługa wielu warunków: `elif` oraz `else`
Gdy chcemy sprawdzić więcej możliwości lub zdefiniować zachowanie domyślne, używamy instrukcji `elif` (skrót od else if) oraz `else`.
- `if`: Sprawdzany jako pierwszy (może być tylko jeden w danej strukturze).
- `elif`: Sprawdzany tylko, jeśli poprzednie warunki nie zostały spełnione (może być ich wiele).
- `else`: Wykonywany na samym końcu, jeśli żaden z powyższych warunków nie był prawdziwy (może być tylko jeden).

```Python
# Struktura if-elif-else
if a > b:
    print("a jest większe niż b")
elif a < b:
    print("a jest mniejsze niż b")
else:
    print("a i b są równe")
```

---

### Praktyczny przykład: Klasyfikacja temperatury
Poniższy kod pokazuje, jak w praktyce można wykorzystać drabinkę instrukcji warunkowych do interpretacji danych:

```Python
temperature = 35

if temperature > 30:
    print("Jest gorąco!")
elif temperature > 20:
    print("Jest przyjemnie.")
elif temperature > 10:
    print("Jest chłodno.")
else:
    print("Jest zimno.")
```

---

### Optymalizacja kodu i Operator Trójargumentowy
Dążąc do tego, aby kod w Pythonie był jak najbardziej czytelny i zwięzły (zgodnie z zasadą Pythonic way), możemy zapisać proste warunki w jednej linii.

Wersja 1 i 2 to klasyczne podejście, ale profesjonaliści w przypadku bardzo prostych przypisań często wybierają wersję 3, czyli **operator trójargumentowy** (ternary operator).

```Python
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
```

# Lekcja 9: Funkcje

Wcześniej używaliśmy gotowych, wbudowanych funkcji, takich jak `print()` czy `round()`. W tej lekcji nauczymy się definiować własne funkcje i dowiemy się, jak ich używać w praktyce.

### Czym jest funkcja?
Funkcja to fragment kodu, który wykonuje określone działanie lub obliczenia. Możemy odwoływać się do niej dowolną liczbę razy. Funkcje są szczególnie przydatne w większych projektach – pozwalają podzielić kod składający się z setek linii na pojedyncze, logiczne części odpowiedzialne za konkretne zadania. Dzięki temu kod staje się przejrzysty i łatwiejszy do zrozumienia.

---

### Definicja i wywołanie funkcji
Aby zdefiniować funkcję, musimy użyć słowa kluczowego `def` (z ang. *define*), a następnie nadać jej nazwę. Zasady nazywania funkcji są takie same jak przy zmiennych, z tą różnicą, że na końcu muszą pojawić się nawiasy okrągłe `()`. 

Sama definicja funkcji to tylko instrukcja – aby kod w środku zadziałał, musimy ją wywołać. Wywołanie polega na wpisaniu nazwy funkcji wraz z nawiasami.

```python
# Definicja funkcji
def greet():
    print("Hi there!")
    print("Welcome aboard!")

# Wywołanie funkcji
greet()
```

---

### Parametry i argumenty funkcji
Funkcje mogą przyjmować dane, na których wykonują operacje. 
* **Parametry** to zmienne, które zapisujemy w nawiasach podczas definiowania funkcji.
* **Argumenty** to konkretne wartości, które przekazujemy do funkcji w momencie jej wywołania.

```python
# Definicja funkcji z parametrami
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard!")

# Wywołanie funkcji z argumentami
greet("Dariusz", "Kubicki")
```

---

### Wartości domyślne (Argumenty opcjonalne)
Możemy sprawić, że dany parametr będzie opcjonalny, przypisując mu **wartość domyślną**. Jeśli podczas wywołania nie podamy tego argumentu, Python użyje wartości domyślnej. 

**Ważne:** Parametry z wartościami domyślnymi muszą zawsze znajdować się na końcu listy parametrów.

```python
def increment(number, by=1):
    return number + by

print(increment(2))      # Wynik: 3 (użyto domyślnego by=1)
print(increment(2, 5))   # Wynik: 7 (nadpisano domyślną wartość)
```

---

### Dowolna liczba argumentów (*args)
Czasami nie wiemy dokładnie, ile danych będziemy chcieli przekazać do funkcji. W Pythonie możemy użyć operatora `*` (często nazywanego **xargs**). Dzięki niemu funkcja przyjmie dowolną liczbę argumentów, które zostaną potraktowane jako krotka (tuple), po której możemy iterować pętlą.

```python
# Funkcja mnożąca wszystkie podane liczby
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

# Możemy podać 2, 4 lub 10 argumentów – funkcja zadziała zawsze
print(multiply(2, 3, 4, 5))
```

---

### Funkcja z wartością zwracaną
Funkcje mogą nie tylko wykonywać polecenia, ale też zwracać wynik do dalszego wykorzystania za pomocą słowa kluczowego `return`. Pamiętaj, że `return` natychmiast przerywa działanie funkcji.

```python
def get_greeting(name):
    return f"Hi {name}!"

message = get_greeting("Dariusz")
print(message)
```

---

### Opisywanie argumentów (Keyword Arguments)
Podczas wywoływania funkcji możemy jawnie wskazać nazwę parametru. Zwiększa to czytelność kodu, zwłaszcza gdy funkcja przyjmuje wiele parametrów i nie chcemy pomylić ich kolejności.

```python
def increment(number, by):
    return number + by

# Wywołanie z nazwanym argumentem 'by'
print(increment(2, by=1))
```

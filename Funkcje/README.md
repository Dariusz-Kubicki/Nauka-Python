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

Poniżej przykład funkcji przyjmującej dwa parametry:

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
Możemy sprawić, że dany parametr będzie opcjonalny. Robimy to poprzez przypisanie mu **wartości domyślnej** już na etapie definicji funkcji. Jeśli podczas wywołania nie podamy tego argumentu, Python użyje wartości domyślnej. Jeśli go podamy – stara wartość zostanie nadpisana nową.

**Ważne:** Parametry z wartościami domyślnymi muszą zawsze znajdować się na końcu listy parametrów.

```python
# 'by' ma domyślną wartość 1
def increment(number, by=1):
    return number + by

# Użycie wartości domyślnej (wynik: 3)
print(increment(2))

# Nadpisanie wartości domyślnej własnym argumentem (wynik: 7)
print(increment(2, 5))
```

---

### Funkcja z wartością zwracaną
Do tej pory funkcje wykonywały tylko polecenia (np. wypisywanie tekstu). Teraz napiszemy funkcję, która przetworzy dane i zwróci nam gotowy wynik za pomocą słowa kluczowego `return`. Wartość tę możemy później zapisać do zmiennej.

```python
# Funkcja z wartością zwracaną
def get_greeting(name):
    return f"Hi {name}!"

# Przypisanie wyniku funkcji do zmiennej
message = get_greeting("Dariusz")
print(message)
```

---

### Opisywanie argumentów (Argumenty słownikowe)
W Pythonie możemy podczas wywoływania funkcji przypisać wartość bezpośrednio do nazwy parametru (`keyword arguments`). Jest to bardzo przydatne w dużych projektach, gdy chcemy, aby kod był bardziej czytelny i jasny dla innych programistów.

```python
def increment(number, by):
    return number + by

# Używamy nazwy parametru 'by', aby wyjaśnić, co robi ta wartość
print(increment(2, by=1))
```

```

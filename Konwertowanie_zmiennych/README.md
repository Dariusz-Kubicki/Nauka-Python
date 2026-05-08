# Lekcja 4: Konwertowanie zmiennych
W tej lekcji dowiedziałem się, jak odbierać dane od użytkownika oraz jak konwertować zmienne (rzutowanie typów), np. z typu `str` na `int`.

### Pobieranie wartości od użytkownika
W Pythonie do interakcji z użytkownikiem służy funkcja `input()`. Pozwala ona na wprowadzenie danych, które następnie możemy wykorzystać w programie.

Spójrzmy na przykład, w którym chcemy pobrać liczbę, dodać do niej 1 i wyświetlić wynik:

```Python
x = input("x: ")  # Pobieramy wartość od użytkownika i przypisujemy ją do zmiennej x.
y = x + 1         # To spowoduje błąd (TypeError)!
print(y)
```

**Dlaczego pojawia się błąd?**
Domyślnie funkcja `input()` zawsze zwraca dane jako tekst (string), nawet jeśli użytkownik wpisze cyfrę. Nie można wykonać operacji matematycznej na tekście i liczbie jednocześnie.

```Python
x = input("x: ") 
print(type(x))    # Wynik: <class 'str'>
```

---

### Przykłady konwersji typów danych
Aby wykonać obliczenia, musimy zmienić typ zmiennej. Służą do tego wbudowane funkcje:
- `int(x)` – konwertuje na liczbę całkowitą.
- `float(x)` – konwertuje na liczbę zmiennoprzecinkową (z kropką).
- `bool(x)` – konwertuje na wartość logiczną (`True`/`False`).
- `str(x)` – konwertuje dowolny typ na tekst.

**Ważne:** Konwersja na `int` lub `float` powiedzie się tylko wtedy, gdy string zawiera znaki będące liczbami. Próba zamiany tekstu `"abc"` na liczbę zakończy się błędem `ValueError`.

---

### Poprawiony kod z konwersją
Dzięki zastosowaniu funkcji `int()`, nasz poprzedni przykład będzie działał bez zarzutu:

```Python
x = input("x: ")             # Pobieramy tekst (np. "5")
y = int(x) + 1               # Konwertujemy tekst na liczbę i dodajemy 1
print(f"x: {x}, y: {y}")     # Wynik: x: 5, y: 6
```

---

### Specyfika konwersji na Boolean (wartość logiczną)
Konwersja na typ `bool` w Pythonie jest bardzo ciekawa. Większość obiektów jest uznawana za `True`, chyba że są "puste" lub równe zero.

```Python
# Co zwraca True, a co False?
print(f"bool('') = {bool('')}")                  # Pusty string -> False
print(f"bool('Hello') = {bool('Hello')}")        # Niepusty string -> True
print(f"bool(0) = {bool(0)}")                    # Zero -> False
print(f"bool(1) = {bool(1)}")                    # Każda inna liczba -> True
print(f"bool([]) = {bool([])}")                  # Pusta lista -> False
print(f"bool(None) = {bool(None)}")              # Brak wartości -> False
```

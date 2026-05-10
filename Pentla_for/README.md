# Lekcja 7: Pętla for

Pętla `for` służy do powtarzania określonych czynności zadaną liczbę razy lub dla każdego elementu w obiekcie iterowalnym (np. w tekście, liście czy krotce). Pozwala ona na znaczną oszczędność kodu – zamiast pisać 100 razy tę samą komendę, możemy użyć pętli, która wykona to zadanie za nas w zaledwie dwóch linijkach.

### Funkcja `range()` i składnia pętli
Podstawowym narzędziem współpracującym z pętlą `for` jest funkcja `range()`. Pozwala ona kontrolować liczbę powtórzeń oraz wartości generowane w każdym kroku.

| Argument | Nazwa | Opis |
| :--- | :--- | :--- |
| `start` | **Początek** | Wartość, od której zaczynamy (domyślnie 0). |
| `stop` | **Koniec** | Wartość, na której kończymy (**nie jest wliczana** do wyniku). |
| `step` | **Krok** | Wartość, o którą zwiększamy licznik w każdej iteracji (domyślnie 1). |

**Przykład z użyciem wszystkich argumentów:**
```python
# Generuje liczby: 1, 3, 5, 7, 9
for number in range(1, 10, 2):
    # number * "." mnoży ciąg znaków przez liczbę, tworząc odpowiednią liczbę kropek
    print("Próba", number, number * ".")
```

---

### Mechanizm `for ... else` oraz instrukcja `break`
Pętla `for` w Pythonie posiada unikalną cechę – blok `else`. Jest on wykonywany tylko wtedy, gdy pętla przejdzie przez wszystkie kroki i **nie zostanie przerwana** instrukcją `break`. Jeśli pętla zostanie przerwana wcześniej, blok `else` zostanie pominięty.

```python
successful = True
for number in range(3):
    print("Próba...")
    if successful:
        print("Sukces!")
        break  # Natychmiast przerywa pętlę, blok 'else' zostanie pominięty
else:
    # Ten kod wykona się tylko, jeśli pętla dojdzie do końca bez instrukcji 'break'
    print("Wykonano 3 próby i nie udało się!")
```

---

### Pętle zagnieżdżone (Nested Loops)
Możemy umieścić jedną pętlę wewnątrz drugiej. Jest to szczególnie przydatne przy pracy ze strukturami wielowymiarowymi, takimi jak tabele, macierze czy współrzędne.

```python
for x in range(5):      # Pętla zewnętrzna
    for y in range(3):  # Pętla wewnętrzna (wykona się w całości dla każdego kroku x)
        print(f"Współrzędne: ({x}, {y})")
```

---

### Obiekty iterowalne (Iterables)
Pętla `for` nie ogranicza się tylko do liczb generowanych przez `range()`. Może ona przechodzić przez dowolny obiekt, który jest **iterowalny** (czyli taki, z którego można pobierać elementy jeden po drugim).

* **Stringi:** Możemy iterować po każdym znaku w tekście.
* **Listy i krotki:** Możemy przechodzić przez elementy zbiorów danych.

```python
# Iteracja po znakach ciągu tekstowego
for letter in "Python":
    print(letter)
```

---

### Efektywność pamięciowa: Czym jest `range`?
Warto wiedzieć, że w Pythonie 3 `range` nie jest listą, lecz specjalnym typem obiektu (tzw. leniwym iteratorem).

```python
print(type(5))         # <class 'int'>
print(type(range(5)))  # <class 'range'>
```

> **Wskazówka:** `range` generuje liczby "na żądanie", zamiast przechowywać je wszystkie naraz w pamięci RAM. Jeśli stworzysz pętlę wykonującą się miliard razy, `range(1000000000)` zużyje minimalną ilość pamięci, podczas gdy lista z taką liczbą elementów mogłaby całkowicie zawiesić Twój komputer.

Jeśli chcesz zobaczyć wszystkie liczby naraz (np. w celu ich wypisania), możesz jawnie przekonwertować `range` na listę:
```python
print(list(range(5)))  # Wynik: [0, 1, 2, 3, 4]
```

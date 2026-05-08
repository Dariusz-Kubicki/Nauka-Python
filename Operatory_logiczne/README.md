
# Lekcja 6: Operatory logiczne
Niniejsza lekcja stanowi rozszerzenie tematu instrukcji warunkowych. Skupimy się w niej na **operatorach logicznych**, które pozwalają na budowanie bardziej złożonych i precyzyjnych testów logicznych w kodzie.

### Rodzaje operatorów logicznych
W Pythonie operatory logiczne są wyjątkowo intuicyjne, ponieważ zapisujemy je w formie angielskich słów, a nie symboli (jak np. `&&` czy `||` w języku C++ lub Java).

| Operator | Znaczenie | Opis |
| :--- | :--- | :--- |
| `and` | **I** (koniunkcja) | Zwraca `True`, jeśli **wszystkie** warunki są prawdziwe. |
| `or` | **LUB** (alternatywa) | Zwraca `True`, jeśli **przynajmniej jeden** z warunków jest prawdziwy. |
| `not` | **NIE** (negacja) | Odwraca wartość logiczną (z `True` na `False` i odwrotnie). |

---

### Praktyczne zastosowanie i priorytety
W jednej instrukcji warunkowej możemy łączyć wiele testów. W przypadku rozbudowanych wyrażeń, w których występują różne operatory, kluczową rolę odgrywa kolejność ich wykonywania oraz czytelność kodu. 
> **Wskazówka:** Aby zachować pełną kontrolę nad logiką i uniknąć błędów, warto używać **nawiasów okrągłych `()`**. Pozwalają one jasno określić priorytet sprawdzania warunków.

**Przykład: Weryfikacja zdolności kredytowej**

```python
# Dane wejściowe
high_income = True
good_credit = False
is_student = False

# Klient może otrzymać pożyczkę, jeśli posiada wysoki dochód LUB dobrą historię kredytową, 
# pod warunkiem, że NIE jest studentem.
if (high_income or good_credit) and not is_student:
    print("Decyzja: Klient może otrzymać pożyczkę")
else:
    print("Decyzja: Klient nie może otrzymać pożyczki")
```

---

### Mechanizm Short-circuiting
Python optymalizuje sprawdzanie warunków logicznych poprzez tzw. **short-circuiting** (krótkie cięcie). Oznacza to, że interpreter przerywa sprawdzanie kolejnych elementów wyrażenia, gdy tylko wynik całego wyrażenia jest już przesądzony:

- **Dla operatora** `and`: Jeśli pierwszy warunek to `False`, wynik całego wyrażenia musi być `False`. Pozostałe warunki są ignorowane.
- **Dla operatora** `or`: Jeśli pierwszy warunek to `True`, wynik całego wyrażenia musi być `True`. Reszta nie jest sprawdzana.

```Python
# Przykład short-circuiting dla 'and'
# Jeśli high_income będzie False, Python nie sprawdzi już reszty warunków.
if high_income and good_credit and not is_student:
    print("Warunki spełnione")
```

---

### Porównania łańcuchowe (Chained Comparison Operators)
Python oferuje bardzo elegancki sposób zapisu przedziałów liczbowych, zapożyczony bezpośrednio z notacji matematycznej. Zamiast łączyć dwa warunki operatorem `and`, możemy zapisać je w jednej linii.

```Python
age = 22

# Zapis tradycyjny z użyciem 'and':
# if age >= 18 and age < 65:

# Zapis łańcuchowy (bardziej czytelny i profesjonalny):
if 18 <= age < 65:
    print("Osoba jest w wieku produkcyjnym")
```

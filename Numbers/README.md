# Lekcja 3: Liczby
W tej lekcji poznałem podstwowe operatory arytmetyczne i ich skróconą wersję, funkcje wbudowane i modół math.

### Podstawowe operatory arytmetyczne
W Pythonie podstawowo mamy do dyspozycji dodawanie, odejmowanie, mnożenie, dzielenie, dzielenie całkowite, reszta z dzielenia i potęgowanie. poniżej podaję przykłady:
```Python
# Podstawowe operatory arytmetyczne
print(10 + 4)     # Dodawanie: 14
print(10 - 4)     # Odejmowanie: 6
print(10 * 4)     # Mnożenie: 40
print(10 / 4)     # Dzielenie: 2.5
print(10 // 4)    # Dzielenie całkowite: 2
print(10 % 4)     # Modulo (reszta z dzielenia): 2
print(10 ** 4)    # Potęgowanie: 10000
```

### Skrócone operacje arytmmetyczne
Aby ułatwić i pszyśpieszyć swoją pracę w Pythopnie mamy do dyspozycji skróconą formę operacji arytmetycznych np.
```Python
a = 2
a += 4  # Skrócona forma: a = a + 4
a -= 4  # Skrócona forma: a = a - 4
a *= 4  # Skrócona forma: a = a * 4
a /= 4  # Skrócona forma: a = a / 4
a //= 4  # Skrócona forma: a = a // 4
a %= 4  # Skrócona forma: a = a % 4
a **= 4  # Skrócona forma: a = a ** 4
```

### Funkcje wbudowane
Python posiada kilka funkcji wbudowanych pomagających nam z zagadnieniami matematycznymi. Poniżej przedstawiam część z nich:
```Python
# Funkcje wbudowane
print(round(2.9))  # Zaokrąglenie: 3
print(abs(-2.9))  # Wartość bezwzględna: 2.9
print(pow(2, 3))  # Potęgowanie: 8
print(max(1, 5, 3))  # Maksimum: 5 
print(min(1, 5, 3))  # Minimum: 1
print(sum([1, 2, 3]))  # Suma: 6
```

### Moduł math
Do naszego kodu możemy zaimportować dodatkowe rzeczy związane z matematyką na wysokim poziomie. Przydaje się to np. jak w przyszłości będę chciał zautomatyczować obliczenia do zadać z elektrotechniki lub przy większych projektach do przliczenia wyników (np. kąt lotu rakiety, wydajność silnika hybrydowego itp). Poniżej napisałem tylko kilka z metod które oferuje:
```Python
# Moduł math (więcej na https://docs.python.org/3/library/math.html)
print(math.ceil(2.1))  # Zaokrąglenie w górę: 3
print(math.floor(2.9))  # Zaokrąglenie w dół: 2
print(math.sqrt(16))  # Pierwiastek kwadratowy: 4.0
print(math.pi)  # Stała pi: 3.141592653589793
print(math.e)  # Stała e: 2.718281828459045
print(math.sin(math.pi / 2))  # Sinus 90 stopni: 1.0
```

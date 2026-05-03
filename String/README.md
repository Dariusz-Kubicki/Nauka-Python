# Lekcja 2: String
W tej lekcji przyjrzałem się bliżej typowi danych **String**. Dowiedziałem się, jak wyodrębniać znaki, liczyć długość ciągu, używać znaków ucieczki, formatować tekst oraz stosować przydatne metody.

### Wyodrębnianie znaków (Slicing)
W Pythonie możemy wycinać fragmenty tekstu za pomocą nawiasów kwadratowych i indeksów. Pamiętaj: **indeksowanie zaczyna się od 0**.

```Python
course = "Python Programming"
print(course[0])      # Pierwszy znak: 'P'
print(course[-1])     # Ostatni znak: 'g'
print(course[0:3])    # Znaki od 0 do 2 (3 jest wykluczone): 'Pyt'
print(course[0:])     # Od 0 do końca: 'Python Programming'
print(course[:3])     # Od początku do 2: 'Pyt'
print(course[:])      # Kopia całego ciągu
```

### Liczenie długości ciągu
Do liczenia znaków służy funkcja `len()`. Zwraca ona liczbę całkowitą (int).

```Python
course = "Python Programming"
print(len(course))    # Wypisze 18
```

### Znaki ucieczki (Escape Characters)
Jeśli chcemy użyć cudzysłowu wewnątrz tekstu ograniczonego cudzysłowem, musimy użyć **backslasha** (`\`). Dzięki temu Python wie, że to znak tekstu, a nie koniec zmiennej.

```Python
course = "Python \"Programming"  # Cudzysłów: \"
course = "Python \'Programming"  # Apostrof: \'
course = "Python \\Programming"  # Backslash: \\
course = "Python \nProgramming"  # Nowa linia: \n
```

### Formatowanie ciągów (f-strings)
Łączenie tekstów za pomocą `+` (konkatenacja) jest poprawne, ale mało czytelne. W Pythonie używamy **f-stringów**, które są znacznie bardziej eleganckie.

```Python
first = "Dariusz"
last = "Kubicki"
# Nowoczesny sposób (f-string)
full = f"{first} {last}"
print(full)
```
### Metody tekstowe
Stringi w Pythonie są obiektami, co daje nam dostęp do wielu wbudowanych metod (funkcji wywoływanych po kropce). **Ważne:** metody nie zmieniają oryginalnego ciągu (stringi są niemutowalne), lecz zwracają nową wartość.

```Python
course = "   PyThon proGramming   "
print(course.upper())            # Wszystkie litery wielkie
print(course.lower())            # Wszystkie litery małe
print(course.title())            # Wielka litera w każdym słowie
print(course.strip())            # Usuwa spacje z obu stron
print(course.find("pro"))        # Zwraca indeks początku frazy (lub -1)
print(course.replace("m", "g"))  # Zamienia znaki
print("pro" in course)           # Zwraca True, jeśli fraza istnieje w tekście
print("swift" not in course)     # Zwraca True, jeśli frazy nie ma w tekście
```

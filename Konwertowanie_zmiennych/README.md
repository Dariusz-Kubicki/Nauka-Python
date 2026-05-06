# Lekcja 4: Konwertowanie zmienncyh
W tej lekcji dowiedziałem się jak odbierać dane od użytkownika oraz jak konwertować zmienne np. z `str` do `int`.

### Pobieranie wartości od użytkownika:
W Pythonie możemy poprosić użytkownika o podanie danych do programu za pomocą funkcji `input()` np. żeby wpisał liczbę do której program ma dodać 1 i zwrócić wynik:

```Python
x = input("x : ")  # Pobieramy wartość od użytkownika i przypisujemy ją do zmiennej x.
y = x + 1          # To spowoduje błąd, ponieważ nie można dodać liczby (1) do stringa (x).
print(y)           # Nic nam się nie wyświetli
```

 Niestety bez odpowiedniego konwertowania nie uda nam się to, ponieważ funkcja `input()` zwraca zmienną String:
 
 ```Python
x = input("x : ") # Pobieramy wartość od użytkownika i przypisujemy ją do zmiennej x.
print(type(x))    # To pokaże, że x jest typu <class 'str'>
```

### Przykłady konwersji typów danych
Przekonwertować możemy prawie każdą zmienną przy użyciu odpowiednich funkcji. Poniżej podaję najważniejsze z nich:
```Python
# Przykład konwersji typów danych:
int(x) - konwertuje x na liczbę całkowitą
float(x) - konwertuje x na liczbę zmiennoprzecinkową
bool(x) - konwertuje x na wartość logiczną (True lub False)
str(x) - konwertuje x na string
```
Napisałem prawie każdą ponieważ funkcja `int()` lub `float()` konwertuje znaki String które są już liczbami tylko że zapisanymi w `str` czyli w zmiennej którą komputer nie czyta jako liczbę. Więc jeżeli będziemy chcieli przekonwertować zmienną `x = "abc"` na liczbę nie uda nam się to.

### Poprawiony kod z konwersją zmiennej
Dzięki konwertowaniu zmiennych możemy napisać działającą wersję poprzedniego kodu, oto ona:
```Python
# Poprawna konwersja z stringa na liczbę całkowitą
x = input("x : ")             # Pobieramy wartość od użytkownika i przypisujemy ją do zmiennej x.
y = int(x) + 1                # Teraz x jest konwertowane na int, więc możemy dodać 1
print(f"x: {x}, y: {y}")      # To pokaże poprawny wynik, np. jeśli użytkownik wpisał "5", to y będzie 6
```

### Konwersja z stringa na boolean
Wartośći logiczne w Pythonie cechują się swoją specjalną konwersją, poniżej podaję przykłady:
```Python
# Przykład konwersji z stringa na boolean
print(f"bool('') = {bool('')}")                  # Pusty string jest False
print(f"bool('Hello') = {bool('Hello')}")        # Niepusty string jest True
print(f"bool(0) = {bool(0)}")                    # Zero jest False
print(f"bool(1) = {bool(1)}")                    # Niezero jest True
print(f"bool([]) = {bool([])}")                  # Pusta lista jest False
print(f"bool([1, 2, 3]) = {bool([1, 2, 3])}")    # Niepusta lista jest True
print(f"bool(None) = {bool(None)}")              # None jest False
```


x = input("x : ")                                # Pobieramy wartość od użytkownika i przypisujemy ją do zmiennej x. Jednak input() zwraca string, więc x będzie typu string.
print(type(x))                                   # To pokaże, że x jest typu <class 'str'>
# y = x + 1                                        To spowoduje błąd, ponieważ nie można dodać liczby (1) do stringa (x).

# Przykład konwersji typów danych:
# int(x) - konwertuje x na liczbę całkowitą
# float(x) - konwertuje x na liczbę zmiennoprzecinkową
# bool(x) - konwertuje x na wartość logiczną (True lub False)
# str(x) - konwertuje x na string

# Poprawna konwersja z stringa na liczbę całkowitą
x = input("x : ")
y = int(x) + 1                                   # Teraz x jest konwertowane na int, więc możemy dodać 1
print(f"x: {x}, y: {y}")                         # To pokaże poprawny wynik, np. jeśli użytkownik wpisał "5", to y będzie 6

# Przykład konwersji z stringa na boolean
print(f"bool('') = {bool('')}")                  # Pusty string jest False
print(f"bool('Hello') = {bool('Hello')}")        # Niepusty string jest True
print(f"bool(0) = {bool(0)}")                    # Zero jest False
print(f"bool(1) = {bool(1)}")                    # Niezero jest True
print(f"bool([]) = {bool([])}")                  # Pusta lista jest False
print(f"bool([1, 2, 3]) = {bool([1, 2, 3])}")    # Niepusta lista jest True
print(f"bool(None) = {bool(None)}")              # None jest False

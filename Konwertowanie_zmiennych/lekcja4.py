x = input("x: ")  # Pobieramy wartość od użytkownika i przypisujemy ją do zmiennej x.
y = x + 1         # To spowoduje błąd (TypeError)!
print(y)

x = input("x: ") 
print(type(x))    # Wynik: <class 'str'>

# Przykład konwersji typów danych:
# int(x) - konwertuje x na liczbę całkowitą
# float(x) - konwertuje x na liczbę zmiennoprzecinkową
# bool(x) - konwertuje x na wartość logiczną (True lub False)
# str(x) - konwertuje x na string

# Poprawna konwersja z stringa na liczbę całkowitą
x = input("x: ")             # Pobieramy tekst (np. "5")
y = int(x) + 1               # Konwertujemy tekst na liczbę i dodajemy 1
print(f"x: {x}, y: {y}")     # Wynik: x: 5, y: 6

# Przykład konwersji z stringa na boolean
# Co zwraca True, a co False?
print(f"bool('') = {bool('')}")                  # Pusty string -> False
print(f"bool('Hello') = {bool('Hello')}")        # Niepusty string -> True
print(f"bool(0) = {bool(0)}")                    # Zero -> False
print(f"bool(1) = {bool(1)}")                    # Każda inna liczba -> True
print(f"bool([]) = {bool([])}")                  # Pusta lista -> False
print(f"bool(None) = {bool(None)}")              # Brak wartości -> False

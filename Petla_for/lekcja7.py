# Generuje liczby: 1, 3, 5, 7, 9
for number in range(1, 10, 2):
    # number * "." mnoży ciąg znaków przez liczbę, tworząc odpowiednią liczbę kropek
    print("Próba", number, number * ".")

successful = True
for number in range(3):
    print("Próba...")
    if successful:
        print("Sukces!")
        break  # Natychmiast przerywa pętlę, blok 'else' zostanie pominięty
else:
    # Ten kod wykona się tylko, jeśli pętla dojdzie do końca bez instrukcji 'break'
    print("Wykonano 3 próby i nie udało się!")

for x in range(5):      # Pętla zewnętrzna
    for y in range(3):  # Pętla wewnętrzna (wykona się w całości dla każdego kroku x)
        print(f"Współrzędne: ({x}, {y})")

# Iteracja po znakach ciągu tekstowego
for letter in "Python":
    print(letter)

print(type(5))         # <class 'int'>
print(type(range(5)))  # <class 'range'>

print(list(range(5)))  # Wynik: [0, 1, 2, 3, 4]

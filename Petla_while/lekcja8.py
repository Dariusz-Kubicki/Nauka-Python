number = 100

# Pętla będzie się wykonywać, dopóki wartość zmiennej 'number' jest większa od 0
while number > 0:
    print(number)
    # Zmniejszamy wartość o połowę przy użyciu dzielenia całkowitego (floor division)
    number //= 2

command = ""

# Warunek jest sprawdzany przed każdym wejściem do pętli
while command.lower() != "quit":
    command = input("> ")
    print("ECHO:", command)

while True:
    # Pobieramy dane bezpośrednio wewnątrz pętli
    command = input("> ")
    print("ECHO:", command)

    # Sprawdzamy warunek wyjścia; jeśli spełniony, natychmiast przerywamy pętlę
    if command.lower() == "quit":
        break

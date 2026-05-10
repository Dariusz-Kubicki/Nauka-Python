# Lekcja 8: Pętla while

W programowaniu często spotykamy sytuacje, w których nie wiemy z góry, ile razy dana operacja powinna zostać powtórzona. O ile pętla `for` idealnie sprawdza się przy iteracji po znanych zbiorach danych, o tyle pętla `while` jest niezastąpiona, gdy czas trwania operacji zależy od dynamicznie zmieniających się warunków.

### 1. Istota pętli while
Pętla `while` (z ang. „podczas gdy”) wykonuje blok instrukcji tak długo, jak długo zdefiniowany warunek logiczny zwraca wartość `True`. Przed każdym powtórzeniem program sprawdza, czy warunek nadal jest spełniony – jeśli przestanie być prawdziwy, pętla natychmiast kończy działanie.

```python
number = 100

# Pętla będzie się wykonywać, dopóki wartość zmiennej 'number' jest większa od 0
while number > 0:
    print(number)
    # Zmniejszamy wartość o połowę przy użyciu dzielenia całkowitego (floor division)
    number //= 2  
```

---

### 2. Interaktywne sterowanie przepływem
Siłą pętli `while` jest możliwość uzależnienia jej działania od danych wprowadzanych przez użytkownika w czasie rzeczywistym. Poniższy przykład ilustruje mechanizm, który przetwarza polecenia do momentu otrzymania komendy wyjścia.

```python
command = ""

# Warunek jest sprawdzany przed każdym wejściem do pętli
while command.lower() != "quit":
    command = input("> ")
    print("ECHO:", command)
```

---

### 3. Pętla nieskończona i instrukcja break
W profesjonalnym kodzie często stosuje się konstrukcję `while True`. Tworzy ona celową pętlę nieskończoną, której przerwanie następuje wewnątrz bloku kodu za pomocą słowa kluczowego `break`.

Takie podejście jest uznawane za zgodne z zasadą **Clean Code**, ponieważ:
* Eliminuje potrzebę definiowania „pustych” zmiennych pomocniczych przed startem pętli.
* Pozwala na bardziej elastyczne i precyzyjne określenie momentu wyjścia z algorytmu.

```python
while True:
    # Pobieramy dane bezpośrednio wewnątrz pętli
    command = input("> ")
    print("ECHO:", command)
    
    # Sprawdzamy warunek wyjścia; jeśli spełniony, natychmiast przerywamy pętlę
    if command.lower() == "quit":
        break
```

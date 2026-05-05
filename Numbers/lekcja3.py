# Podstawowe operatory arytmetyczne
print(10 + 4)     # Dodawanie: 14
print(10 - 4)     # Odejmowanie: 6
print(10 * 4)     # Mnożenie: 40
print(10 / 4)     # Dzielenie: 2.5
print(10 // 4)    # Dzielenie całkowite: 2
print(10 % 4)     # Modulo (reszta z dzielenia): 2
print(10 ** 4)    # Potęgowanie: 10000

a = 2
a += 4  # Skrócona forma: a = a + 4
a -= 4  # Skrócona forma: a = a - 4
a *= 4  # Skrócona forma: a = a * 4
a /= 4  # Skrócona forma: a = a / 4
a //= 4 # Skrócona forma: a = a // 4
a %= 4  # Skrócona forma: a = a % 4
a **= 4 # Skrócona forma: a = a ** 4

# Funkcje wbudowane
print(round(2.9))     # Zaokrąglenie: 3
print(abs(-2.9))      # Wartość bezwzględna: 2.9
print(pow(2, 3))      # Potęgowanie: 8
print(max(1, 5, 3))   # Maksimum: 5 
print(min(1, 5, 3))   # Minimum: 1
print(sum([1, 2, 3])) # Suma: 6

import math # Ważne: musimy to zaimportować na początku!

print(math.ceil(2.1))         # Zaokrąglenie w górę: 3
print(math.floor(2.9))        # Zaokrąglenie w dół: 2
print(math.sqrt(16))          # Pierwiastek kwadratowy: 4.0
print(math.pi)                # Stała pi: 3.141592653589793
print(math.e)                 # Stała e: 2.718281828459045
print(math.sin(math.pi / 2))  # Sinus 90 stopni: 1.0

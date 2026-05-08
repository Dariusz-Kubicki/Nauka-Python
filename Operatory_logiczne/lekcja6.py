# Operatory logiczne:
# and
# or
# not

# Sprawdzanie czy klient może dostać pożyczkę
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

# Przykład short-circuiting dla 'and'
# Jeśli high_income będzie False, Python nie sprawdzi już reszty warunków.
if high_income and good_credit and not is_student:
    print("Warunki spełnione")

age = 22
# Łańcuchowe porównanie (sprawdza, czy age jest większe lub równe 18 i jednocześnie mniejsze niż 65)
if 18 <= age < 65:
    print("Osoba jest w wieku produkcyjnym")

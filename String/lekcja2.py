course = "Python Programming"
print(course[0])      # Pierwszy znak: 'P'
print(course[-1])     # Ostatni znak: 'g'
print(course[0:3])    # Znaki od 0 do 2 (3 jest wykluczone): 'Pyt'
print(course[0:])     # Od 0 do końca: 'Python Programming'
print(course[:3])     # Od początku do 2: 'Pyt'
print(course[:])      # Kopia całego ciągu

course = "Python Programming"
print(len(course))    # Wypisze 18

course = "Python \"Programming"  # Cudzysłów: \"
course = "Python \'Programming"  # Apostrof: \'
course = "Python \\Programming"  # Backslash: \\
course = "Python \nProgramming"  # Nowa linia: \n

first = "Dariusz"
last = "Kubicki"
# Nowoczesny sposób (f-string)
full = f"{first} {last}"
print(full)

course = "   PyThon proGramming   "
print(course.upper())            # Wszystkie litery wielkie
print(course.lower())            # Wszystkie litery małe
print(course.title())            # Wielka litera w każdym słowie
print(course.strip())            # Usuwa spacje z obu stron
print(course.find("pro"))        # Zwraca indeks początku frazy (lub -1)
print(course.replace("m", "g"))  # Zamienia znaki
print("pro" in course)           # Zwraca True, jeśli fraza istnieje w tekście
print("swift" not in course)     # Zwraca True, jeśli frazy nie ma w tekście

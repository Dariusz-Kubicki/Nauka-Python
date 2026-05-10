# Pętla while
number = 100
while number > 0:
    print(number)
    number //= 2  # Skrócona forma: number = number // 2

command = ""
while command.lower() != "quit":
    command = input("> ")
    print("ECHO:", command)

while True:
    command = input("> ")
    print("ECHO:", command)
    if command.lower() == "quit":
        break

for character in file:
    if character.isupper():
        capital += 1
        file.readline().rstrip()
        break

print(capital)

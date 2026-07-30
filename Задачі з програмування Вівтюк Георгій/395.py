text = input()
count = 0
in_word = False

for char in text:
    if char.isalpha():
        if not in_word:
            count += 1
            in_word = True
    else:
        in_word = False

print(count)
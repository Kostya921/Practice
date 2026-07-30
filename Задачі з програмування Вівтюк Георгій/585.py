text = input().split()
max_len = 0
for word in text:
    if len(word) > max_len:
        max_len = len(word)
print(max_len)
n = input()
digits = sorted(list(n))

max_num = "".join(sorted(digits, reverse=True))

min_num = "".join(sorted(digits))
if min_num[0] == '0':
    for i in range(1, len(min_num)):
        if min_num[i] != '0':
            min_num = min_num[i] + min_num[:i] + min_num[i+1:]
            break

print(min_num, max_num)
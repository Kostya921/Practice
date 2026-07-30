import itertools

def get_permutations(sequence):
    return [list(p) for p in itertools.permutations(sequence)]

data = [int(x) for x in input().split()]
print(get_permutations(data))
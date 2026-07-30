with open('input.txt', 'r') as file:
    results = {}
    for line in file:
        line = line.strip()
        if not line:
            continue

        parts = line.split()
        if len(parts) >= 2 and parts[1].isdigit():
            candidate = parts[0]
            votes = int(parts[1])
            results[candidate] = results.get(candidate, 0) + votes

    for candidate in sorted(results.keys()):
        print(f"{candidate} {results[candidate]}")
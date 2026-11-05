counts = {}

with open("app.log") as f:
    for line in f:
        parts = line.split()
        level = parts[2]

        if level in counts:
            counts[level] = counts[level] + 1
        else:
            counts[level] = 1

print(counts)


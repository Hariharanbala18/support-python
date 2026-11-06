service_counts = {}

with open("app.log") as f:
    for line in f:
        parts = line.split()
        level = parts[2]
        service = parts[3]

        if level == "ERROR":
            if service in service_counts:
                service_counts[service] = service_counts[service] + 1
            else:
                service_counts[service] = 1

print(service_counts)
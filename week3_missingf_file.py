try:
    with open("file.log") as f:
        for line in f:
            print(line)

except FileNotFoundError:
    print("ERROR : Log file not found")
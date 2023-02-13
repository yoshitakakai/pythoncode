data = ["red", "green", "yellow", "blue", "black", "white"]
found = False
for i in range(len(data)):
    if data[i] == "blue":
        print(i)
        found = True
        break

if not found:
    print("Not Found")
with open("data.txt") as file:
    data = [i.replace("\n", "") for i in file.readlines()]

data_lists = [list(item) for item in data]
count = 0

for i in range(1, len(data_lists)):
    current_line = data_lists[i]
    previous_line = data_lists[i - 1]
    for j in range(len(current_line)):
        if previous_line[j] == "S":
            if current_line[j] == "^":
                current_line[j - 1], current_line[j + 1] = "S", "S"
                count += 1
            else:
                current_line[j] = "S"
print(count)



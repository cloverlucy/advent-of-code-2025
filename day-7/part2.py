with open("data.txt") as file:
    particle_data = [i.replace("\n", "") for i in file.readlines()]

data_lists = [list(item) for item in particle_data]
count = 0

for i in range(1, len(data_lists)):
    current_line = data_lists[i]
    previous_line = data_lists[i - 1]
    for j in range(len(current_line)):
        if previous_line[j] == "S":
            if current_line[j] == "^":
                left_list = []
                right_list = []
                for x in range(i + 1, len(data_lists)):
                    left_list.append(data_lists[x][j - 1])
                    right_list.append(data_lists[x][j + 1])
                print(j)

                print(left_list)
                if "^" in left_list:
                    pass
                else:
                    print("no ^ in left list")
                    count += 1

                print(right_list)
                if "^" in right_list:
                    pass
                else:
                    print("no ^ in right list")
                    count += 1

                current_line[j - 1], current_line[j + 1] = "S", "S"
            else:
                current_line[j] = "S"
print(data_lists)
print(count)

# for i in range(1, len(data_lists)):
#     current_line = data_lists[i]
#     previous_line = data_lists[i - 1]
#     for j in range(len(current_line)):
#         if previous_line[j] == "S":
#             if current_line[j] == "^":
#                 current_line[j - 1], current_line[j + 1] = "S", "S"
#                 count += 1
#             else:
#                 current_line[j] = "S"
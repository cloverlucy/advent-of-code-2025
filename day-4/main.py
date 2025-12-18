def printing_department(data, loop_once):
    count = 0

    while True:
        new_data = []
        for i in range(len(data) - 1):
            if i != 0 and i != len(data):
                current_line = data[i]
                previous_line = data[i - 1]
                next_line = data[i + 1]
                indexes = []
                for j in range(1, len(current_line) - 1):
                    if current_line[j] == "@":
                        if i != len(current_line):
                            items = [current_line[j - 1], current_line[j + 1], previous_line[j - 1: j + 2], next_line[j - 1: j + 2]]
                            items_string = "".join(items)
                            if items_string.count("@") < 4:
                                count += 1
                                indexes.append(j)
                new_current_line = list(current_line)
                for x in indexes:
                    new_current_line[x] = "."
                new_current_line = "".join(new_current_line)
                new_data.append(new_current_line)
        new_data.insert(0, "0" * len(data[0]))
        new_data.append("0" * len(data[0]))
        if new_data == data or loop_once == True:
            return count
        else:
            data = new_data


with open("data.txt") as file:
    roll_data = [i.replace("\n", "") for i in file.readlines()]
    roll_data.insert(0, "0" * len(roll_data[0]))
    roll_data.append("0" * len(roll_data[0]))
    roll_data = ["0" + i + "0" for i in roll_data]

printing_department(roll_data, True)
printing_department(roll_data, False)
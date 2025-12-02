def secret_entrance_part1(data, start_number):
    number = start_number
    count = 0
    for i in data:
        adjustment = int(i[1:])
        if i[0] == "L":
            number -= adjustment
        elif i[0] == "R":
            number += adjustment
        number %= 100
        if number == 0:
            count += 1
    return count

def secret_entrance_part2(data, start_number):
    number = start_number
    count = 0
    for i in data:
        adjustment = int(i[1:])
        if i[0] == "L":
            if adjustment >= number > 0:
                count += 1 + ((adjustment - number) // 100)
            elif number == 0:
                count += adjustment // 100
            number -= adjustment
        elif i[0] == "R":
            if adjustment + number >= 100:
                count += (adjustment + number) // 100
            number += adjustment
        number %= 100
    return count

with open("data.txt") as file:
    data_file = file.readlines()

secret_entrance_part1(data_file, 50)
print(secret_entrance_part2(data_file, 50))
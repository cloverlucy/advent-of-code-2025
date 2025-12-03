def gift_shop_part1(data):
    count = 0
    for item in data:
        first_number, last_number = int(item.split("-")[0]), int(item.split("-")[1])
        for number in range(first_number, last_number + 1):
            number_string = str(number)
            first_half, second_half = number_string[:int(len(number_string) / 2)], number_string[int(len(number_string) / 2):]
            if first_half == second_half:
                count += number
    return count

def gift_shop_part2(data):
    count = 0
    for item in data:
        first_number, last_number = int(item.split("-")[0]), int(item.split("-")[1])
        for number in range(first_number, last_number + 1):
            original_number_length = len(str(number))
            for factor in range(2, original_number_length + 1):
                if original_number_length % factor == 0:
                    number_split = []
                    number_string_tosplit = str(number)
                    for i in range(factor):
                        divisor = int(original_number_length / factor)
                        number_split.append(number_string_tosplit[:int(divisor)])
                        number_string_tosplit = number_string_tosplit[int(divisor):]
                    if all(x == number_split[0] for x in number_split):
                        count += number
                        break
    return count

with open("data.txt") as file:
    id_data = file.read().split(",")

gift_shop_part1(id_data)
gift_shop_part2(id_data)






def gift_shop_part1(data):
    count = 0
    for i in data:
        first_number = int(i.split("-")[0])
        last_number = int(i.split("-")[1])
        for number in range(first_number, last_number + 1):
            number_string = str(number)
            first_half, second_half = number_string[:int(len(number_string) / 2)], number_string[int(len(number_string) / 2):]
            if first_half == second_half:
                count += number
    return count

def gift_shop_part2(data):
    count = 0
    for item in data:
        first_number = int(item.split("-")[0])
        last_number = int(item.split("-")[1])
        for number in range(first_number, last_number + 1):
            number_string = str(number)
            factors = []
            original_number_length = len(number_string)
            for i in range(2, original_number_length + 1):
                if original_number_length % i == 0:
                    factors.append(i)

            for factor in factors:
                number_split = []
                number_string_tosplit = number_string
                for j in range(factor):
                    divisor = int(original_number_length / factor)
                    number_split.append(number_string_tosplit[:int(divisor)])
                    number_string_tosplit = number_string_tosplit[int(divisor):]
                if all(x == number_split[0] for x in number_split):
                    print(number_split)
                    count += number
                    break
    return count

with open("data.txt") as file:
    data_list = file.read().split(",")

gift_shop_part1(data_list)
gift_shop_part2(data_list)






def lobby(data, digits):
    joltage_total = 0
    for bank in data:
        enumerated_data = list(enumerate(bank))
        digits_list = []
        current_digit_position = -1
        for i in range(digits):
            current_best_digit = -1
            for item in enumerated_data[current_digit_position + 1:]:
                if int(item[1]) > current_best_digit and item[0] + (digits - 1) - i <= enumerated_data[-1][0]:
                    current_best_digit = int(item[1])
                    current_digit_position = item[0]
            digits_list.append(str(current_best_digit))
        joltage_total += int("".join(digits_list))
    return joltage_total

with open("data.txt") as file:
    battery_data = [i.replace("\n", "") for i in file.readlines()]

lobby(battery_data, 2)
lobby(battery_data, 12)
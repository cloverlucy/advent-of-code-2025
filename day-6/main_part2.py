def trash_compactor_part2(data):
    total = 0

    operators = data[len(data) - 1]
    operator_positions = []
    for i in range(len(operators)):
        if operators[i] == "*" or operators[i] == "+": # checks if character is an operator
            operator_positions.append(i) # adds position to list
    final_operator = len(operators) + 1 # adds position of final operator (had no spaces after to check position
    operator_positions.append(final_operator)

    number_list = []

    for j in range(len(data) - 1):
        numbers = []
        for i in range(len(operator_positions) - 1):
            if i == len(operator_positions) - 2: # checks for final number (had no spaces after to check spacing)
                numbers.append(data[j][operator_positions[i]:operator_positions[i+1] + 1])
            else:
                numbers.append(data[j][operator_positions[i]:operator_positions[i + 1]][:-1]) # adds numbers from one operator location to the next
        number_list.append(numbers)

    for i in range(len(number_list[0])): # amount of lists in number_list
        new_numbers = []
        for j in range(len(number_list[0][0])): # length of each number in number_list
            new_numbers.append(number_list[j][i]) # appends nth number from each column into a list

        rearranged_numbers = []
        for k in range(len(new_numbers[0])): # amount of numbers in new_numbers (also number of rows in data)
            rearranged_number = ""
            for j in range(len(data) - 1): # number of rows in data
                rearranged_number += new_numbers[j][k] # add nth digit of each item in list to new string
            rearranged_numbers.append(int(rearranged_number.strip("0"))) # remove 0s and turn to integer

        if operators[operator_positions[i]] == "+":
            total += sum(rearranged_numbers)
        elif operators[operator_positions[i]] == "*":
            res = 1
            for value in rearranged_numbers:
                res = res * value
            total += res
    return total

with open("data.txt") as file:
    maths_data = [i.replace("\n", "") for i in file.readlines()]
    maths_data = [i.replace(" ", "0") for i in maths_data]

trash_compactor_part2(maths_data)


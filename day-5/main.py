def cafeteria(data):
    count = 0
    data_divider = data.index("") # splits data into both sections
    id_ranges = data[:data_divider]
    ingredient_ids = data[data_divider + 1:]
    fresh_ingredients = []

    for item in id_ranges:
        first_number, last_number = int(item.split("-")[0]), int(item.split("-")[1])
        for j in ingredient_ids:
            if first_number <= int(j) <= last_number and j not in fresh_ingredients:
                count += 1
                fresh_ingredients.append(j)
    return count

def cafeteria_part2(data):
    count = 0
    id_ranges = data[:data.index("")]
    first_numbers = []
    last_numbers = []

    for i in id_ranges:
        first_number, last_number = int(i.split("-")[0]), int(i.split("-")[1])
        first_numbers.append(first_number)
        last_numbers.append(last_number)
    sorted_list = sorted(list(zip(first_numbers, last_numbers)))

    for x in range(len(sorted_list)):
        if x == 0: # first values added
            count += sorted_list[x][1] - sorted_list[x][0] + 1
        else:
            if sorted_list[x][0] > sorted_list[x - 1][1]: # if current and previous ranges do not overlap
                count += sorted_list[x][1] - sorted_list[x][0] + 1 # add entire range to total
            else:
                if (sorted_list[x][1] - sorted_list[x - 1][1]) >= 0: # if ranges do overlap and is not entirely contained within previous range
                    count += sorted_list[x][1] - sorted_list[x - 1][1] # add difference between current last number and previous last number
                else:
                    sorted_list[x] = sorted_list[x - 1] # ranges overlap but are entirely contained, so add no value, so compare to the previous range instead in next iteration
    return count

with open("data.txt") as file:
    ingredient_data = [i.replace("\n", "") for i in file.readlines()]

cafeteria(ingredient_data)
cafeteria_part2(ingredient_data)

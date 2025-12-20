def trash_compactor(data):
    total = 0

    maths_lists = []
    for item in data:
        x = item.split(" ")
        x = [i for i in x if i] # removes empty strings
        maths_lists.append(x)

    for j in range(len(maths_lists[0])):
        operator = maths_lists[-1][j]
        if operator == "+":
            res = 0
            for x in maths_lists[:-1]:
                res += int(x[j])
            total += res
        elif operator == "*":
            res = 1
            for x in maths_lists[:-1]:
                res *= int(x[j])
            total += res
    return total

with open("data.txt") as file:
    maths_data = [i.replace("\n", "") for i in file.readlines()]

trash_compactor(maths_data)
def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)

count = 0
with open("data.txt") as file:
    particle_data = [i.replace("\n", "") for i in file.readlines()]
data_lists = [list(item) for item in particle_data]

def recursion(n):
    global count

        # grab first line
        # search for S
        # if S,
        # if yes, search for ^ below until one is found
        # when one is found, recall function with beam position to the left and right
        # if it reaches line 15, count += 1
# PART ONE
# # First we process the input
lines = []
with open('input.txt') as input:
    for line in input:
        lines.append(line.rsplit())

modulo = len(lines[0])
index_last_row = len(lines) - 1
sum = 0

# For each column perform the calculation and add it
for column in range(modulo):
    temp_sum = int(lines[0][column])
    print("temp sum: ", temp_sum)
    for row in range(1,index_last_row):
        if lines[index_last_row][column] == "*":
            temp_sum = temp_sum * int(lines[row][column])
        else:
            temp_sum += int(lines[row][column])
    sum += temp_sum

print("Total sum: ", sum)

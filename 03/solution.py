# PART ONE

# Keep track of the total sum
# sum = 0

# with open('input.txt') as input:
#     for line in input:
#         maxlength = len(line.rstrip()) - 1
#         # we need to find the highest combination of numbers 
#         # let's loop over the line right to left, until we find the highest number and then find the highest number on the right side of that number?
#         first = -1
#         second = -1
#         firstindex = -1
#         secondindex = -1
#         for index in range(maxlength - 1, -1, -1):
#             # print(line[index])
#             if int(line[index]) >= first:
#                 first = int(line[index])
#                 firstindex = index
        
#         for indexTwo in range(maxlength, firstindex, -1):
#             if int(line[indexTwo]) >= second:
#                 second = int(line[indexTwo])
#                 secondindex = indexTwo
#         print(f"First: {first}, Second: {second}, at indices {firstindex}, {secondindex}")
#         total = first * 10 + second
#         print("Totals: ", total)
#         sum += total
#         print("Making the sum: ", sum)
            # 16946
# print("Total sum: ", sum)

# PART TWO 
sum = 0

with open('input.txt') as input:
    for line in input:
        maxlength = len(line.rstrip())
        digits = []
        currentIndex = 0
        # Find the digits needed
        for currentDigit in range(1,13):
            highest = -1
            highestIndex = -1
            # loop over the correct part of the remaining numbers
            for index in range(currentIndex, maxlength - (12-currentDigit)):
                if int(line[index]) > highest:
                    highest = int(line[index])
                    highestIndex = index + 1
            currentIndex = highestIndex
            digits.append(highest)

        # turn the digits into numbers 
        for i,x in enumerate(digits):
            sum += (x * pow(10,(12-i-1)))

print("Total sum: ", sum)
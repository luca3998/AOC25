# PART ONE

# Keep track of the total sum
# sum = 0

# with open('input.txt') as input:
#     for line in input:
#         # for each range check if there is an example where the two halves are symmetrical 
#         cur = line.split(",")
#         for current_range in cur:
#             range_converted = str(current_range).split("-") # list of lists of ranges, in strings
#             start = int(range_converted[0])
#             end = int(range_converted[1])
#             for x in range(start,end + 1):
#                 x_str = str(x)
#                 # for each number if length not even. skip
#                 if (len(x_str) % 2) != 0:
#                     continue 
                
#                 # for each number split in half 
#                 x_str = str(x)
#                 half_length = int(len(x_str) / 2)
#                 first_half = x_str[:half_length]
#                 second_half = x_str[half_length:]
#                 # Check if first half == second half 
#                 if first_half == second_half:
#                     sum += x

# print(sum)

# PART TWO
import math
set_sum = {0}

with open('input.txt') as input:
    for line in input:
        # for each range check if there is an example where the two halves are symmetrical 
        
        cur = line.split(",")
        for current_range in cur:

            range_converted = str(current_range).split("-") # list of lists of ranges, in strings
            start = int(range_converted[0])
            end = int(range_converted[1])
            for number in range(start,end + 1):
                number_stringified = str(number)
                amount_of_characters = len(number_stringified)
                # for each number if length = 1, skip
                if amount_of_characters == 1:
                    continue 

                # for each number check by which numbers you can divide it and then splice it accordingly 
                dividable_numbers = []
                for x in range(1,amount_of_characters):
                    if amount_of_characters % x == 0:
                        dividable_numbers.append(x)

                # We need to check every combination of numbers
                # For every combination we check the first option and see if its the same as all other parts, if not continue 
                for option in dividable_numbers:  # 1,2,3
                    amount_of_options = int(amount_of_characters / option)  # 6,3,2
                    first = number_stringified[:option]
                    for a in range(option,amount_of_characters,option):
                        # loop over the other options and compare them to first, if not same break
                        second = number_stringified[a:a+option]

                        if first != second:
                            break
                        elif a+option == amount_of_characters: 
                            set_sum.add(number)
                    
print(set_sum)
sum_of_sum = sum(set_sum)
print("sums up to : ", sum_of_sum)
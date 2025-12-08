# PART ONE

# Keep track of the total sum
# rolls = 0
# input_list = []
# with open('input.txt') as input:
#     for line in input:
#         input_list.append(line.rstrip())

# width = len(input_list[0])
# height = len(input_list)

# for x in range(width): # loop over the positions in x direction
#     for y in range(height): # "" in y direction
#         if input_list[y][x] == ".": continue
#         # we are going to check for every position how many "@" there are in the 8 positions surrounding it
#         start_ix = 0 if x == 0 else -1
#         start_iy = 0 if y == 0 else -1
#         end_ix = 0 if x == (width - 1) else 1
#         end_iy =  0 if y == (height - 1) else 1
#         surrounding_rolls = 0
#         for a in range(start_ix,end_ix+1):
#             for b in range(start_iy,end_iy+1):
#                 if a == 0 and b == 0: continue
#                 if input_list[y + b][x + a] == "@": 
#                     surrounding_rolls += 1
#         if surrounding_rolls < 4:
#             rolls += 1
# print("Total rolls: ", rolls)


# Part Two
rolls = 0
input_list = []
with open('input.txt') as input:
    for line in input:
        input_list.append(line.rstrip())

width = len(input_list[0])
height = len(input_list)
keep_going = True

while keep_going:
    rolls_in_sweep = 0
    for x in range(width): # loop over the positions in x direction
        for y in range(height): # "" in y direction
            if input_list[y][x] == ".": continue
            # we are going to check for every position how many "@" there are in the 8 positions surrounding it
            start_ix = 0 if x == 0 else -1
            start_iy = 0 if y == 0 else -1
            end_ix = 0 if x == (width - 1) else 1
            end_iy =  0 if y == (height - 1) else 1
            surrounding_rolls = 0
            for a in range(start_ix,end_ix+1):
                for b in range(start_iy,end_iy+1):
                    if a == 0 and b == 0: continue
                    if input_list[y + b][x + a] == "@" or input_list[y + b][x + a] == "X" : 
                        surrounding_rolls += 1
            if surrounding_rolls < 4:
                rolls_in_sweep += 1
                new = list(input_list[y])
                new[x] = "X"
                input_list[y] = "".join(new)
    rolls += rolls_in_sweep
    # once a sweep has been completed we simply replace X's by "."s
    for y in range(height): # "" in y direction
        input_list[y] = input_list[y].replace('X','.')

    # Check if we can still remove rolls, if not we exit the loop
    if(rolls_in_sweep == 0):
        keep_going = False
print("Total rolls: ", rolls)

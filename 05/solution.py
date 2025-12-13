# PART ONE
# all = []
# ranges = []
# ids = []
# fresh_ids = []
# # First we process the input
# with open('input.txt') as input:
#     for line in input:
#         all.append(line)

# # Split into ranges and ids
# split_index = all.index("\n")
# ranges = all[0:split_index]
# ids = all[split_index+1:]

# # Loop over all ids to find out which ones are fresh 
# for id in ids:
#     for range_to_check in ranges:
#         converted = range_to_check.split("-")
#         start = int(converted[0])
#         end = int(converted[1].rstrip())
#         if start <= int(id) <= end:
#             fresh_ids.append(id)
#             break
# amount = len(fresh_ids)
# print(f"Amount: ", amount)

# PART TWO
# yet to implement

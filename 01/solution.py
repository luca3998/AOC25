import math 

countZeroes = 0
current = 50

# Part one
# with open('input.txt') as input:
#     for line in input:
#         direction = line[0]
#         amount = int(line[1:])
#         if direction == "L":
#             current = (current - amount) % 100
#         if direction == "R":
#             current = (current + amount) % 100
        
#         if current == 0:
#             countZeroes += 1

# Part two (uncomment whichever you want)
with open('input.txt') as input:
    for line in input:
        direction = line[0]
        amount = int(line[1:])
        if direction == "L":
            new = current - amount 
            if new <= 0:
                passes = 1 + math.floor(abs(amount / 100)) 
                result = new % 100 #
                if current == 0:
                    passes -= 1
                if (amount % 100) < current:
                    passes -= 1
                
                countZeroes = countZeroes + passes
        if direction == "R":
            new = current + amount
            if new > 99:
                passes = 1 + math.floor(abs(amount / 100))
                result = new % 100 # this will be the new number 
                if current == 0:
                    passes -= 1
                if (amount % 100) < (100 - current) and current != 0:
                    passes -= 1
                countZeroes = countZeroes + passes
        current = new % 100

print(countZeroes)

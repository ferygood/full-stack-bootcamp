def calculate(min, max):
    sum = 0
    for x in range(min, max+1):
        sum += x
    return sum

print(calculate(1,3)) #6
print(calculate(4,8)) #30
        

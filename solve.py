def solve(number, count):
    sum = 0
    for i in range(count):
        for j in range(i+1):
            sum += number*10**j
    return sum

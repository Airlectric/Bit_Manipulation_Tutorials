def countConvertedBits(num, goal):
    res = num ^ goal
    count = 0
    while (res != 0):
        res = res & res-1
        count+=1
    return count

print(countConvertedBits(10,7))

        
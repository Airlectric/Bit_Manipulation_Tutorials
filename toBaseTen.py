def toBaseTen(num):
    num = str(num)
    pow = 0
    res = 0
    
    for i in range(len(num)-1,-1,-1):
        res += int(num[i]) * 2**pow
        pow += 1

    return res

print(toBaseTen(1101))


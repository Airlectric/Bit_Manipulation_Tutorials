def toBinary(num):
    res = ''
    while num != 1:

        if num % 2 == 1:
            res += '1'
        else:
            res+= '0'
        
        num //= 2
    res += '1'
    return int(res[::-1])

print(toBinary(4))

def xorNumInRange(N):
    if N % 4 == 1:
        return 1
    elif N % 4 == 2:
        return N+1
    elif N % 4 == 3:
        return 0
    else:
        return N
    
def withinRange(l,r):
    return xorNumInRange(l) ^ xorNumInRange(r)

print(xorNumInRange(12))

print(withinRange(3,6))
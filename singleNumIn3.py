def singleNum(arr):
    res = 0

    for bitIndex in range(32):
        count = 0
        for j in range(len(arr)):
            if arr[j] & (1 << bitIndex):
                count +=1
        if count % 3 == 1:
            res = res | (1 << bitIndex)

    return res

# print(singleNum([1,1,1,3,3,3,4,4,4,6]))

def singleNumII(arr):
    arr = sorted(arr)
    print(arr)
    for i in range(1, len(arr),3):
        if arr[i] != arr[i-1]:
            return arr[i-1]
    return arr[-1]
        

# print(singleNumII([1,1,1,6,3,3,3,4,4,4]))

def singleNumIII(arr):
    ones, twos = 0, 0
    for num in arr:
        twos |= ones & num

        ones ^= num

        threes = ones & twos

        ones &= ~threes
        twos &= ~threes
    return ones

# print(singleNumIII([1,1,1,6,3,3,3,4,4,4]))

def singleNumIV(arr):
    ones, twos = 0,0

    for num in arr:
        ones ^= num & ~twos
        twos ^= num & ~ones

    return ones

print(singleNumIV([1,1,1,6,3,3,3,4,4,4]))




        
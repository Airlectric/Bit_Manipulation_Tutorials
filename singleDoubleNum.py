def singleDouNums(arr):
    single = 0
    for num in arr:
        single ^= num
    
    rightmost = (single & single-1) ^ single
    
    b1,b2 = 0,0
    for num in arr:
        if (num & rightmost):
            b1 ^= num
        else:
            b2 ^= num

    return [b1,b2]

print(singleDouNums([1,1,3,2,2,5,7,7,9,9,10,10]))
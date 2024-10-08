def singleNumInArray(arr):
    single = 0

    for i in range(len(arr)):
        single ^= arr[i]

    return single

print(singleNumInArray([1,1,2,3,3,4,4]))


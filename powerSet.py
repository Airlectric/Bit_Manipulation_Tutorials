def powerSet(arr):
    n = len(arr)
    big = []

    for i in range(2**n):
        small = []
        for j in range(len(arr)):
            if (i & (1<< j)) != 0:
                small.append(arr[j])
        big.append(small)

    return big

print(powerSet([6,3,2]))

    

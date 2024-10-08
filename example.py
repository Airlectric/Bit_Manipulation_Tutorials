#swap two numbers

# a = 5
# b = 8

# a = a^b
# b = a^b
# a = a^b

# print('a:',a, 'b:',b)

# check if ith bit is set or not
# print((13>>2) & 1)
# print(13 & (1 << 1))

# set the ith bit
# print(9 | 1 << 2)

# clear the ith bit
# print(13 & ~(1<<2))

# Toggling the ith bit
# print(13 ^ (1<<1) )

# Remove the last set bit
# print(13 & (13-1))

# check if the number is a power of 2. if pow of 2:output is 0 else any number is output
print(16 & (16-1)) 

# Count the number of set bits
def countBits(num):
    count = 0

    while num > 1:
        if num & 1 == 1:
            count+=1
        num = num >> 1

    if num == 1:
        count+=1

    return count

# print(countBits(13))

def countBits2(num):
    count = 0
    while num != 0:
        num = (num & num-1)
        count+=1
    return count

# print(countBits2(13))
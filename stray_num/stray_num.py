# You are given an odd-length array of integers, in which all of them are the same, except for
# one single number.
#
# Complete the method which accepts such an array, and returns that single different number.

def stray(arr):
    arr_dict = {x:arr.count(x) for x in arr}
    for k, v in arr_dict.items():
        if v == 1:
            stray_num = k
    return stray_num

arr= [17, 17, 4, 17, 17, 17]
print(stray(arr))
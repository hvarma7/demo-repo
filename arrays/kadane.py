def kadane(array):
    max_so_far = max_ending_here = 0
    for i in range(0,len(array)):
        max_ending_here += array[i]

        if max_ending_here < 0:
            max_ending_here = 0
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

    return max_so_far

array = [-2, -3, 4, -1, -2, 1, 5, -3] 
array_2 = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
array_3 = [-2, 1, -3, 4, -1, 2, 1, -5,4]
# print(kadane(array))
print(kadane(array))
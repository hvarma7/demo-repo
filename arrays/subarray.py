
def subarray(array, target):
    left = right = 0
    current_sum = array[0]
    while right < len(array):
        if current_sum == target:
            print("found {} and {}".format(left, right))

        if current_sum <= target:
            right += 1
            if(right < len(array)):
                current_sum += array[right]        
        else:
            current_sum -= array[left]
            left += 1

    


array = [1, 4, 20, 3, 10, 5]
array_2 = [ 0, 0, 0, 1, 0, 0, 0, 0]
sum = 33
sum_2 = 1
subarray(array, sum)
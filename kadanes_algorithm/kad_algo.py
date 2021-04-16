def kadane_algo(arr):

    if len(arr) == 0:
        return 0

    max_sum = arr[0]
    current_sum = arr[0]

    for num in arr[1:]:
        current_sum += num
        if num > current_sum:
            current_sum = num
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

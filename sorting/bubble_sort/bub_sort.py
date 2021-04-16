def bubble_sort(array):

    while True:  # [2nd method] for j in range(len(array) - 1):

        did_it_swap = False

        for i in range(len(array) - 1):  # [2nd method] for i in range(len(array) - 1 - j):
            if array[i] > array[i + 1]:
                a1 = array[i]
                array[i] = array[i + 1]
                array[i + 1] = a1
                did_it_swap = True

        if not did_it_swap:
            break

    return array

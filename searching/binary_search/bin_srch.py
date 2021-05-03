def binary_search(sequence, target):
    """
    binary_search- a binary search algorithm that finds the position (index) of a target*
    within a given sequence* (sorted array)
    """

    starting_index = 0
    ending_index = len(sequence) - 1

    while starting_index <= ending_index:

        middle_index = starting_index + ((ending_index - starting_index) // 2)

        if sequence[middle_index] == target:
            return middle_index

        elif target < sequence[middle_index]:
            ending_index = middle_index - 1

        else:
            starting_index = middle_index + 1

    return None  # return None if a target is not present in the sequence

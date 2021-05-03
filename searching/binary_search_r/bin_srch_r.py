def binary_search_r(sequence, target, starting_index=None, ending_index=None):
    """
    binary_search_r- a recursive binary search algorithm that finds the position (index) of a target*
    within a given sequence* (sorted array)
    """

    if starting_index is None:
        starting_index = 0

    if ending_index is None:
        ending_index = len(sequence) - 1

    if ending_index < starting_index:
        return None

    middle_index = (starting_index + ending_index) // 2

    if target == sequence[middle_index]:
        return middle_index

    elif target < sequence[middle_index]:
        return binary_search_r(sequence, target, starting_index=None, ending_index=middle_index - 1)

    else:
        return binary_search_r(sequence, target, starting_index=middle_index + 1, ending_index=None)

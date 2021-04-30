def binary_search(sequence, item):
    """
    sequence- sorted array
    """

    start_index = 0
    end_index = len(sequence) - 1

    while start_index <= end_index:

        midpoint_index = start_index + ((end_index - start_index) // 2)

        if sequence[midpoint_index] == item:
            return midpoint_index

        elif item < sequence[midpoint_index]:
            end_index = midpoint_index - 1

        else:
            start_index = midpoint_index + 1

    return None  # return None if an item is not present in the sequence

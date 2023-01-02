from array import array


def process_insert_sort(unsorted_array: array) -> array:
    """

    :param unsorted_array: array
    :return:
        sorted_array
    """
    sorted_array = unsorted_array
    for j in range(2, len(sorted_array)):
        key = sorted_array[j]
        i = j - 1
        while i > 0 and sorted_array[i] > key:
            sorted_array[i+1] = sorted_array[i]
            i = i - 1
        sorted_array[i+1] = key

    return sorted_array


def process_reverse_insert_sort(unsorted_array: array) -> array:
    """

    :param unsorted_array:
    :return:
        reverse_sorted_array
    """
    reverse_sorted_array = unsorted_array

    return reverse_sorted_array


if __name__ == '__main__':
    my_array = array('b', [31, 41, 59, 26, 41, 58])
    print(process_insert_sort(my_array))
    print(process_reverse_insert_sort(my_array))

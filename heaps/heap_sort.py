from heaps.min_heap import MinHeap


def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(n * n log n)
        Space Complexity: O(n)
    """
    if len(list) <= 1:
        return list

    heap = MinHeap()

    for item in list:
        heap.add(item)

    return_list = []
    while heap.empty() != True:
        return_list.append(heap.remove())

    return return_list


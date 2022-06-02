from min_heap import MinHeap


def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  ?
        Space Complexity: ?
    """
    heap = MinHeap()

    sorted_array = []
    for num in list:
        heap.add(num)

    while not heap.empty():
        sorted_array.append(heap.pop())

    return sorted_array

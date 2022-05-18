from heaps.min_heap import MinHeap


def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  On
        Space Complexity: On
    """
    result = []
    heap = MinHeap()

    for item in list:
        heap.add(item)

    while len(heap.store) > 0:
        result.append(heap.remove())

    return result

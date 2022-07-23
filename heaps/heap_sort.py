from heaps.min_heap import MinHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  ?
        Space Complexity: ?
    """
    if len(list) <= 1:  # returns list of empty or only has one node
        return list

    heap = MinHeap()

    for value in list:
        heap.add(value)

    result = []  # unpacking the heap into a new result list to avoid side effects
    while not heap.empty():
        result.append(heap.remove())

    return result

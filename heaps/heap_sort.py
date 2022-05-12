from heaps.min_heap import MinHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  ?
        Space Complexity: ?
    """
    min_heap = MinHeap()

    for item in list:
        min_heap.add(item)

    for i in range(len(list)):
        list[i] = min_heap.remove()

    return list

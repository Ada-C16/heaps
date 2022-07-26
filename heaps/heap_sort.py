from heaps.min_heap import MinHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  (log n)
        Space Complexity: (O n)
    """

    heap = MinHeap()

    for i in list:
        heap.add(i)

    i = 0

    while not heap.empty():
        list[i] = heap.remove()
        i += 1

    return list
from heaps.min_heap import MinHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(n log n)
        Space Complexity: O(n)
    """

    heap = MinHeap()
    for element in list:
        heap.add(element)

    index = 0
    while not heap.empty():
        list[index] = heap.remove()
        index += 1

    return list
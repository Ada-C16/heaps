from heaps.min_heap import MinHeap

def heap_sort(arr):
    """ This method uses a heap to sort an array.
        Time Complexity:  o(n^2)
        Space Complexity: o(1)
    """
    heap = MinHeap()

    for x in arr:
        heap.add(x) # o(n) | o(1)

    i = 0
    while not heap.empty():
        arr[i] = heap.remove()
        i += 1

    return arr

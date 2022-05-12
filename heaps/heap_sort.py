from .min_heap import MinHeap

def heap_sort(l):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(n log n)
        Space Complexity: O(n)
    """
    if len(l) <= 1:
        return l

    heap = MinHeap()

    for item in l:
        heap.add(item)

    sorted = []

    while heap.store:
        item = heap.remove()
        sorted.append(item)

    return sorted

l = [5, 27, 3, 16, 50]
heap_sort(l)
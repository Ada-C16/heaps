from . import min_heap as h

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(n log n)
        Space Complexity: O(n log n) even though it sorts in place it still uses heap_down
            which is O(log n)
    """
    heap = h.MinHeap(list)
    for item in list:
        heap.add(item)

    for item in list:
        list.append(heap.remove())

    return list




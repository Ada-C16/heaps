from . import min_heap as h

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  ?
        Space Complexity: ?
    """
    heap = h.MinHeap(list)
    for item in list:
        heap.add(item)

    for item in list:
        list.append(heap.remove())

    return list




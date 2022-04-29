from heaps.min_heap import MinHeap


def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  ?
        Space Complexity: ?
    """
    
    min_heap = MinHeap()
    
    for num in list:
        min_heap.add(num)
    
    i = 0
    while min_heap.empty() is False:
        cur_min = min_heap.remove() # remove the root and re-heap the heap
        list[i] = cur_min
        i += 1
    return list 
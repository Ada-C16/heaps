from heaps.min_heap import MinHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(n log n)
        Space Complexity: O(n)
    """
    min_heap = MinHeap()

    
    for element in list:
        min_heap.add(element)

    for i in range(len(list)):
        list[i] = min_heap.remove()

    return list
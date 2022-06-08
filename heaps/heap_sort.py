from heaps.min_heap import MinHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(log n)
        Space Complexity: O(n)
    """
    heap = MinHeap()
    for element in list:
        heap.add(element)

    sorted_list = []
    while heap.store:
        element = heap.remove()
        sorted_list.append(element)

    return sorted_list
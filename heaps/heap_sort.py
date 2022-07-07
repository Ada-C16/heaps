from heaps.min_heap import MinHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(n log n) where n is the number of items in the list
        Space Complexity: O(n) where n is the number of items in the list
    """
    heap = MinHeap()
    for item in list:
        heap.add(item)
    for i in range(len(list)):
        list[i] = heap.remove()
    return list

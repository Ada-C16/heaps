from heaps.min_heap import MinHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(nlogn)
        Space Complexity: O(n)
    """
    heap = MinHeap()
    sorted = []
    for item in list:
        heap.add(item)
    for i in range(len(list)):
        sorted.append(heap.remove())
    return sorted
    
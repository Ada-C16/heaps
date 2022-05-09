from .min_heap import MinHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(nlogn)
        Space Complexity: O(n)
    """
    heap = MinHeap()

    for item in list:
        heap.add(item)
    
    ordered = []

    while not heap.empty():
        next_smallest = heap.remove()
        ordered.append(next_smallest)
    
    return ordered
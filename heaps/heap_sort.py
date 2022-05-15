from heapq import heappush, heappop

def heap_sort(unsorted):
    """ This method uses a heap to sort an array.
        Time Complexity:  n log n
        Space Complexity: n
    """
    heap = []

    for item in unsorted:
        heappush(heap, item)
    
    ordered = []

    while heap:
        value = heappop(heap)
        ordered.append(value)

    return ordered

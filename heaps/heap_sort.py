from heapq import heappush, heappop

def heap_sort(lst):
    """ This method uses a heap to sort an array.
        Time Complexity: O(n logn)
        Space Complexity: O(n)
    """
    heap = []

    # heappush takes care of the swapping behind the scenes
    for item in lst: #n log(n)
        heappush(heap, item)

    # new list
    ordered = []

    # heappop also takes care of swapping
    while len(heap) > 0:
        val = heappop(heap) #n log(n)
        ordered.append(val)

    return ordered


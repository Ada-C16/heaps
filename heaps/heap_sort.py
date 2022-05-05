from heapq import heappush, heappop

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(n log n)
        Space Complexity: O(n)
    """
    heap = []
    for item in list:
      heappush(heap, item)
    
    sorted_list = []
    while len(heap) > 0:
      sorted_list.append(heappop(heap))

    return sorted_list 
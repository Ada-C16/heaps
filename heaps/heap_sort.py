from heapq import heappush, heappop


def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(n log n)
        Space Complexity: O(n)
    """
    heap = []

    for item in list:
        heappush(heap, item)

    ordered = []

    while len(heap) > 0:
        value = heappop(heap)
        ordered.append(value)

    # print(heap)
    return ordered

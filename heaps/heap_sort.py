from heapq import heappush, heappop


def heap_sort(list):

    heap = []

    for item in list:
        heappush(heap, item)

    ordered = []

    while len(heap) > 0:
        val = heappop(heap)
        ordered.append(val)

    return ordered

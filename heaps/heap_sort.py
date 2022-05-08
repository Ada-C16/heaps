

from os import remove
from heaps.min_heap import MinHeap


def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(nlogn)
        Space Complexity: O(1)
    """
    heap = MinHeap()
    for item in list:
        heap.add(item)
    return [heap.remove() for _ in range(heap.length)]

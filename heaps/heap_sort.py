

from heaps.min_heap import MinHeap


def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(nlogn)
        Space Complexity: O(1)
    """
    heap = MinHeap()
    [heap.add(item) for item in list]
    return [heap.remove() for _ in range(heap.length)]

from heaps.min_heap import MinHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  ?
        Space Complexity: ?
    """
    if len(list) <= 1:  # returns list of empty or only has one node
        return list

    heap = MinHeap()

    for value in list:
        heap.add(value)

    index = 0
    while not heap.empty():
        list[index] = heap.remove()
        index += 1

    return list

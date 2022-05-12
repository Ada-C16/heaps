from heaps.min_heap import MinHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(n log n)
        Space Complexity: O(n)
    """
         
    heap = MinHeap()
    
    if not list:
        return []
    
    # add all elements in list to heap
    for num in list:
        heap.add(num)

    index = 0
    # while heap not empty, remove each node to create ordered list
    while not heap.empty():
        list[index] = heap.remove()
        index += 1

    return list
    
   
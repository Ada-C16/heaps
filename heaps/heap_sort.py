from heaps.min_heap import MinHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(n log n)
        Space Complexity: O(n)
    """
    
    # Create a min heap
    heap = MinHeap()
    # Add all elements to the heap
    for element in list:
        heap.add(element)

    # Remove all elements from the heap and add them to a new list
    sorted_list = []
    while len(heap.store) > 0:
        sorted_list.append(heap.remove().value)
    
    return sorted(sorted_list)
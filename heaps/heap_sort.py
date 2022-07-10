from heaps.min_heap import MinHeap
def heap_sort(nums):
    """ This method uses a heap to sort an array.
        Time Complexity:  ?
        Space Complexity: ?
    """


    heap = MinHeap()

    for num in nums:
        heap.add(num)
    
    #adding everything to the minheap, which sorts everything
    
    index = 0

    #then we are printing them in order
    while not heap.empty():
        nums[index] = heap.remove()
        index += 1

    
    return nums 
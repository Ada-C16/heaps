from heaps.min_heap import MinHeap

def heap_sort(nums):
    
    heap = MinHeap()

    for num in nums:
        heap.add(num)

    index = 0
    while not heap.empty():
        nums[index] = heap.remove()
        index += 1

    return nums
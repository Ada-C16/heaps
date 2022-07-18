from heapq import heappush, heappop
from heaps.min_heap import MinHeap

def heap_sort(list): # O(n)
    """ This method uses a heap to sort an array.
        Time Complexity:  O(n log n)
        Space Complexity: O(n)
    """
    heap = MinHeap()
    for num in list:
        # has heap_up inside and sorts it in heap everytime new node is added
        heap.add(num)

    # while the heap is not empty, it removes the most minimal value which is always the root
    index = 0
    while not heap.empty():
        # puts sorted nums back in list using index
        # remove is O(log n)
        list[index] = heap.remove()
        index += 1

    return list

# from class
# Time: n log n
# space: n
def heapsort(unsorted):
    heap = []
    for item in unsorted:
        heappush(heap, item)
        # heapq is putting all of this together. append will treat it like any other list and does order it
    
    ordered = []
    while len(heap) > 0:
        value = heappop(heap)
        ordered.append(value)

    # returns ordered elements
    return ordered 

print(heapsort([4,7,1,33,0,-8]))
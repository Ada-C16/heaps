''' i tried to import MinHeap from the other file but it wasn't passing pytest tests 

this is what i was writing:
from min_heap import MinHeap

anyway i copy and pasted the functions from previous work, but removed the Heap Node part since these tests just look at a list of numbers.

see line 76 for the heap_sort function!

'''

class MinHeap:

    def __init__(self):
        self.store = []

    def add(self, key):
        self.store.append(key)
        last_index = len(self.store) - 1
        self.heap_up(last_index)
        return

    def remove(self):
        if self.empty():
            return
        self.swap(0, -1)
        result = self.store.pop()
        if not self.empty():
            self.heap_down(0)
        return result

    def empty(self):
        if len(self.store) == 0:
            return True
        return False

    def heap_up(self, index):
        parent_index = int((index - 1) / 2)
        current = self.store[index]
        parent = self.store[parent_index]

        while current < parent:
            self.swap(index, parent_index)
            index = parent_index
            parent_index = int((index - 1) / 2)
            current = self.store[index]
            parent = self.store[parent_index]

    def has_left_child(self, index):
        left_child_index = int((2 * index) + 1)
        if left_child_index <= len(self.store) - 1:
            return True
        return False

    def has_right_child(self, index):
        right_child_index = int((2 * index) + 2)
        if right_child_index <= len(self.store) - 1:
            return True
        return False
    
    def heap_down(self, index):
        if self.has_left_child(index) and (self.store[index] > self.store[int((2 * index) + 1)]):
            left_child_index = (2 * index) + 1
            self.swap(index, left_child_index)
            self.heap_down(left_child_index)

        if self.has_right_child(index) and (self.store[index] > self.store[int((2 * index) + 2)]):
            right_child_index = (2 * index) + 2
            self.swap(index, right_child_index)
            self.heap_down(right_child_index)           
        return        

    def swap(self, index_1, index_2):
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  ? O(n)
        Space Complexity: ? O(n)
    """
    result = []
    if not list:
        return result
    
    da_heap = MinHeap()

    for num in list:
        da_heap.add(num)
    
    while len(result) != len(list):
        top_of_heap = da_heap.remove()
        result.append(top_of_heap)

    return result


nums = [5, 27, 3, 16, 50]
print(f"{nums} <---given nums")
result = heap_sort(nums)
print(f"{result} <---result of heap_sort")
expected = [3, 5, 16, 27, 50]
print(f"{expected} <--- expected result")
print(f"do they match? {result == expected}")
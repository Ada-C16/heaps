from logging import root
import re


class HeapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

class MinHeap:

    def __init__(self):
        self.store = []


    def add(self, key, value = None):
        """ This method adds a HeapNode instance to the heap
            If value == None the new node's value should be set to key
            Time Complexity: O(log n)
            Space Complexity: O(1)
        """
        node = None
        if value == None:
            value = key
        
        node = HeapNode(key, value)
        self.store.append(node)
        self.heap_up(self.last_index())


    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: O(log n)
            Space Complexity: O(1)
        """
        if self.empty():
            return None

        self.swap(0, self.last_index())
        root = self.store.pop(self.last_index()).value
        self.heap_down(0)

        return root


    
    def __str__(self):
        """ This method lets you print the heap, when you're testing your app.
        """
        if len(self.store) == 0:
            return "[]"
        return f"[{', '.join([str(element) for element in self.store])}]"


    def empty(self):
        """ This method returns true if the heap is empty
            Time complexity: O(1)
            Space complexity: O(1)
        """

        return len(self.store) == 0



    def heap_up(self, index):
        """ This helper method takes an index and
            moves the corresponding element up the heap, if 
            it is less than it's parent node until the Heap
            property is reestablished.
            
            This could be **very** helpful for the add method.
            Time complexity: O(log n)
            Space complexity: O(1)
        """
        if index == 0:
            return

        swap = (index - 1) // 2

        if self.store[index].key < self.store[swap].key:
            self.swap(index, swap)
            self.heap_up(swap)

        elif self.store[index].key == self.store[swap].key and self.store[index].value < self.store[swap].value:
            self.swap(index, swap)
            self.heap_up(swap)               



    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
            Time complexity: O(log n)
            Space complexity: O(1)
        """
        left = (index*2) + 1
        right = (index*2) + 2

        if left > self.last_index():
            return

        to_compare = left

        if right <= self.last_index():
            if self.store[right].key < self.store[left].key:
                to_compare = right
    
        if self.store[index].key > self.store[to_compare].key:
            self.swap(index, to_compare)
            self.heap_down(to_compare)

        elif self.store[index].key == self.store[to_compare].key and self.store[index].value > self.store[to_compare].value:
            self.swap(index, to_compare)
            self.heap_up(to_compare)               


    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp
    
    def last_index(self):
        """ This method gives you the last index
            of your heap.
        """
        return len(self.store)-1


from queue import Empty
from turtle import left


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
            Time Complexity: O(1) if adding to rear, else O(logn)
            Space Complexity: O(1)
        """
        if value == None:
            value = key
        
        node = HeapNode(key, value)
        self.store.append(node)
        self.heap_up(len(self.store) - 1)

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: O(logn)
            Space Complexity: O(1)
        """
        if len(self.store) == 0:
            return None
        
        # swap at index 0 and last element
        self.swap(0, len(self.store) -1)
        # remove last element
        min = self.store.pop()
        self.heap_down(0)

        return min.value


    
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
        if len(self.store) == 0:
            return True
        return False


    def heap_up(self, index):
        """ This helper method takes an index and
            moves the corresponding element up the heap, if 
            it is less than it's parent node until the Heap
            property is reestablished.
            
            This could be **very** helpful for the add method.
            Time complexity: ?
            Space complexity: ?
        """
        # return when index = 0
        if index == 0:
            return
        
        # get parent node
        parent = ( index - 1 ) // 2

        # check parent and current index
        if self.store[parent].key > self.store[index].key:
            self.swap(parent, index)
        index = parent
        
        #recursively check until index == 0
        return self.heap_up(index)

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        # check children
        # if children > index, swap
        # return when index > heap size

        # return when index is greater than size of heap
        if index > len(self.store) - 1:
            return
        
        left = (index * 2) + 1
        right = (index * 2) + 2

        if self.store[left].key > self.store[index].key:
            self.swap(left, index)
        index = left

        return self.heap_down(index)

    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp


# heap = MinHeap()
# heap.add(3, "Pasta")
# heap.add(7, "Noodles")
# heap.add(2, "Icecream")
# heap.add(5, "Zaub Haus")
# print(heap)
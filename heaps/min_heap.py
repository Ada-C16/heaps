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

    # helpers
    def parent_index(self, index):
        return (index - 1) // 2

    def left_child_index(self, index):
        return (2 * index) + 1

    def right_child_index(self, index):
        return (2 * index) + 2


    def add(self, key, value = None):
        """ This method adds a HeapNode instance to the heap
            If value == None the new node's value should be set to key
            Time Complexity: O(log n)
            Space Complexity: O(1)
        """

        if value is None:
            value = key

        new_node = HeapNode(key, value)
        self.store.append(new_node)
        self.heap_up(len(self.store) - 1) 


    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: O(log n)
            Space Complexity: O(1)
        """

        if len(self.store) == 0:
            return

        self.swap(0, len(self.store) - 1)
        min = self.store.pop()
        self.heap_down(0)

        return min.value


    def __str__(self):
        """ This method lets you print the heap, when you're testing your app."""

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

        if self.store[self.parent_index(index)].key > self.store[index].key:
            self.swap(self.parent_index(index), index)
            self.heap_up(self.parent_index(index))


    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        
        if self.left_child_index(index) < len(self.store):
            if self.right_child_index(index) < len(self.store):
                if self.store[self.left_child_index(index)].key < self.store[self.right_child_index(index)].key:
                    smaller_node = self.left_child_index(index)
                else:
                    smaller_node = self.right_child_index(index)
            else:
                smaller_node = self.left_child_index(index)
            if self.store[index].key > self.store[smaller_node].key:
                self.swap(index, smaller_node)
                self.heap_down(smaller_node)

    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """

        self.store[index_1], self.store[index_2] = self.store[index_2], self.store[index_1]


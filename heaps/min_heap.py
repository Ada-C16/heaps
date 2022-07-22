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
            Time Complexity: ? O(log n)
            Space Complexity: ? O(1)
        """
        if value == None:
            value = key
        self.store.append(HeapNode(key, value))
        last_index = len(self.store) - 1
        self.heap_up(last_index)
        return

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: ? O(log n)
            Space Complexity: ? O(1)
        """
        if self.empty():
            return
        self.swap(0, -1)
        result = self.store.pop()
        if not self.empty():
            self.heap_down(0)
        return str(result)
    
    def __str__(self):
        """ This method lets you print the heap, when you're testing your app.
        """
        if len(self.store) == 0:
            return "[]"
        return f"[{', '.join([str(element) for element in self.store])}]"


    def empty(self):
        """ This method returns true if the heap is empty
            Time complexity: ? O(1)
            Space complexity: ? O(1)
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
            Time complexity: ? O(log n)
            Space complexity: ? O(1)
        """
        parent_index = int((index - 1) / 2)
        current_key = self.store[index].key 
        parent_key = self.store[parent_index].key 

        while current_key < parent_key:
            self.swap(index, parent_index)
            index = parent_index
            parent_index = int((index - 1) / 2)
            current_key = self.store[index].key
            parent_key = self.store[parent_index].key 

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
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
            time complexity O(log n)
            space complexity O(1)
        """
        if self.has_left_child(index) and (self.store[index].key > self.store[int((2 * index) + 1)].key):
            left_child_index = (2 * index) + 1
            self.swap(index, left_child_index)
            self.heap_down(left_child_index)

        if self.has_right_child(index) and (self.store[index].key > self.store[int((2 * index) + 2)].key):
            right_child_index = (2 * index) + 2
            self.swap(index, right_child_index)
            self.heap_down(right_child_index)           
        return
 
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp

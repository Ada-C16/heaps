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
            Time Complexity: ?
            Space Complexity: ?
        """
        if value != None:
            self.store.append(HeapNode(key, value))
        else:
            self.store.append(HeapNode(key, key))
            
        self.heap_up(len(self.store) - 1)


    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: O(log n)
            Space Complexity: O(1)
        """
        if len(self.store) == 0:
            return
        self.swap(len(self.store) - 1, 0)
        removed_element = self.store.pop()
        self.heap_down(0)
        return removed_element.value

    
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
        return True if len(self.store) == 0 else False


    def heap_up(self, index):
        """ This helper method takes an index and
            moves the corresponding element up the heap, if 
            it is less than it's parent node until the Heap
            property is reestablished.
            
            This could be **very** helpful for the add method.
            Time complexity: O(log n)
            Space complexity: O(1)
        """
        curr_index = index
        while curr_index > 0:
            parent_index = (curr_index - 1) // 2
            if self.store[curr_index].key < self.store[parent_index].key:
                self.swap(curr_index, parent_index)
                curr_index = parent_index
            else: 
                return
        return


    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
            Time complexity: O(log n)
            Space complexity: O(1)
        """

        curr_index = index
        left_child_index = curr_index * 2 + 1
        right_child_index = curr_index * 2 + 2

        while left_child_index < len(self.store):
            if right_child_index >= len(self.store):
                if self.store[curr_index].key > self.store[left_child_index].key:
                    self.swap(curr_index, left_child_index)
                return
            if self.store[left_child_index].key < self.store[right_child_index].key:
                if self.store[curr_index].key > self.store[left_child_index].key:
                    self.swap(curr_index, left_child_index)
                    curr_index = left_child_index
                else: 
                    return
            else:
                if self.store[curr_index].key > self.store[right_child_index].key:
                    self.swap(curr_index, right_child_index)
                    curr_index = right_child_index
                else:
                    return
            left_child_index = curr_index * 2 + 1
            right_child_index = curr_index * 2 + 2
        return
            
    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp

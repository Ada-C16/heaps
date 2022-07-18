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
            Space Complexity: O(log n)
        """

        if value == None:
            value = key
        node = HeapNode(key, value)
        self.store.append(node)
        self.heap_up(len(self.store) - 1)

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: O(log n)
            Space Complexity: O(log n)
        """

        if len(self.store) == 0:
            return None

        # Swap the first element with the last element
        self.swap(0, len(self.store) - 1)
        # Remove the last element
        removed_element = self.store.pop()
        # Reheapify the heap
        self.heap_down(0)
        return removed_element
    
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
            Space complexity: O(log n)
        """
        if index == 0:
            return
        if self.store[index].key < self.store[(index - 1) // 2].key:
            self.swap(index, (index - 1) // 2)
            self.heap_up((index - 1) // 2)

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """

        if index * 2 + 1 < len(self.store):
            if index * 2 + 2 < len(self.store):
                if self.store[index * 2 + 1].key > self.store[index * 2 + 2].key:
                    if self.store[index * 2 + 1].key < self.store[index].key:
                        self.swap(index, index * 2 + 1)
                        self.heap_down(index * 2 + 1)
                    else:
                        return
                else:
                    if self.store[index * 2 + 2].key < self.store[index].key:
                        self.swap(index, index * 2 + 2)
                        self.heap_down(index * 2 + 2)
                    else:
                        return
            else:
                if self.store[index * 2 + 1].key < self.store[index].key:
                    self.swap(index, index * 2 + 1)
                    self.heap_down(index * 2 + 1)
                else:
                    return

    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp

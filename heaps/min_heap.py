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
            Time Complexity: o(n)
            Space Complexity: o(1)
        """
        if value == None:
            value = key
        node = HeapNode(key, value)

        self.store.append(node)

        index = len(self.store) -1
        while index != None and index != 0:
            index = self.heap_up(index)



    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: o(n)
            Space Complexity: o(1)
        """
        if len(self.store) == 0:
            return

        self.swap(0, len(self.store) - 1)
        root = self.store.pop().value
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
            Time complexity: o(1)
            Space complexity: o(0-1)
        """
        return len(self.store) == 0


    def heap_up(self, index):
        """ This helper method takes an index and
            moves the corresponding element up the heap, if 
            it is less than it's parent node until the Heap
            property is reestablished.
            
            This could be **very** helpful for the add method.
            Time complexity: o(1)
            Space complexity: o(1)
        """

        if self.store[index].key < self.store[(index-1)//2].key:
            self.swap((index-1)//2, index)
            return (index-1)//2


    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        left = index * 2 + 1
        right = index * 2 + 2

        if left < len(self.store):
            if right< len(self.store) and self.store[left].key >= self.store[right].key:
                    swap_for = right
            else:
                swap_for = left

            if self.store[index].key > self.store[swap_for].key:
                self.swap(index, swap_for)
                self.heap_down(swap_for)

    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp

import operator

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
            Time Complexity: O(logn)
            Space complexity: O(logn) because of the call stack
        """
        self.store.append(HeapNode(key, value or key))
        self.heap_up(len(self.store)-1)

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: O(logn)
            Space complexity: O(logn) because of the call stack
        """
        if self.empty():
            return None
        if len(self.store) == 1:
            return self.store.pop().value
        minimum = self.store[0]
        self.store[0] = self.store.pop()
        self.heap_down(0)

        return minimum.value
        


    
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
            Time complexity: O(logn)
            Space complexity: O(logn) because of the call stack
        """
        if index == 0:
            return
        parent = (index-1)//2
        if self.store[parent].key > self.store[index].key:
            self.swap(parent, index)
            self.heap_up(parent)


    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        def get_valid_index_or_none(index):
            if index < len(self.store):
                return index
            else:
                return None

        def get_key_or_none(index):
            if not index:
                return None
            return self.store[index].key

        left_index = get_valid_index_or_none(index * 2 + 1)
        right_index = get_valid_index_or_none(index * 2 + 2)

        left_key = get_key_or_none(left_index)
        right_key = get_key_or_none(right_index)

        index_to_swap = min((node for node in [(left_index, left_key), (right_index, right_key)] if node[1] is not None ), key=operator.itemgetter(1), default=None) 

        if index_to_swap and self.store[index].key > index_to_swap[1]:
            self.swap(index, index_to_swap[0])
            self.heap_down(index_to_swap[0])
        

    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp

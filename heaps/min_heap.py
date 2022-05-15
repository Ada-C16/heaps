

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
        """ Adds a HeapNode instance to the heap
            If value == None the new node's value is set to key
            Time Complexity: O(log n)
            Space Complexity: O(1)
        """
        if value == None: 
            value = key

        node = HeapNode(key, value)

        self.store.append(node)

        self.heap_up(len(self.store) - 1)

    def remove(self):
        """ Removes and returns root element from the heap
            maintaining the heap structure
            Time Complexity: O(log n)
            Space Complexity: O(1)
        """
        if self.empty:
            return None

        self.swap(0, len(self.store) - 1)
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
        return self.store == None


    def heap_up(self, index):
        """ Moves the element identified by index up the heap 
            If it is less than it's parent node until the Heap
            property is reestablished.
            
            Time complexity: ?
            Space complexity: ?
        """
        if index == 0:
            return 

        parent = self.store[(index - 1)//2]

        if self.store[index].key < parent.key:
                self.swap(index, (index - 1)//2)
                self.heap_up((index - 1)//2)

    def heap_down(self, index):
        """ moves element at corresponding index down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        left_index = (index * 2) + 1
        right_index = (index * 2) + 2
        parent = self.store[index]
        left_child = self.store[left_index]
        right_child = self.store[right_index]

        if left_child == None: 
            return 
        
        if left_child and right_child: 
            if parent.key > left_child.key and parent.key > right_child.key: 
                if left_child.key > right_child.key:
                    self.swap(index, right_index)
                    self.heap_down(right_index)
                else: 
                    self.swap(index, left_index)
                    self.heap_down(left_index)
            if parent.key > left_child.key:
                self.swap(index, left_index)
                self.heap_down(left_index)
            if parent.key > right_child.key:
                self.swap(index, right_index)
                self.heap_down(right_index)
            else: 
                return 

        if parent.key > left_child.key: 
            self.swap(index, left_index)
            self.heap_down(left_index)

        return
            
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp

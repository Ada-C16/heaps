

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
            Space Complexity: O(n)
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
        if self.empty():
            return None

        self.swap(0, len(self.store) - 1)
        min = self.store.pop()

        if not self.empty():
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
        return len(self.store) == 0


    def heap_up(self, index):
        """ Moves the element identified by index up the heap 
            If it is less than it's parent node until the Heap
            property is reestablished.
            
            Time complexity: O(1)
            Space complexity: O(n)
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

        if left_index < len(self.store):
            if right_index < len(self.store):
                if self.store[left_index].key < self.store[right_index].key:
                    smaller_child = left_index
                else:
                    smaller_child = right_index
            else: 
                smaller_child = left_index

            if parent.key > self.store[smaller_child].key:
                self.swap(index, smaller_child)
                self.heap_down(smaller_child)

    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp

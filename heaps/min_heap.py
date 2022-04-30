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
        if value is None:
            self.store.append(HeapNode(key, key))
        else:
            self.store.append(HeapNode(key, value))
        self.heap_up(len(self.store)-1)

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: O(log n)
            Space Complexity: O(1)
        """
        if self.empty() == True:
            return None
        
        self.swap(0, len(self.store) -1)
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
        parent_index = (index-1)//2
        while parent_index >= 0 and self.store[parent_index].key > self.store[index].key:
            self.swap(index, parent_index)
            index = parent_index
            parent_index = (index-1)//2

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        left_child_index = (2 * index) + 1
        right_child_index = (2 * index) + 2
        if left_child_index < len(self.store) and right_child_index < len(self.store):
            if self.store[left_child_index].key > self.store[right_child_index].key:
                next_root_index = right_child_index
            else:
                next_root_index = left_child_index
        else:
            next_root_index = left_child_index

        if next_root_index < len(self.store) and self.store[next_root_index].key < self.store[index].key:
            self.swap(index, next_root_index)
            self.heap_down(next_root_index)
                
            

    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp


heap = MinHeap()
# Arrange
heap.add(3, "Pasta")
heap.add(57, "Cake")
heap.add(6, "Soup")
heap.add(1, "Pizza")
heap.add(0, "Donuts")
heap.add(16, "Cookies")

returned_items = ["Donuts", "Pizza", "Pasta", "Soup", "Cookies", "Cake"]
# Act
for item in returned_items:
    print(heap.remove())
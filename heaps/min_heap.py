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
        if value == None:
            value = key
        self.store.append(HeapNode(key, value))
        last_index = len(self.store) - 1
        self.heap_up(last_index)
        return

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: ?
            Space Complexity: ?
        """
        pass
        if len(self.store) == 0:
            return None
        top_node = self.store[0]
        #swap first and last
        self.swap(0, -1)
        #remove last
        result = self.store.pop()
        while self.empty() == False:
            self.heap_down(0)
        return result
    
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
            Space complexity: ?
        """
        parent_index = int((index - 1) / 2)
        current_key = self.store[index].key 
        parent_key = self.store[parent_index].key 
        # print(f"parent key is {parent_key}")
        # print(f"current key is {current_key}")

        while current_key < parent_key:
            self.swap(index, parent_index)
            index = parent_index
            parent_index = int((index - 1) / 2)
            current_key = self.store[index].key
            parent_key = self.store[parent_index].key 

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        # i need to figure out how to ensure that an index is within bounds

        # left child
        if index <= len(self.store) - 1 and int((2 * index) + 1) <= len(self.store) - 1:
            while self.store[index].key > self.store[int((2 * index) + 1)].key:
                self.swap(index, int((2 * index) + 1))
                index = int((2 * 1) + 1)
                if index > len(self.store) - 1 or int((2 * index) + 1) > len(self.store) - 1:
                    break

        #right child
        # while self.store[index].key > self.store[int((2 * index) + 2)].key:
        #     self.swap(index, int((2 * index) + 2))
        #     index = int((2 * index) + 2)
        #     if index > len(self.store) - 1:
        #         break
            
        return

    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp

# some_heap = MinHeap()
# some_heap.add(3, "Pasta")
# some_heap.add(6, "Soup")
# some_heap.add(1, "Pizza")
# some_heap.add(0, "Donuts")
# some_heap.add(16, "Cookies")
# some_heap.add(57, "Cake")
# print(some_heap.store)
# for item in some_heap.store:
#     print(item.value)
#     some_heap.remove()
#     print(some_heap.store)
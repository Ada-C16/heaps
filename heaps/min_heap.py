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
        if value == None:
            value = key
        new_node = HeapNode(key,value)

        # add new_node to end of heap
        self.store.append(new_node)
        self.heap_up(len(self.store) - 1)


    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity:  O(log n)
            Space Complexity:  O(1)
        """
        if self.empty():
            return None

        # swap root and last element in heap
        self.swap(0, len(self.store) - 1)
        print(f"We're swapping {self.store[0]} and {self.store[len(self.store) - 1]}")

        # remove last element in list, former root for return
        min = self.store.pop()

        # heapdown new root to its proper place
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
        return self.store == []


    def heap_up(self, index):
        """ This helper method takes an index and
            moves the corresponding element up the heap, if 
            it is less than it's parent node until the Heap
            property is reestablished.
            
            This could be **very** helpful for the add method.
            Time complexity:  O(log n)
            Space complexity: O(1)
        """
        if index == 0:
            return 

        # Which child node -- 1st or 2nd?
        #     the floor operation, //, rounds down
        #     x - 1 // 2 and x - 2 // 2 will always be ==
        parent = (index - 1) // 2

        if self.store[index].key < self.store[parent].key:
            self.swap(index, parent)
            self.heap_up(parent)


    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        child_left = index * 2 + 1
        child_right = index * 2 + 2

        # if child_left
        if child_left < len(self.store):
            # if child_right 
            if child_right < len(self.store):
                # Pick min of children
                if self.store[child_left].key < self.store[child_right].key:
                    child = child_left
                else:
                    child = child_right
            
            else:
                # No child_right, so pick left
                child = child_left

            if self.store[child].key < self.store[index].key:
                self.swap(child, index)
                self.heap_down(child)

    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp



if __name__ == '__main__':

    heap = MinHeap()
    # Arrange
    heap.add(3, "Pasta")
    heap.add(57, "Cake")
    heap.add(6, "Soup")
    heap.add(1, "Pizza")
    # heap.add(0, "Donuts")
    # heap.add(16, "Cookies")


    # Act
    print(heap)
    #  [(0, Donuts), (1, Pizza), (6, Soup), (57, Cake), (3, Pasta), (16, Cookies)]
    # returned_items = ["Donuts", "Pizza", "Pasta", "Soup", "Cookies", "Cake"]
    # print(returned_items)
    # for item in returned_items:
    #     assert heap.remove() == item
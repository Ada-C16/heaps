class HeapNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

class MinHeap1:

    def __init__(self):
        self.store = []
        self.length = 0


    def add(self, key, value = None):
        """ This method adds a HeapNode instance to the heap
            If value == None the new node's value should be set to key
            Time Complexity: O(log n)
            Space Complexity: O(log n)
        """
        
        # create new node O(1)
        new_node = HeapNode(key, value if value else key)

        # append to end of list O(1)
        self.store.append(new_node)
        self.length += 1

        # re sort to maintain order O(log n)
        self.heap_up(self.length - 1)

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: O(log n)
            Space Complexity: O( log n)
        """
        if self.empty():
            return None

        # swap the first and last items O(1)
        self.swap(0, self.length - 1)

        # remove and store the last item which is the minimum O(1)
        result = self.store.pop().value
        self.length -= 1

        # re sort to maintain order
        self.heap_down(0)
        return result


    
    def __str__(self):
        """ This method lets you print the heap, when you're testing your app.
        """
        if self.length == 0:
            return "[]"
        return f"[{', '.join([str(element) for element in self.store])}]"


    def empty(self):
        return self.length == 0


    def heap_up(self, index):
        """ This helper method takes an index and
            moves the corresponding element up the heap, if 
            it is less than it's parent node until the Heap
            property is reestablished.
            
            This could be **very** helpful for the add method.
            Time complexity: O(log n) where n is the length of self.store, because
                at most it traverses log n levels down to the bottom
            Space complexity: O(log n) where n is the length of self.store, because
                at most it adds log n function calls to the stack
        """
        if index == 0:
            # at the root, no parent
            return
        
        parent_index = (index - 1) // 2
        current_node = self.store[index]
        parent_node = self.store[parent_index]

        if parent_node.key <= current_node.key:
            # in correct order
            return

        else:
            # not in correct order. Swap and check again
            self.swap(index, parent_index)
            self.heap_up(parent_index)

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        left_child_index = index * 2 + 1
        right_child_index = index * 2 + 2
        
        if index * 2 + 1 > self.length - 1:
            # no children, can't heap down any further
            return

        elif index * 2 + 2 > self.length - 1:
            # only left child
            compare_key = self.store[index * 2 + 1].key
            swap_index = index * 2 + 1

        else:
            # both children
            compare_key = self.store[right_child_index].key if self.store[right_child_index].key < self.store[left_child_index].key else self.store[left_child_index].key
            swap_index = right_child_index if self.store[right_child_index].key < self.store[left_child_index].key else left_child_index

        if self.store[index].key <= compare_key:
            # in order
            return
        else:
            # not in correct order. Swap and check again
            self.swap(index, swap_index)
            self.heap_down(swap_index)


    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp

class MinHeap(MinHeap1):
    # for sorting in place

    def __init__(self, l = None):
        self.store = l if l else []
        self.length = 0

    def add(self, key, value = None):

        # create new node O(1)
        new_node = HeapNode(key, value if value else key)

        # append to end of list O(1)
        if self.length >= len(self.store):
            self.store.append(new_node)
        else:
            self.store[self.length] = new_node
        self.length += 1

        # re sort to maintain order O(log n)
        self.heap_up(self.length - 1)

    def remove(self):

        if self.empty():
            return None

        # swap the first and last items O(1)
        self.swap(0, self.length - 1)

        # remove and store the last item which is the minimum O(1)
        result = self.store.pop(self.length - 1).value
        self.length -= 1

        # re sort to maintain order
        self.heap_down(0)
        return result

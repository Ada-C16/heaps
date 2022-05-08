class HeapNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        if self.value:
            return str(self.value)
        else:
            return str(self.key)

    def __repr__(self):
        return str(self.value)


class MinHeap:

    def __init__(self):
        self.store = []
        self.length = 0

    def add(self, key, value=None):
        """ This method adds a HeapNode instance to the heap
            If value == None the new node's value should be set to key
            Time Complexity: ?
            Space Complexity: ?
        """
        self.store.append(HeapNode(key, value))
        self.length +=1
        self.heap_up(self.length-1)

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: O(logn)
            Space Complexity: O(1)
        """
        if self.length>1:
            self.swap(0, self.length-1)
            removed = self.store.pop()
            self.length-=1
            self.heap_down(0)
            return removed.value if removed.value else removed.key
        elif self.length==1:
            node = self.store.pop()
            return node.value if node.value else node.key
        else:
            return None

    def __str__(self):
        """ This method lets you print the heap, when you're testing your app.
        """
        if self.length == 0:
            return "[]"
        return f"[{', '.join([str(element) for element in self.store])}]"

    def empty(self):
        """ This method returns true if the heap is empty
            Time complexity: O(1)
            Space complexity: O(1)
        """
        if not self.store:
            return None 
        

    def heap_up(self, index):
        """ This helper method takes an index and
            moves the corresponding element up the heap, if 
            it is less than it's parent node until the Heap
            property is reestablished.

            This could be **very** helpful for the add method.
            Time complexity: O(logn)
            Space complexity: O(1)
        """
        # Finding parent index (if index % 2 != 0 -> then left child else right)
        # IndexLchild = Iparent * 2 + 1
        # IndexRchild = Iparent * 2 + 2
        parent_ind = int((index-1)/2) if (index % 2 != 0) else int(index/2 - 1)
        # Check to see if parent value is greater than child
        if parent_ind >= 0 and self.store[parent_ind].key > self.store[index].key:
            self.swap(parent_ind, index)
            self.heap_up(parent_ind)

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        lhs_child = index*2 + 1
        rhs_child = index*2 + 2
        if rhs_child>=self.length:
            child = lhs_child
        elif lhs_child>=self.length:
            return
        else:
            child = lhs_child if self.store[lhs_child].key<self.store[rhs_child].key else rhs_child
        if child<len(self.store) and self.store[child].key < self.store[index].key:
            self.swap(index, child)
            self.heap_down(child)

    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp

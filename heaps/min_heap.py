from turtle import left, right


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
        if not value:
            value = key
     
        self.store.append(HeapNode(key, value))
        self.heap_up(len(self.store)-1)


    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: O(log n)
            Space Complexity: O(1)

            First, swap the last leaf & the root node
            Delete the last leaf (last item in the array)
            Then heap-down the new root, to reestablish the heap property
        """
        if len(self.store) == 0:
            return None
        
        last_node_idx = len(self.store)-1
        self.swap(last_node_idx, 0)
        removed = self.store.pop()
        self.heap_down(0)
        return removed.value


    
    def __str__(self):
        """ This method lets you print the heap, when you're testing your app.
        """
        if len(self.store) == 0:
            return "[]"
        return f"[{', '.join([str(element) for element in self.store])}]"


    def empty(self):
        """ This method returns true if the heap is empty
            Time complexity: O(n)
            Space complexity: O(1)
        """
        if len(self.store) == 0:
            return True


    def heap_up(self, index):
        """ This helper method takes an index and
            moves the corresponding element up the heap, if 
            it is less than it's parent node until the Heap
            property is reestablished.
            
            This could be **very** helpful for the add method.
            Time complexity: O(log n)
            Space complexity: O(1)
        """
        if index == 0:
            return
        if self.store[index].key < self.store[(index-1) // 2].key:
            self.swap(index, (index-1) // 2)
            self.heap_up((index-1) // 2)



    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.

            Find min between left and right child
            Swap root with min child
            Heap down
        """
        left_child = (index * 2) + 1 
        right_child = (index * 2) + 2

        # when current node has no children 
        if left_child > len(self.store):
            return
        # when both left and child exists, find min
        elif left_child < len(self.store) and right_child < len(self.store):
            if self.store[left_child].key < self.store[right_child].key:
                self.swap(index, left_child)
                self.heap_down(left_child)
            else:
                self.swap(index, right_child)
                self.heap_down(right_child)
        # has one child, just the left
        elif left_child < len(self.store):
            if self.store[index].key > self.store[left_child].key:
                self.swap(index, left_child)
                self.heap_down(left_child)

            
    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp

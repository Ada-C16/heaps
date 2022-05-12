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
        # check for value, if no value, set value of new node to key
        if value == None:
            value = key
        
        # if value, create new node and add to self.store, end of heap
        node = HeapNode(key, value)
        self.store.append(node)
        # use heap_up helper to check the value of appended node against parent to order heap 
        self.heap_up(len(self.store) - 1)
        

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: O(log n)
            Space Complexity: O(1)
        """
        # check if empty
        if self.empty():
            return None
        
        # if not empty, swap the last index with the root
        self.swap(0, len(self.store) - 1)
       
        # remove the root and store it
        min = self.store.pop()
        
        # call heap_down helper
        self.heap_down(0)
        
        #return the value of the root - the min value
        return str(min.value)
        
    
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
            Space complexity:  makes a recursive call
        """
        # compare the index to the parent index and if larger, swap node positions 
       
        
        if index == 0:
            return None
        
        # use swap helper to swap the node with the parent node

        parent = (index - 1) // 2
        if self.store[index].key < self.store[parent].key:
            self.swap(index, parent)
            #continue to heap_up until the root is reached and every node ordered correctly 
            self.heap_up(parent)

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        
        left = index * 2 + 1
        right = index * 2 + 2

        # check if out of range and determine if which node is smaller
        if left < len(self.store):
            
            # set min_child to left node if right child is larger or if there is no right child
            if right < len(self.store):
                if self.store[left].key < self.store[right].key:
                    smaller = left
                else:
                    smaller = right
            else:
                smaller = left
            
            # swap the node with the smaller child node
            if self.store[index].key > self.store[smaller].key:
                self.swap(index, smaller)
                self.heap_down(smaller)
       

    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp

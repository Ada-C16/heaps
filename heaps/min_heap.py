# from queue import Empty
# from turtle import left


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
            Time Complexity: O(1) if adding to rear, else O(logn)
            Space Complexity: O(1)
        """
        if value == None:
            value = key
        
        node = HeapNode(key, value)
        self.store.append(node)
        self.heap_up(len(self.store) - 1)

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: O(logn)
            Space Complexity: O(1)
        """
        if len(self.store) == 0:
            return None
        
        # swap at index 0 and last element
        self.swap(0, len(self.store) -1)
        # remove last element
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
            Time complexity: O(nlogn)
            Space complexity: O(1)
        """
        # return when index = 0
        if index == 0:
            return
        
        # get parent node
        parent = ( index - 1 ) // 2

        # check parent and current index
        if self.store[parent].key > self.store[index].key:
            self.swap(parent, index)
            index = parent
        
            #recursively check until index == 0
            self.heap_up(index)

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
            
            Time complexity: O(nlogn)
            Space complexity: O(1)
        """       
        heap_length = len(self.store)

        left = (index * 2) + 1
        right = (index * 2) + 2

        # check if right/left is valid
        if left < heap_length:
            if right < heap_length:
                # compare the two children and set child to the smaller child
                if self.store[left].key < self.store[right].key:
                    child = left
                else:
                    child = right
            else:
                child = left
        
            # compare child and cuurent index
            if self.store[index].key > self.store[child].key:
                self.swap(child, index)
                index == child
                self.heap_down(index)
        
    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp

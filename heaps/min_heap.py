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
            Time Complexity: log n
            Space Complexity: 1
        """
        if value == None:
            value = key
        
        #make a new node
        new_node = HeapNode(key, value)
        #add in the new node
        self.store.append(new_node)
        #figure out what the very last index is because that is where we added to
        index = len(self.store) - 1
        #shift and restore the heap
        self.heap_up(index)
        

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: log n
            Space Complexity: 1
        """
        if len(self.store) == 0:
            return None
        
        #put the minimum value at the very end
        self.swap(0, len(self.store) - 1)
        #pop it off
        min = self.store.pop()
        #bring down the value we put at the very top
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
            Time complexity: 1
            Space complexity: 1
        """
        return len(self.store) == 0

    def heap_up(self, index):
        """ This helper method takes an index and
            moves the corresponding element up the heap, if 
            it is less than it's parent node until the Heap
            property is reestablished.
            
            This could be **very** helpful for the add method.
            Time complexity: log n
            Space complexity: 1
        """
        #base case
        if index == 0:
            return

        #parent node
        parent = (index - 1)//2
        #list
        array = self.store

        #if the parent is greater than the child
        if array[parent].key > array[index].key:
            #swap
            self.swap(parent, index) 
            #you would need to keep calling this until you have finally restored the heap
            self.heap_up(parent)

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        left = index * 2 + 1 
        right = index * 2 + 2
        array = self.store

        #is there a left child
        if left < len(array):
            #is there a right child
            if right < len(array):
                #which is smaller
                if array[left].key < array[right].key:
                    child_to_swap = left
                else:
                    child_to_swap = right
            #there is no right child
            else:
                child_to_swap = left
            
            #if the child is smaller
            if array[index].key > array[child_to_swap].key:
                #swap them
                self.swap(index, child_to_swap)
                #keep going until the heap is restored
                self.heap_down(child_to_swap)
    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp

    def parent_idx(self, index):
        return index // 2

    def left_child_idx(self, index):
        return index * 2

    def right_child_idx(self, index):
        return index * 2 + 1

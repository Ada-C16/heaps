import re


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
            Space Complexity: ?
        """
        if value == None:
            value = key
        node = HeapNode(key, value)
        #store is my array, which holds the heap
        #so here i am adding the node to the end of my heap
        self.store.append(node)
        #but wait! there's more!
        #this means that the heap is out of order
        #we need to "heap up" aka bubble up this node until it's in the correct position
        #the heap up method is recursive
        self.heap_up(len(self.store) - 1)


    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            (It removes the smallest item)
            And remember that since this is a min heap, we have the root element at index 0

            Time Complexity: O(log n)
            Space Complexity: ?
        """

        if len(self.store) == 0:
            return None

        #best way to do this is to swap the last with first,
        #pop the new last elem,
        #heap down from there

        self.swap(0, len(self.store) - 1)
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
            Time complexity: ?
            Space complexity: ?
        """
        if not self.store:
            return True

    def heap_up(self, index):
        """ This helper method takes an index and
            moves the corresponding element up the heap, if 
            it is less than it's parent node until the Heap
            property is reestablished.
            
            This could be **very** helpful for the add method.
            Time complexity: ?
            Space complexity: ?
        """
        if index == 0:
            return
        
        parent = (index - 1) // 2
        store = self.store
        if store[parent].key > store[index].key:
            self.swap(parent, index)
            self.heap_up(parent)
            #we do this recursively
            #so we check until everything is in the right place



    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        left_child = index * 2 + 1
        right_child = index * 2 + 2
        store = self.store

        if left_child < len(self.store):
            if right_child < len(self.store):
                if store[left_child].key < store[right_child].key:
                    smaller = left_child
                else:
                    smaller = right_child
            else:
                smaller = left_child

            if store[index].key > store[smaller].key:
                self.swap(index, smaller)
                self.heap_down(smaller)
                #another recursive check


    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp


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
        if self.empty():
            return None 

        self.swap(0, len(self.store)-1)
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
        node_to_add = self.store[index]
        current_parent_index = (index - 1)//2
        current_parent_node = self.store[current_parent_index]

        while current_parent_index >= 0 and current_parent_node.key > node_to_add.key:
            self.swap(index, current_parent_index)
            # reset values before continuing to loop 
            index = current_parent_index  
            current_parent_index = (index - 1)//2
            current_parent_node = self.store[current_parent_index]

    # helper for heap_down to determine which of two children is smaller 
    def get_smaller_index(self, left_index, right_index):
        smaller_child_index = left_index 
        if right_index < len(self.store) and\
            self.store[right_index].key < self.store[smaller_child_index].key:
                smaller_child_index = right_index
        return smaller_child_index
      
    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        left_index, right_index = (index * 2 + 1), (index * 2 + 2) 
        
        while left_index < len(self.store):
            smaller_child_index = self.get_smaller_index(left_index, right_index)
            
            # if what's at current idx is less than what's at smaller child's idx, 
            # no need to swap & can break out out loop; else, make a swap!
            if self.store[index].key < self.store[smaller_child_index].key:
                break  
            self.swap(index, smaller_child_index)
            
            # reset values before continuing to loop
            index = smaller_child_index
            left_index = index * 2 + 1 
            right_index = index * 2 + 2 
        

    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp

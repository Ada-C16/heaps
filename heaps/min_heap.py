from cgitb import small


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
            Space Complexity: O(log n)
        """
        if value == None:
            value = key
        item = HeapNode(key, value)
        self.store.append(item)
        self.heap_up(len(self.store)-1)

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: O(log n)
            Space Complexity: O(log n)
        """
        if self.empty():
            return None
        
        self.swap(0, -1)

        removed_value = self.store.pop()

        self.heap_down(0)

        return removed_value.value

    
    def __str__(self):
        """ This method lets you print the heap, when you're testing your app.
        """
        if self.empty():
            return "[]"
        return f"[{', '.join([str(element) for element in self.store])}]"


    def empty(self):
        """ This method returns true if the heap is empty
            Time complexity: O(1)
            Space complexity: O(1)
        """
        return not self.store


    def heap_up(self, index):
        """ This helper method takes an index and
            moves the corresponding element up the heap, if 
            it is less than it's parent node until the Heap
            property is reestablished.
            
            This could be **very** helpful for the add method.
            Time complexity: O(log n)
            Space complexity: O(log n)
        """
        if self.empty():
            return

        if index != 0:
            compare_index = (index - 1) // 2
            if self.store[index].key < self.store[compare_index].key:
                self.swap(index, compare_index)
                self.heap_up(compare_index)
        
        return

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        if self.empty():
            return

        left_child_index = index * 2 + 1
        right_child_index = index * 2 + 2

        if left_child_index < len(self.store):
            if right_child_index < len(self.store):
                if self.is_left_index_smaller(left_child_index, right_child_index):
                # smaller_value = self.find_smaller_key(right_child_index, left_child_index)
                # if smaller_value == left_child_index:
                    self.swap(index, left_child_index)
                    self.heap_down(left_child_index)
                else:
                    if self.store[index].key > self.store[right_child_index].key:
                        self.swap(index, right_child_index)
                        self.heap_down(right_child_index)
            else:
                if self.is_left_index_smaller(left_child_index, index):
                    self.swap(index, left_child_index)
                    self.heap_down(left_child_index)

        return

# I started with this helper method, but then switched to the other one
    # def find_smaller_key(self, index_1, index_2):
    #     if self.store[index_1].key < self.store[index_2].key:
    #         return index_1
    #     else:
    #         return index_2

# I know this isn't that helpful, but it helped me make more sense of what was happening
# in the heap_down method
    def is_left_index_smaller(self, index_1, index_2):
        if self.store[index_1].key < self.store[index_2].key:
                return True
        return False
    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp

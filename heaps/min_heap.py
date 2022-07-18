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
    
        if value == None:
            value = key

        node = HeapNode(key, value)
        self.store.append(node)
        self.heap_up(len(self.store) - 1)

    def remove(self):
    
        if len(self.store) == 0:
            return None

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
        
        return len(self.store) == 0


    def heap_up(self, index):
    
        if index == 0:
            return
        
        parent = (index - 1) // 2
        store = self.store
        if store[parent].key > store[index].key:
            self.swap(parent, index)
            self.heap_up(parent)

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves it up the heap if it's smaller
            than it's parent node.
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

    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp
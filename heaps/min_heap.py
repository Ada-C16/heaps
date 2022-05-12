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
            Time Complexity: O(log n) where n is the length of self.store (??)
            Space Complexity: O(1)
        """
        if not value:
            value = key
        
        node = HeapNode(key, value)
        self.store.append(node) 
        self.heap_up(len(self.store) - 1) 

    def heap_up(self, index):
        """ This helper method takes an index and
            moves the corresponding element up the heap, if 
            it is less than it's parent node until the Heap
            property is reestablished.
            
            This could be **very** helpful for the add method.
            Time complexity: O(log n) where n is the length of self.store (??) 
            Space complexity: O(1)
        """
        if index == 0:
            return

        curr = self.store[index]
        if index % 2 == 0: 
            parent_index = (index // 2) - 1
        else:
            parent_index = index // 2 

        parent_node = self.store[parent_index]

        if parent_node.key > curr.key:
            self.swap(index, parent_index) 
            self.heap_up(parent_index)
        else:
            return

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: ?
            Space Complexity: ?
        """
        if self.empty():
            return None

        self.swap(0, len(self.store) - 1)

        removed = self.store.pop()

        self.heap_down(0)

        return removed.value

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        if index >= len(self.store) - 1:
            return

        curr = self.store[index]

        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        if left_child_index >= len(self.store):
            left_child_index = None
        if right_child_index >= len(self.store):
            right_child_index = None

        if not left_child_index and not right_child_index:
            return
        elif not left_child_index:
            compare_index = right_child_index
        elif not right_child_index:
            compare_index = left_child_index
        else:
            left_child = self.store[left_child_index]
            right_child = self.store[right_child_index]
            compare_index = left_child_index if left_child.key < right_child.key else right_child_index

        compare_node = self.store[compare_index]
        if curr.key > compare_node.key:
            self.swap(compare_index, index)
            self.heap_down(compare_index)
        else:
            return

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
        if len(self.store) > 0:
            return False

        return True

    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp


def heap_sort(l):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(n log n)
        Space Complexity: O(n)
    """
    if len(l) <= 1:
        return l

    heap = MinHeap()

    for item in l:
        heap.add(item)

    sorted = []

    while heap.store:
        item = heap.remove()
        sorted.append(item)

    return sorted

l = [5, 27, 3, 16, 50]
heap_sort(l)
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
        value = key if value is None else value
        self.store.append(HeapNode(key, value))
        last_index = len(self.store) - 1
        self.heap_up(last_index)

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: O(log n)
            Space Complexity: O(log n)
        """
        if self.empty():
            return None

        self.swap(0, len(self.store) - 1)
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
            Time complexity: O(1)
            Space complexity: O(1)
        """
        return len(self.store)== 0


    def heap_up(self, index):
        """ This helper method takes an index and
            moves the corresponding element up the heap, if
            it is less than it's parent node until the Heap
            property is reestablished.

            This could be **very** helpful for the add method.
            Time complexity: O(log n)
            Space complexity: O(log n)
        """
        if index == 0:
            return
        current_node = self.store[index]
        parent_index = (index - 1) // 2
        parent_node = self.store[parent_index]

        if parent_node.key > current_node.key:
            self.swap(index, parent_index)
            self.heap_up(parent_index)


    def heap_down(self, index):
        """ This helper method takes an index and
            moves the corresponding element down the heap if it's
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        child1_index = index * 2 + 1
        child2_index = index * 2 + 2

        if child1_index >= len(self.store):
            return
        elif child2_index >= len(self.store):
            smaller_child_index = child1_index
        else:
            child1 = self.store[child1_index]
            child2 = self.store[child2_index]
            smaller_child_index = child1_index if child1.key < child2.key else child2_index

        if self.store[index].key < self.store[smaller_child_index].key:
            return
        self.swap(index, smaller_child_index)
        return self.heap_down(smaller_child_index)


    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp

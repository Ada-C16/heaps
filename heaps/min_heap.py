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

    def add(self, key, value=None):
        """ This method adds a HeapNode instance to the heap
            If value == None the new node's value should be set to key
            Time Complexity: Ologn
            Space Complexity: On
        """
        if value is None:
            value = key

        node = HeapNode(key, value)

        self.store.append(node)
        index = len(self.store) - 1

        self.heap_up(index)

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: Ologn
            Space Complexity: O1
        """
        if self.empty():
            return None

        self.swap(0, len(self.store)-1)
        result = self.store.pop()
        self.heap_down(0)

        return result.value

    def __str__(self):
        """ This method lets you print the heap, when you're testing your app.
        """
        if len(self.store) == 0:
            return "[]"
        return f"[{', '.join([str(element) for element in self.store])}]"

    def empty(self):
        """ This method returns true if the heap is empty
            Time complexity: O1
            Space complexity: 01
        """
        return len(self.store) == 0

    def heap_up(self, index):
        """ This helper method takes an index and
            moves the corresponding element up the heap, if 
            it is less than it's parent node until the Heap
            property is reestablished.

            This could be **very** helpful for the add method.
            Time complexity: Ologn
            Space complexity: O1
        """
        if index == 0:
            return None

        # left = index * 2 +
        parent = (index - 1) // 2

        if self.store[index].key < self.store[parent].key:
            self.swap(index, parent)
            self.heap_up(parent)

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
            Time Complexity: Ologn
            Space Complexity: O1
            [2, 5, 3, 6 ]
             0  1  2  3
        """
        left = index * 2 + 1
        right = index * 2 + 2

        if left < len(self.store):  # check if left node is valid
            if right < len(self.store):  # determine if left or right is smaller
                if self.store[left].key < self.store[right].key:
                    smaller_child = left
                    self.swap(index, smaller_child)
                    self.heap_down(smaller_child)
                else:
                    smaller_child = right
                    self.swap(index, smaller_child)
                    self.heap_down(smaller_child)
            elif self.store[index].key > self.store[left].key:
                smaller_child = left
                self.swap(index, smaller_child)
                self.heap_down(smaller_child)

    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp

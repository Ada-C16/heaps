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
        """This method adds a HeapNode instance to the heap
        If value == None the new node's value should be set to key
        Time Complexity: ?
        Space Complexity: ?
        """
        if value == None:
            value = key

        self.store.append(HeapNode(key, value))
        self.heap_up(len(self.store) - 1)

    def remove(self):
        """This method removes and returns an element from the heap
        maintaining the heap structure
        Time Complexity: ?
        Space Complexity: ?
        """
        if len(self.store) == 0:
            return None

        self.swap(0, len(self.store) - 1)  # swap first w/ last
        removed = self.store.pop()  # remove the last node
        self.heap_down(0)  # restructure the heap

        return removed.value

    def __str__(self):
        """This method lets you print the heap, when you're testing your app."""
        if len(self.store) == 0:
            return "[]"
        return f"[{', '.join([str(element) for element in self.store])}]"

    def empty(self):
        """This method returns true if the heap is empty
        Time complexity: ?
        Space complexity: ?
        """
        return self.store == []

    def heap_up(self, index):
        """This helper method takes an index and
        moves the corresponding element up the heap, if
        it is less than it's parent node until the Heap
        property is reestablished.

        This could be **very** helpful for the add method.
        Time complexity: ?
        Space complexity: ?
        """
        if self.empty():
            return

        if index != 0:
            check = (index - 1) // 2
            if self.store[index].key < self.store[check].key:
                self.swap(index, check)

            self.heap_up(check)
        return

    def heap_down(self, index):
        """This helper method takes an index and
        moves the corresponding element down the heap if it's
        larger than either of its children and continues until
        the heap property is reestablished.
        """
        left = index * 2 + 1
        right = index * 2 + 2
        store = self.store
        if left < len(self.store):
            if right < len(self.store):
                if store[left].key < store[right].key:
                    less = left
                else:
                    less = right
            else:
                less = left

            if store[index].key > store[less].key:
                self.swap(index, less)
                self.heap_down(less)

    def swap(self, index_1, index_2):
        """Swaps two elements in self.store
        at index_1 and index_2
        used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp


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
            Time Complexity: ?
            Space Complexity: ?
        """
        new_node = HeapNode(key, value)
        if value == None:
            new_node.value = key
        self.store.append(new_node)
        if len(self.store) > 1:
            index = len(self.store) - 1
            self.heap_up(index)

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: ?
            Space Complexity: ?
        """
        if self.empty():
            return None
        # root_node_index = 0
        # last_node_index = len(self.store) - 1
        self.swap(0, len(self.store)-1)
        # storing this node to remove later
        node_to_remove = self.store.pop()
        self.heap_down(0)
        return node_to_remove.value

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
        return len(self.store) == 0

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
        parent_idx = (index - 1) // 2
        if self.store[parent_idx].key > self.store[index].key:
            self.swap(parent_idx, index)
            self.heap_up(parent_idx)

    def heap_down(self, index):
        """ This helper method takes an index and
            moves the corresponding element down the heap if it's
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        heap = self.store
        left_child_idx = (index * 2) + 1
        right_child_idx = (index * 2) + 2
        if left_child_idx < len(heap):
            if right_child_idx < len(heap):
                if heap[left_child_idx].key < heap[right_child_idx].key:
                    smaller = left_child_idx
                else:
                    smaller = right_child_idx
            else:
                # when there is no right child
                smaller = left_child_idx
            if heap[index].key > heap[smaller].key:
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

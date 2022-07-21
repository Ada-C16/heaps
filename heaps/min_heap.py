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
        if value == None:
            value = key
        new_node = HeapNode(key, value)

        self.store.append(new_node)
        self.heap_up(len(self.store) - 1)

    def remove(self):
        if self.empty():
            return None
        self.swap(0, len(self.store) - 1)

        min = self.store.pop()
        self.heap_down(0)

        return min.value

    def __str__(self):
        """This method lets you print the heap, when you're testing your app."""
        if len(self.store) == 0:
            return "[]"
        return f"[{', '.join([str(element) for element in self.store])}]"

    def empty(self):
        return self.store == []

    def heap_up(self, index):
        if index == 0:
            return

        parent = (index - 1) // 2

        if self.store[index].key < self.store[parent].key:
            self.swap(index, parent)
            self.heap_up(parent)

    def heap_down(self, index):
        child_left = index * 2 + 1
        child_right = index * 2 + 2

        # if child_left
        if child_left < len(self.store):
            # if child_right
            if child_right < len(self.store):
                # Pick min of children
                if self.store[child_left].key < self.store[child_right].key:
                    child = child_left
                else:
                    child = child_right

            else:
                # No child_right, so pick left
                child = child_left

            if self.store[child].key < self.store[index].key:
                self.swap(child, index)
                self.heap_down(child)

    def swap(self, index_1, index_2):
        """Swaps two elements in self.store
        at index_1 and index_2
        used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp


class ArrayDeque:
    """Deque implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty deque."""
        self._data = []
    
    def add_first(self, e):
        self._data = [e] + self._data
        
    def add_last(self, e):
        self._data.append(e)
        
    def delete_first(self):
        value = self._data[0]
        self._data = self._data[1:]
        return value
        
    def delete_last(self):
        value = self._data[-1]
        self._data = self._data[:-1]
        return value
        
    def first(self):
        if self.is_empty():
            raise "Deque is empty"
        return self._data[0]
    
    def last(self):
        if self.is_empty():
            raise "Deque is empty"
        return self._data[-1]

    def is_empty(self):
        """Return True if the queue is empty."""
        return len(self._data) == 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return len(self._data)
    
    def __str__(self):
        return str(self._data)

if __name__ == '__main__':
    D = ArrayDeque()
    print("Command \t|\t Return \t|\t Deque")
    print("D.add_last(5)", "\t|\t", D.add_last(5), "\t|\t", str(D))
    print("D.add_first(3)", "\t|\t", D.add_first(3), "\t|\t", str(D))
    print("D.add_first(7)", "\t|\t", D.add_first(7), "\t|\t", str(D))
    print("D.first()", "\t|\t", D.first(), "\t|\t", str(D))
    print("D.delete_last()", "\t|\t", D.delete_last(), "\t|\t", str(D))
    print("len(D)", "\t|\t", len(D), "\t|\t", str(D))
    print("D.delete_last()", "\t|\t", D.delete_last(), "\t|\t", str(D))
    print("D.delete_last()", "\t|\t", D.delete_last(), "\t|\t", str(D))
    print("D.add_first(6)", "\t|\t", D.add_first(6), "\t|\t", str(D))
    print("D.last()", "\t|\t", D.last(), "\t|\t", str(D))
    print("D.add_first(8)", "\t|\t", D.add_first(8), "\t|\t", str(D))
    print("D.is_empty()", "\t|\t", D.is_empty(), "\t|\t", str(D))
    print("D.last()", "\t|\t", D.last(), "\t|\t", str(D))
    
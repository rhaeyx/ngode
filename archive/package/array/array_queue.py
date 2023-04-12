
class ArrayQueue:
  """FIFO queue implementation using a Python list as underlying storage."""
  DEFAULT_CAPACITY = 10          # moderate capacity for all new queues

  def __init__(self):
    """Create an empty queue."""
    self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
    self._size = 0
    self._front = 0

  def __len__(self):
    """Return the number of elements in the queue."""
    return self._size

  def is_empty(self):
    """Return True if the queue is empty."""
    return self._size == 0

  def first(self):
    """Return (but do not remove) the element at the front of the queue.

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Empty('Queue is empty')
    return self._data[self._front]

  def dequeue(self):
    """Remove and return the first element of the queue (i.e., FIFO).

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Empty('Queue is empty')
    answer = self._data[self._front]
    self._data[self._front] = None         # help garbage collection
    self._front = (self._front + 1) % len(self._data)
    self._size -= 1
    return answer

  def enqueue(self, e):
    """Add an element to the back of queue."""
    if self._size == len(self._data):
      self._resize(2 * len(self.data))     # double the array size
    avail = (self._front + self._size) % len(self._data)
    self._data[avail] = e
    self._size += 1

  def _resize(self, cap):                  # we assume cap >= len(self)
    """Resize to a new list of capacity >= len(self)."""
    old = self._data                       # keep track of existing list
    self._data = [None] * cap              # allocate list with new capacity
    walk = self._front
    for k in range(self._size):            # only consider existing elements
      self._data[k] = old[walk]            # intentionally shift indices
      walk = (1 + walk) % len(old)         # use old size as modulus
    self._front = 0                        # front has been realigned

if __name__ == '__main__':
  S = ArrayQueue()                 # contents: [ ]
  S.enqueue(5)                     # contents: [5]
  S.enqueue(3)                     # contents: [5, 3]
  print(len(S))                    # contents: [5, 3];    outputs 2
  print(S.dequeue())               # contents: [3];       outputs 5
  print(S.is_empty())              # contents: [3];       outputs False
  print(S.dequeue())               # contents: [ ];       outputs 3
  print(S.is_empty())              # contents: [ ];       outputs True
  S.enqueue(7)                     # contents: [7]
  S.enqueue(9)                     # contents: [7, 9]
  print(S.first())                 # contents: [7, 9];    outputs 7
  S.enqueue(4)                     # contents: [7, 9, 4]
  print(len(S))                    # contents: [7, 9, 4]; outputs 3
  print(S.dequeue())               # contents: [9, 4];    outputs 7
  S.enqueue(6)                     # contents: [9, 4, 6]
  S.enqueue(8)                     # contents: [9, 4, 6, 8]
  print(S.dequeue())               # contents: [4, 6, 8]; outputs 9
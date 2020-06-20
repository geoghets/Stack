# enqueue - add and item to start of list at list[0]
# dequeue - remove and item from the end of list (remove list[-1]
class Queue:
    def __init__(self):
        self.list_ = []

    # pop list_ and then print the value you just popped
    # if the list is empty print None
    def dequeue(self):
        if len(self.list_) == 0:
            a = None
        else:
            a = self.list_[-1]
            self.list_.pop()
        return a

    # add an item
    def enqueue(self,i):
        self.list_.insert(0,i)


s = Queue()
s.enqueue("a")
s.enqueue("b")
s.enqueue("c")

assert s.dequeue() == "c"
assert s.dequeue() == "b"
s.enqueue("B")
s.enqueue("C")
assert s.dequeue() == "C" # I switched this line
assert s.dequeue() == "B" # with this line
assert s.dequeue() == "a"
assert s.dequeue() == None







# assert( s.pop(), "c")
# assert( s.pop(), "b")
# s.push("B")
# s.push("C")
# assert( s.pop(), "B")
# assert( s.pop(), "C")
# assert( s.pop(), "a")
# assert( s.pop(), None)



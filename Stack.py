
class Stack:
    def __init__(self):
        self.list_ = []

    # pop list_ and then print the value you just popped
    # if the list is empty print None
    def pop(self):
        if len(self.list_) == 0:
            a = None
        else:
            a = self.list_[-1]
            self.list_.pop()
        return a

    # add an item
    def push(self,i):
        self.list_.append(i)


s = Stack()
s.push("a")
s.push("b")
s.push("c")

assert s.pop() == "c"
assert s.pop() == "b"
s.push("B")
s.push("C")
assert s.pop() == "C" # I switched this line
assert s.pop() == "B" # with this line
assert s.pop() == "a"
assert s.pop() == None


# assert( s.pop(), "c")
# assert( s.pop(), "b")
# s.push("B")
# s.push("C")
# assert( s.pop(), "B")
# assert( s.pop(), "C")
# assert( s.pop(), "a")
# assert( s.pop(), None)



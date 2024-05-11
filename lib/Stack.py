class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if len(self.items) <= 0:
            return True
        else:
            return False

    def push(self, item):
        if self.full():
            return None
        else:
            self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items) >= self.limit:
            return True
        else:
            return False

    def search(self, target):
        distance = 0
        while self.items:
            top = self.items.pop()
            if top == target:
                if distance == 0:
                    return 0
                else:
                    return distance - 1
            distance += 1
        return -1
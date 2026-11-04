import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.q_size = 0

    def put(self, x):
        new_node = Node(x)
        if self.q_size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.q_size += 1

    def get(self):
        if self.q_size == 0:
            return "error"

        val = self.head.value
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self.q_size -= 1
        return val

    def size(self):
        return self.q_size


if __name__ == '__main__':
    n = int(input().strip())
    q = Queue()

    for _ in range(n):
        command = input().strip().split()

        if command[0] == "put":
            q.put(int(command[1]))
        elif command[0] == "get":
            print(q.get())
        elif command[0] == "size":
            print(q.size())
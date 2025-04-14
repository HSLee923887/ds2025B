class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0


    def enqueue(self, data):
        self.size += 1              #인큐(선입) 1씩 증가
        node = Node(data)           #새 노드 생성
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.link = node
            self.rear = node


q = Queue()
q.enqueue("DataBase")
q.enqueue("Data Structure")
print(q.size, q.front.data, q.rear.data)


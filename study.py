class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


class Stack:
    def __init__(self):
        #self.items = list()
        self.top = None

    # def push(self, item):
    #     self.items.append(item)
    def push(self, data):
        node = Node(data)               #입력받은 노드를 만듦
        if self.top is None:            #스택 처음 만드는거면
            self.top = node             #방금 넣은 노드가 제일 위
        else:
            node.link = self.top        #제일 위였던 놈을 방금 넣은 노드의 "링크"가 가리키게 함
            self.top = node             #그리고 방금 들어오는 노드는 제일 위가 됨

    def pop(self):
        if self.top is None:            #스택이 비었는지 확인
            return "Stack is empty!"    #스택이 비었으면 반환
        popped_node = self.top          #제일 마지막에 들어간 데이터를 임시 변수가 가리킴
        self.top = self.top.link        #self.top은 원래 제일 위에 있던 데이터의 전 데이터를 가리킴
        popped_node.link = None # !     #마지막 데이터의 연결을 끊음
        return popped_node.data         #마지막 데이터 반환

    def __str__(self):
        if self.top is None:
            return "Stack is empty"
        stack_str = ""
        current = self.top  # ✅ 스택을 따라갈 임시 변수. 임시 변수를 안 쓰면 본래의 스택을 파괴할 수 있음 주의
        while current:
            stack_str += f"{current.data} -> "
            current = current.link
        return stack_str + "end"


s1 = Stack()
s1.push("Data structure")
s1.push("Database")
# print(s1.pop())
# print(s1.pop())
print(s1)
for i in range(3):
     print(s1.pop())
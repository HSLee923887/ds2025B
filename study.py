import random
class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link            #노드 형태 |data|link|


class LinkedList:
    def __init__(self):
        self.head = None            #기준이 되는 머리(시작) 노드

    def append(self, data):
        if not self.head:           #링크드리스트가 노드가 하나도 없는 상태면
            self.head = Node(data)  #새 노드를 head에 연결
            return
        current = self.head         #일단 머리를 가리키게 함
        while current.link:         #머리서부터 가리키는 녀석이 있는지 확인
            current = current.link  #처음에 노드10을 가리키니까 current는 노드10이 됨.노드10은 노드-9를 가리키고있으니 true. current는 다시 노드-9가 됨.
        current.link = Node(data)   #append할 값을 추가. 가리키게 함

    def search(self, target):
        current = self.head
        while current.link:
            if current.data == target:
                return f"{target}을(를) 찾았습니다"
            else:
                current = current.link
        return f"{target}은(는) 링크드리스트 안에 존재하지 않습니다"

    def __str__(self):
        node = self.head
        out_texts = ""
        while node is not None:
            #print(node.data)
            #out_texts = out_texts + str(node.data) + " -> "
            out_texts = out_texts + f"{node.data} -> "          #""=""+8, "8 -> ","10 -> ","-9 -> ","end"
            node = node.link
        return out_texts + "end"


ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)
print(ll)
print(ll.search(100))
print(ll.search(10))
for _ in range(10):
     ll.append(random.randint(1, 30))
print(ll.search(27))
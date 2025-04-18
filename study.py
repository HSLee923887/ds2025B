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

    def remove(self, target):
        current = self.head                     #current가 노드8을 가리킴

        if self.head is None:
            return "리스트가 비어 있습니다"

        if self.head.data == target:            #처음에 머리 data검사 지우려는 값이 머리 일 때만 true를 반환 ex) ll.remove(10) 8 != 10
            self.head = self.head.link          #false기 때문에 실행 x
            current.link = None                 #다음 노드와 연결을 끊음
            return
        previous = None                         #변수 None으로 초기화
        while current:                          #current에 값이 있을 때
            if current.data == target:          #8 != 10, 10 == 10
                previous.link = current.link    #실행 안 함, previous.link가 -9를 가리킴(다음 노드 기억)
                current.link = None             #값을 찾으면 다음으로 가는 링크만 끊음
                break
            previous = current                  #previous가 current(노드8)를 가리킴. previous는 link가 None인 노드10을 가리킴
            current = current.link              #current는 노드10을 가리키게 됨(루프O). current는 None이 됨(루프 탈출)

    def search(self, target):
        current = self.head
        while current:
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

ll.remove(10)
ll.remove(8)
ll.remove(15)
ll.remove(20)
print(ll)
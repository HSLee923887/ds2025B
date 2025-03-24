import array

arr = array.array('f', [11, 9, -77, 8]) # 메모리의 같은 공간에 저장하는 법
for i in range(len(arr)):
    print(f"{arr[i]:3} {id(arr[i])}")
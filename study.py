def move_zeros(l):
    zero_idx = 0                        #초기값 0
    for i in range(len(l)):             #l의 길이만큼 반복
        n = l[i]                        #n에 l의 i번째 인덱스 대입
        if n != 0:                      #n이 0이 아니면 (l의 인덱스가 0인지 아닌지 검사하는 부분)
            l[zero_idx] = n             #l의 0~4번째에 n 대입 (0이 아니면 그대로 넣어주는 거임)
            if zero_idx != i:           #만약에 제로idx가 i랑 다르면
                l[i] = 0                #l의 i번째 인덱스에 0 대입.
            zero_idx = zero_idx + 1     #제로idx에 + 1
    return l                            #이 메소드는 리스트에서 0을 뒤로 빼는 기능.


l = [11, 0, 9, 0, -77]
move_zeros(l)
print(l)

# l = [11, 9, -77, 8]
# for i, v in enumerate(l):
#     print(i, v)

# l = [11, 9, -77, 8]
# for i in range(len(l)):
#     print(i, l[i])
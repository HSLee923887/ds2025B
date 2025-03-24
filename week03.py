def move_zeros(a_list):
    zero_index = 0
    for index, n in enumerate(a_list):  # 입력받은 리스트에서 인덱스index와 값n를 순서대로 꺼냄
        if n != 0:                      # 입력받은 리스트의 값이 0이 아닐 때
            a_list[zero_index] = n      # 입력받은 리스트의 zero_index번째에 n를 넣음
            if zero_index != index:     # zero_index가 입력받은 리스트의 인덱스 번호와 다를 때
                a_list[index] = 0       # 입력받은 리스트의 index번째에 0을 넣음
            zero_index += 1
    return(a_list)                      # 리스트를 받아 0이 아닌 값을 뒤로 밀어내는 함수

a_list = [8, 0, 3, 0, 12]
move_zeros(a_list)
print(a_list)
n = int(input("정수 입력 : "))
result = 0
for i in range(1, n+1): #O(n)
    result = result + i
# result = n * (n + 1) // 2  # O(1)
print(result)
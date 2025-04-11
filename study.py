import random

answer = random.randint(1, 100)

win = False
for i in range(7):
    guess = int(input(f"{7-i}번의 기회가 남았습니다. 숫자 입력 : "))

    if guess > answer :
        print("입력하신 수는 정답보다 큰 수 입니다. HIGH")
    elif guess < answer :
        print("입력하신 수는 정답보다 작은 수 입니다. LOW")
    else:
        win = True
        break

if win:
    print("정답입니다! You win!")
else:
    print("You lose. The answer is ", answer, ".")
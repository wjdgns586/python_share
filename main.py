# 4523
# 1234
# 0s 3b
# 하나도 없으면
import random

def non_overlap_random_number():
    random_number = []
    for i in range(4):
        if i == 0:
            number = random.randint(1, 9)

        if i > 0:
            number = random.randint(0, 9)
            while number in random_number:
                number = random.randint(0, 9)

        random_number.append(number)
        print(random_number)

    return random_number


def input_():
    a = input("원하는 숫자를 입력하세요(4자리수): ")

    a = list(map(int, a))
    print(a)
    return a

def check():
    a = input_()
    random_number = non_overlap_random_number()
    strike = 0
    for i in range(4):
        if a[i] == random_number[i]:
            strike += 1
    if strike == 4:
        print("정답입니다.")

    print(strike)

check()







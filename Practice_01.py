import random


def first_game_start():
    print()
    print("랜덤숫자 맞추기 게임을 시작하겠습니다. \n")

    while True:
        count_1 = input("원하는 랜덤생성 숫자 자리수를 입력하세요: ")
        if count_1.isdigit():

            if 0 < int(count_1) < 4:
                break

            elif int(count_1) >= 4:
                print(f"입력하신 값은 {count_1}로 유효하지 않은 값입니다. \n다시 입력해주세요.\n")

            elif int(count_1) < 0:
                print(f"입력하신 값은 {count_1}로 유효하지 않은 값입니다. \n다시 입력해주세요.\n")

        else:
            print()
            print(f"입력하신 값은 {count_1}로 유효하지 않은 값입니다. \n다시 입력해주세요.\n")

    count_1 = int(count_1)

    print()

    while True:
        count_2 = input("원하는 도전 횟수를 입력하세요(10회 초과 불가능): ")

        if count_2.isdigit():

            if 0 < int(count_2) <= 10:
                break

            elif int(count_2) > 10:
                print(f"입력하신 값은 {count_2}회로, 최대 도전횟수 10회를 초과하였습니다. \n다시 입력해주세요.\n")

            elif int(count_2) <= 0:
                print(f"입력하신 값은 {count_2}회로, 0회이하입니다. \n다시 입력해주세요.\n")

        else:
            print()
            print(f"입력한 값은 {count_2}로 유효한 값이 아닙니다. \n\n다시 유요한 값을 입력해 주세요.\n")

    count_2 = int(count_2)

    print()

    print("게임을 시작합니다.")

    return count_1, count_2


def non_overlap_random_number(count):
    random_number = []
    for i in range(count):
        if i == 0:
            number = random.randint(1, 9)

        if i > 0:
            number = random.randint(0, 9)
            while number in random_number:
                number = random.randint(0, 9)

        random_number.append(number)
    random_number_r = list(map(str, random_number))
    sum_random_number = "".join(random_number_r)
    return sum_random_number


def game_restart():
    while True:
        b = input("게임을 계속하고 싶으면, 1을 종료하고 싶으면 0을 입력하세요: ")
        if b.isdigit():
            if int(b) == 0 or int(b) == 1:
                break

            else:
                print()
                print(f"입력한 값은 {b}로 유효한 값이 아닙니다. \n\n다시 유요한 값을 입력해 주세요.\n")

        else:
            print()
            print(f"입력한 값은 {b}로 유효한 값이 아닙니다. \n\n다시 유요한 값을 입력해 주세요.\n")

    return b


def bigger_than_rand_number(a, rand_num, trial, count_2):
    b = 2
    if a > rand_num:
        if trial < count_2:
            print(f"입력하신 값은 {a}입니다. \n\n{a}는 생성된 랜덤숫자보다 큽니다. \n\n{trial}번째 도전입니다.")
            print(f"남은 도전 횟수는 {count_2 - trial}회입니다. \n신중하게 하세요!!!!\n")

            # while True:
            #     count_1 = input("원하는 랜덤생성 숫자 자리수를 입력하세요: ")
            #     if count_1.isdigit():
            #
            #         if 0 < int(count_1) < 4:
            #             break
            #
            #         elif int(count_1) >= 4:
            #             print(f"입력하신 값은 {count_1}로 유효하지 않은 값입니다. \n다시 입력해주세요.\n")
            #
            #         elif int(count_1) < 0:
            #             print(f"입력하신 값은 {count_1}로 유효하지 않은 값입니다. \n다시 입력해주세요.\n")
            #
            #     else:
            #         print()
            #         print(f"입력하신 값은 {count_1}로 유효하지 않은 값입니다. \n다시 입력해주세요.\n")
            #
            # count_1 = int(count_1)

        if trial == count_2:
            print(f"입력하신 값은 {a}입니다. \n\n{a}는 생성된 랜덤숫자보다 큽니다. \n\n{trial}번째 도전입니다.")
            print(f"안타깝지만, 도전가능 횟수{count_2}회를 초과하였습니다. \n\n게임에서 패배하였습니다.\n")
            b = game_restart()
    return b


def smaller_than_rand_number(a, rand_num, trial, count_2):
    b = 2
    if a < rand_num:
        if trial < count_2:
            print(f"입력하신 값은 {a}입니다. \n\n{a}는 생성된 랜덤숫자보다 작습니다. \n\n{trial}번째 도전입니다.")
            print(f"남은 도전 횟수는 {count_2 - trial}회입니다. \n신중하게 하세요!!!!\n")
        if trial == count_2:
            print(f"입력하신 값은 {a}입니다. \n\n{a}는 생성된 랜덤숫자보다 작습니다. \n\n{trial}번째 도전입니다.")
            print(f"안타깝지만, 도전가능 횟수{count_2}회를 초과하였습니다. \n\n게임에서 패배하였습니다.\n")
            b = game_restart()
    return b


def number_finding(count_1, count_2):
    rand_num = int(non_overlap_random_number(count_1))
    print()
    print(f"입력하신 랜덤생성 숫자는 {count_1}자리수이고 그에따라, {count_1}자리수의 랜덤 숫자가 생성되었습니다.")
    print()
    print(f"숫자맞추기 도전기회는 총 {count_2}회입니다.\n\n만약 {count_2}회만에 맞추지 못할시, 게임은 패배로 종료됩니다.")
    print(rand_num)

    b = 2
    trial = 0
    while True:
        if int(b) == 1:
            trial = 0

            count_1, count_2 = first_game_start()

            number_finding(count_1, count_2)
            break


        elif int(b) == 0:
            print()
            print("""-----------------------------------------------------
                    게임을 종료합니다.
-----------------------------------------------------""")
            break

        a = int(input("예상하는 숫자를 입력해주세요: "))
        trial += 1
        if a == rand_num:
            print(f"축하합니다!!! {trial}회만에 맞추셨습니다. \n\n랜덤 숫자는 {rand_num}였습니다!!!")
            b = game_restart()


        else:
            if a > rand_num:
                b = bigger_than_rand_number(a, rand_num, trial, count_2)

            elif a < rand_num:
                b = smaller_than_rand_number(a, rand_num, trial, count_2)


# Coding 본문!!!!

count_1, count_2 = first_game_start()

number_finding(count_1, count_2)




def print_cat():
    cat = [
        " /\\_/\\  ",
        "( o.o ) ",
        " > ^ <  "
    ]
    for _ in range(5):
        for line in cat:
            print(line)
        print()  # 줄바꿈


def print_dog():
    dog = [
        " / \\__",
        "(    @\\___",
        " /         O",
        "/   (_____/",
        "/_____/   U"
    ]
    for _ in range(5):
        for line in dog:
            print(line)
        print()  # 줄바꿈


def print_rabbit():
    rabbit = [
        "  (\\_/)",
        "  (o o)",
        "  ( > )"
    ]
    for _ in range(5):
        for line in rabbit:
            print(line)
        print()  # 줄바꿈


# 무한 반복 시작
while True:
    print("그림 출력 프로그램")
    print("=====================")
    print("1. 고양이")
    print("2. 강아지")
    print("3. 토끼")
    print("0. 프로그램 종료")
    print("=====================")

    n = int(input("선택: "))
    
    if n == 1:
        print("\n고양이")
        print_cat()
    elif n == 2:
        print("\n강아지")
        print_dog()
    elif n == 3:
        print("\n토끼")
        print_rabbit()
    elif n == 0:
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못 입력했습니다. 다시 선택해주세요.\n")
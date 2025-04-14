def print_animal(animal):
    for _ in range(5):
        for line in animal:
            print(line)
        print()  


cat = [
    " /\\_/\\  ",
    "( o.o ) ",
    " > ^ <  "
]

dog = [
    " / \\__",
    "(    @\\___",
    " /         O",
    "/   (_____/ ",
    "/_____/   U"
]

rabbit = [
    "  (\\_/)",
    "  (o o)",
    "  ( > )"
]

def play(n):
    if n == 1:
        print("\n고양이\n")
        print_animal(cat)
    elif n == 2:
        print("\n강아지\n")
        print_animal(dog)
    elif n == 3:
        print("\n토끼\n")
        print_animal(rabbit)
    else:
        print("잘못된 번호입니다. 1~3 중에서 선택해주세요.\n")


while True:
    print("그림 출력 프로그램")
    print("=====================")
    print("1. 고양이")
    print("2. 강아지")
    print("3. 토끼")
    print("0. 프로그램 종료")
    print("=====================")

    try:
        n_str = input("선택(1-3), 종료(0): ")
        n = int(n_str)
    except ValueError:
        print("⚠️ 잘못된 입력입니다. 숫자를 입력해주세요.\n")
        continue

    if n == 0:
        print("프로그램을 종료합니다.")
        break

    play(n)
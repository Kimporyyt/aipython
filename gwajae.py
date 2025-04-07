def print_cat():
    cat = [
        " /\\_/\\  ",
        "( o.o ) ",
        " > ^ <  "
    ]
    for line in cat:
        print(line)

def print_dog():
    dog = [
        " / \\__",
        "(    @\\___",
        " /         O",
        "/   (_____/",
        "/_____/   U"
    ]
    for line in dog:
        print(line)

def print_rabbit():
    rabbit = [
        "  (\\_/)",
        "  (o o)",
        "  ( > )"
    ]
    for line in rabbit:
        print(line)

# 공통 그림 출력 함수
def play():
    print("\n그림 출력 프로그램")
    print("=====================")
    print("1. 고양이")
    print("2. 강아지")
    print("3. 토끼")
    print("0. 종료")
    print("=====================")

    n = int(input("선택: "))

    if n == 1:
        print("\n[고양이]")
        print_cat()
    elif n == 2:
        print("\n[강아지]")
        print_dog()
    elif n == 3:
        print("\n[토끼]")
        print_rabbit()
    elif n == 0:
        return False  # 종료 조건
    else:
        print("잘못 입력했습니다.")
    return True  # 계속 반복

# 5번만 실행
def play_5times():
    for i in range(5):
        print(f"\n[{i+1}/5번째 실행]")
        play()

# 무한 반복, 0 입력 시 종료
def play_infinite():
    count = 1
    while True:
        print(f"\n[{count}번째 실행]")
        if not play():  # False 반환 시 종료
            print("프로그램을 종료합니다.")
            break
        count += 1

# 메인 메뉴
def main_menu():
    while True:
        print("\n🎬 [동물 그림 출력 메인 메뉴]")
        print("1. 5번만 출력하고 종료")
        print("2. 무한 반복 (0 입력 시 종료)")
        print("0. 프로그램 종료")
        choice = input("모드 선택: ")

        if choice == "1":
            play_5times()
        elif choice == "2":
            play_infinite()
        elif choice == "0":
            print("전체 프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")


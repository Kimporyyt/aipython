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

def play():
    print("그림 출력 프로그램")
    print("=====================")
    print("1. 고양이")
    print("2. 강아지")
    print("3. 토 끼")
    print("=====================")
    n = int(input("선택: "))

    if n == 1:
        print("고양이")
        print_cat()
    elif n == 2:
        print("강아지")
        print_dog()
    elif n == 3:
        print("토끼")
        print_rabbit()
    else:
        print("잘못입력")    


print("5번 출력 프로그램 시작")
for i in range(5):
    play()

print("5번 출력 프로그램 종료")

print("0을 입력하면 종료 프로그램 시작 ")
while True: # 무한 반복 (계속 참)
    play()

print("0을 입력하면 종료 프로그램 종료 ")
num = int(input("출력할 구구단의 단을 입력하세요: "))

print(f"\n=== {num}단 ===")
for i in range(1, 10):
    print(f"{num} × {i} = {num * i}")
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def print_animal(animal, title):
    panel_text = "\n".join(animal)
    console.print(Panel(panel_text, title=title, subtitle="🐾 반복 출력 5회", expand=False, border_style="magenta"))
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
    animal_names = {1: "고양이", 2: "강아지", 3: "토끼"}
    animal_data = {1: cat, 2: dog, 3: rabbit}

    if n in animal_data:
        for i in range(5):
            print_animal(animal_data[n], f"{animal_names[n]} 🐾 ({i+1}/5)")
    else:
        print("[bold red]⚠️ 잘못된 번호입니다. 1~3 중에서 선택해주세요.[/bold red]\n")


while True:
    print("[bold cyan]그림 출력 프로그램[/bold cyan]")
    print("[green]=====================[/green]")
    print("1. 🐱 고양이")
    print("2. 🐶 강아지")
    print("3. 🐰 토끼")
    print("0. ❌ 프로그램 종료")
    print("[green]=====================[/green]")

    try:
        n_str = input("선택(1-3), 종료(0): ")
        n = int(n_str)
    except ValueError:
        print("[red]⚠️ 잘못된 입력입니다. 숫자를 입력해주세요.[/red]\n")
        continue

    if n == 0:
        print("[bold yellow]프로그램을 종료합니다.[/bold yellow]")
        break

    play(n)
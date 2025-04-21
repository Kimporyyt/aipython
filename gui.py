import tkinter as tk
from PIL import Image, ImageTk
import os

def show_image(bread_type):
    """선택된 빵 타입에 맞는 이미지를 로드하여 화면에 표시하는 함수"""
    global photo_image

    file_name = f"{bread_type}.jpg"
    file_path = os.path.join(os.path.dirname(__file__), file_name)

    try:
        pil_image = Image.open(file_path)
        max_width = 400
        max_height = 350
        pil_image.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
        photo_image = ImageTk.PhotoImage(pil_image)
        image_label.config(image=photo_image, text="")
        image_label.image = photo_image
        print(f"{bread_type} 이미지 로드 완료.")

    except FileNotFoundError:
        error_message = f"오류: '{file_name}' 파일을 찾을 수 없습니다.\n스크립트와 같은 폴더에 있는지 확인하세요."
        print(error_message)
        image_label.config(text=error_message, image='')
    except Exception as e:
        error_message = f"오류: {file_name} 이미지 로드 중 문제 발생\n{e}"
        print(error_message)
        image_label.config(text=error_message, image='')

# --- GUI 설정 ---
window = tk.Tk()
window.title("빵 사진 보기")
window.geometry("500x500")

photo_image = None

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

# 팥빵 버튼 생성
redbean_button = tk.Button(button_frame, text="팥빵", width=10, command=lambda: show_image('팥빵'))
redbean_button.pack(side=tk.LEFT, padx=5)

# 크로와상 버튼 생성
croissant_button = tk.Button(button_frame, text="크로와상", width=10, command=lambda: show_image('크로와상'))
croissant_button.pack(side=tk.LEFT, padx=5)

# 소보로빵 버튼 생성
soboro_button = tk.Button(button_frame, text="소보로빵", width=10, command=lambda: show_image('소보로빵'))
soboro_button.pack(side=tk.LEFT, padx=5)

image_label = tk.Label(window, text="버튼을 클릭하여 빵을 선택하세요.", compound=tk.CENTER)
image_label.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

window.mainloop()
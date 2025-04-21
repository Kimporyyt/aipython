from PIL import Image, ImageDraw, ImageFont, ImageFilter

image_path = input("이미지 파일 경로를 입력하세요 (예: sample.jpg): ")

try:
    img = Image.open(image_path)
    print("✅ 이미지 열기 성공!")

    img_resized = img.resize((400, 400))
    img_cropped = img_resized.crop((50, 50, 350, 350))
    img_rotated = img_cropped.rotate(45)
    img_gray = img_rotated.convert("L")
    img_text = img_gray.convert("RGB")

    draw = ImageDraw.Draw(img_text)

    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()

    draw.text((10, 10), "Hello, Pillow!", fill=(255, 0, 0), font=font)

    img_blur = img_text.filter(ImageFilter.BLUR)
    output_path = "final_result.jpg"
    img_blur.save(output_path)
    img_blur.show()

    print(f"🎉 이미지 처리 완료! 결과는 '{output_path}'로 저장되었습니다.")

except FileNotFoundError:
    print("❌ 오류: 이미지 파일을 찾을 수 없습니다. 경로를 다시 확인해주세요.")

except Exception as e:
    print(f"⚠️ 예상치 못한 오류 발생: {e}")
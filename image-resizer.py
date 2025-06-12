import os
from PIL import Image

# 📂 入力・出力フォルダパス設定
INPUT_DIR = "images_input"     # 元画像フォルダ
OUTPUT_DIR = "images_output"   # リサイズ・圧縮画像保存フォルダ
MAX_WIDTH = 230                # 希望する最大幅（比率維持）
QUALITY = 70                  # JPG圧縮品質（60～85推奨）


def resize_and_compress(input_path, output_path):
    try:
        img = Image.open(input_path)
        img = img.convert("RGB")  # JPG保存のためRGBに変換

        # 比率を維持してリサイズ
        w_percent = MAX_WIDTH / float(img.size[0])
        h_size = int((float(img.size[1]) * float(w_percent)))
        img = img.resize((MAX_WIDTH, h_size), Image.LANCZOS)

        # ファイル保存
        img.save(output_path, "JPEG", quality=QUALITY, optimize=True)
        print(f"✅ {os.path.basename(input_path)} → 保存完了")
    except Exception as e:
        print(f"❌ エラー発生 - {input_path}: {e}")


def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            input_path = os.path.join(INPUT_DIR, filename)
            output_filename = os.path.splitext(filename)[0] + ".jpg"
            output_path = os.path.join(OUTPUT_DIR, output_filename)
            resize_and_compress(input_path, output_path)


if __name__ == "__main__":
    main()

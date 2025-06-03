import cv2
import pytesseract
import numpy as np
import os
from PIL import Image
from tkinter import Tk, filedialog

# ✔ Path to Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def select_image_file():
    Tk().withdraw()  # Hide root Tk window
    file_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.webp")]
    )
    return file_path

def load_image_with_webp_support(path):
    ext = os.path.splitext(path)[-1].lower()
    if ext == '.webp':
        try:
            pil_img = Image.open(path).convert("RGB")
            cv_img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
            return cv_img
        except Exception as e:
            print(f"❌ Error loading .webp image: {e}")
            return None
    else:
        return cv2.imread(path)

def pre_processing(image_path):
    print(f"📂 Reading image: {image_path}")
    img = load_image_with_webp_support(image_path)

    if img is None:
        print("❌ Error: Could not load the input image.")
        return None

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    denoised = cv2.fastNlMeansDenoising(gray, h=10)
    equalized = cv2.equalizeHist(denoised)
    resized = cv2.resize(equalized, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    thresh = cv2.adaptiveThreshold(resized, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 31, 10)

    os.makedirs('output', exist_ok=True)
    output_path = os.path.join('output', 'preprocessed_image.png')
    cv2.imwrite(output_path, thresh)

    print(f"✅ Preprocessed and saved at: {output_path}")
    return output_path

def text_extraction(output_path):
    if output_path is None or not os.path.exists(output_path):
        print("❌ Invalid image path for OCR.")
        return

    img = cv2.imread(output_path)
    config = "--oem 3 --psm 6"
    recognized_text = pytesseract.image_to_string(img, config=config)

    if recognized_text.strip():
        print("\n✅ Extracted Text:\n")
        print(recognized_text)
        with open('output/final_text.txt', 'w', encoding='utf-8') as f:
            f.write(recognized_text)
    else:
        print("⚠️ No readable text found.")

def main():
    image_path = select_image_file()
    if image_path:
        preprocessed_path = pre_processing(image_path)
        text_extraction(preprocessed_path)
        print("\n🏁 OCR process completed.")
    else:
        print("❌ No file selected.")

if __name__ == "__main__":
    main()

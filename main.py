from flask import Flask, render_template, request, send_from_directory
import cv2
import pytesseract
import numpy as np
import os
from PIL import Image
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'output'

# Create folders if not exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

# Path to Tesseract (for Windows users)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def load_image_with_webp_support(path):
    ext = os.path.splitext(path)[-1].lower()
    if ext == '.webp':
        pil_img = Image.open(path).convert("RGB")
        return cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    return cv2.imread(path)

def preprocess_image(image_path):
    img = load_image_with_webp_support(image_path)
    if img is None:
        return None

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    denoised = cv2.fastNlMeansDenoising(gray, h=10)
    equalized = cv2.equalizeHist(denoised)
    resized = cv2.resize(equalized, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    thresh = cv2.adaptiveThreshold(resized, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 10)

    output_path = os.path.join(app.config['OUTPUT_FOLDER'], 'preprocessed.png')
    cv2.imwrite(output_path, thresh)
    return output_path

def extract_text(image_path):
    img = cv2.imread(image_path)
    config = "--oem 3 --psm 4"
    text = pytesseract.image_to_string(img, config=config)
    return text.strip()

@app.route('/', methods=['GET', 'POST'])
def index():
    extracted_text = None
    uploaded_filename = None
    if request.method == 'POST':
        file = request.files.get('image')
        if file:
            filename = secure_filename(file.filename)
            uploaded_filename = filename
            upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(upload_path)

            preprocessed_path = preprocess_image(upload_path)
            if preprocessed_path:
                extracted_text = extract_text(preprocessed_path)
    return render_template('index.html', extracted_text=extracted_text, uploaded_filename=uploaded_filename)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)

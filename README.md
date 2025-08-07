# 🧠 OCR Web App – Text Extraction from Images using EasyOCR & Flask

This project is a web-based OCR (Optical Character Recognition) application built using **Python**, **Flask**, and **EasyOCR**. It allows users to upload an image (JPEG, PNG, etc.) containing printed or handwritten text and extracts that text using an advanced deep-learning OCR model.

---

## 🔍 What is OCR?

**Optical Character Recognition (OCR)** is a technology that detects and extracts text from images such as scanned documents, photos of signs, handwritten notes, and more. OCR bridges the gap between image-based and text-based information.

---

## 📚 Tesseract OCR vs EasyOCR – A Brief Theory

### ✅ Tesseract OCR:
- Developed by HP and maintained by Google.
- Uses traditional image processing + LSTM (Long Short-Term Memory) neural networks.
- Best for clean documents, scanned text, and printed text.
- Supports over 100 languages.
- **Needs good image preprocessing** for accurate results (grayscale, thresholding, etc.).

### ✅ EasyOCR:
- Built using deep learning (PyTorch-based).
- Supports over 80 languages including non-Latin scripts.
- Works better out-of-the-box for:
  - Handwritten text
  - Artistic/graphic fonts
  - Poor lighting or contrast
- No complex preprocessing needed.

> 🔍 **This app uses EasyOCR for improved recognition of stylized and real-world images.**

---

## 💻 Features

- Upload image files via a browser
- Extract text using **EasyOCR**
- Displays extracted text on the same page
- Automatically saves uploaded images
- Lightweight Flask backend
- Easy to deploy and extend

---

## 🏧 Folder Structure

```
ocr-web-app/
├── main.py                # Flask app
├── templates/
│   └── index.html         # Web UI
├── uploads/               # Temporary image uploads
├── static/                # (optional) CSS or JS files
├── output/                # (optional) extracted text output
└── README.md              # Documentation
```

---

## ⚙️ Installation Guide

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/ocr-web-app.git
cd ocr-web-app
```

### Step 2: Install Required Libraries

#### Option A: Using `requirements.txt`
```bash
pip install -r requirements.txt
```

#### Option B: Manual Installation
```bash
pip install flask easyocr pillow
```

### Step 3: Run the Flask App
```bash
python main.py
```

Open your browser and go to:  
```
http://127.0.0.1:5000/
```

---

## 🌐 How It Works

1. User uploads an image via the web interface.
2. The image is saved to the `uploads/` directory.
3. **EasyOCR** scans the image and extracts visible text using deep learning.
4. Extracted text is shown below the image.

---

## ✨ Sample Output

Website 

<img width="1161" height="677" alt="Screenshot 2025-07-24 234556" src="https://github.com/user-attachments/assets/89ecc436-e745-4919-9fe0-119df680cbb0" />

**Uploaded Image:**

<img width="1151" height="852" alt="Screenshot 2025-07-24 234653" src="https://github.com/user-attachments/assets/65b43f47-a5c6-4508-aba5-cb88b3da6a36" />


**Extracted Text:**

<img width="1190" height="507" alt="Screenshot 2025-07-24 234717" src="https://github.com/user-attachments/assets/9fd8de73-26e0-4ec6-ab26-97d0f3010678" />


## ✅ Future Improvements

- Add support for Tesseract OCR as an option
- Save extracted text to PDF/Word
- Add multiple language support
- Deploy to Heroku or Render

---

## 🤝 Acknowledgements

- [EasyOCR](https://github.com/JaidedAI/EasyOCR)
- [Flask](https://flask.palletsprojects.com/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)


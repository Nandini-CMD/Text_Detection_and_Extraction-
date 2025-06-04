from flask import Flask, render_template, request, send_from_directory
import os
from werkzeug.utils import secure_filename
import easyocr
from PIL import Image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# EasyOCR Reader Initialization (only once)
reader = easyocr.Reader(['en'])  # Add 'hi' or other languages as needed

@app.route('/', methods=['GET', 'POST'])
def index():
    extracted_text = None
    uploaded_filename = None

    if request.method == 'POST':
        file = request.files.get('image')
        if file:
            filename = secure_filename(file.filename)
            uploaded_filename = filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Use EasyOCR to extract text
            result = reader.readtext(file_path, detail=0)
            extracted_text = " ".join(result)

    return render_template('index.html', extracted_text=extracted_text, uploaded_filename=uploaded_filename)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)

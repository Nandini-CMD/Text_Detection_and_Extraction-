import cv2
import pytesseract

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def pre_processing(image_path):
    
    img = cv2.imread(image_path)

    if img is None:
        print("Error loading image.")
    else:
        # Original image
        original = img.copy()

        # Step 1: Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Step 2: Apply moderate denoising
        denoised = cv2.fastNlMeansDenoising(gray, h=15)

        # Step 3: Increase contrast for better text clarity
        contrast_enhanced = cv2.convertScaleAbs(denoised, alpha=2.0, beta=0)

        # Save the final preprocessed image
        output_path = 'output/preprocessed_image.jpg'
        cv2.imwrite(output_path, contrast_enhanced)

        return output_path

def text_extraction(output_path):
    img_for_ocr = cv2.imread(output_path)
    if img_for_ocr is None:
        print("Error loading image for text recognition.")
    else:
        # Tesseract OCR with custom config
        config = "--oem 3 --psm 6"
        recognized_text = pytesseract.image_to_string(img_for_ocr, config=config)
        
        if recognized_text.strip():
            print("Text extraction completed successfully!")
            print(f"Extracted text:\n{recognized_text}")
            
            # Save the recognized text to a file
            with open('output/final_text.txt', 'w', encoding='utf-8') as f:
                f.write(recognized_text)
        else:
            print("No text detected.")

def main(image_path):
    print("Starting text detection...")
    
    # Step 1: Preprocess the image
    preprocessed_image_path = pre_processing(image_path)
    print("Preprocessing completed.")
    # Step 2: Detect text regions
    text_extraction(preprocessed_image_path)
    print('done')


if __name__ == "__main__":
    main(r'c:\Users\Sumit\OneDrive\Desktop\Text_project\image\example_1.png')  # Adjust the image path accordingly
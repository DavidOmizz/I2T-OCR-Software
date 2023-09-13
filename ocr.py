from PIL import Image
import pytesseract

# Path to the Tesseract executable (change this to the location on your system)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open an image using PIL (Pillow)

image_path = 'lets_go.png'
image = Image.open(image_path)

# Perform OCR on the image
text = pytesseract.image_to_string(image, lang='eng')

# Print the extracted text
print(text)

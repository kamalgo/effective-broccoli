import cv2
import pytesseract

# Specify the full path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'  # Update the path here


def preprocess_image(image_path, blur_size=5, threshold_method='gaussian'):
    """
    Preprocess the image for better OCR results:
    - Convert to grayscale
    - Apply Gaussian blur
    - Perform adaptive thresholding
    - Remove noise and deskew the image
    """
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    alpha = 1.5  # Contrast
    beta = 20    # Brightness
    img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
    img = cv2.GaussianBlur(img, (blur_size, blur_size), 0)

    if threshold_method == 'gaussian':
        img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    else:
        img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    return img


def extract_structured_fields(image):
    """
    Extract structured fields from the image.
    For example, fields from certificates or forms.
    """
    text = pytesseract.image_to_string(image, lang='eng')
    # Add logic to parse structured fields
    return {"structured_text": text}


def extract_general_text(image):
    """
    Extract general text from the image (unstructured).
    """
    text = pytesseract.image_to_string(image, lang='mar')
    return {"general_text": text}










# # import pytesseract
# # import cv2
# # import re

# # # Specify the full path to the Tesseract executable
# # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'  # Update the path here


# # def preprocess_image(image_path):
# #     """
# #     Preprocesses the image by converting it to grayscale and applying binary thresholding.
# #     :param image_path: Path to the input image file.
# #     :return: Preprocessed image as a numpy array.
# #     """
# #     img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
# #     _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
# #     return img

# # def extract_structured_fields(image_path):
# #     """
# #     Extracts structured fields (e.g., yearly income, validity, location, and date) from the image.
# #     :param image_path: Path to the input image file.
# #     :return: Dictionary with extracted fields and their values.
# #     """
# #     # Extract text using Tesseract OCR
# #     text = pytesseract.image_to_string(image_path, lang='mar+eng')

# #     # Define regex patterns for structured fields
# #     patterns = {
# #         "Yearly Income": r"(\d{4}[-–]\d{4}).*?(\d{1,3}(,\d{3})*)",
# #         "Validity": r"वैध राहील.*?(\d{2}/\d{2}/\d{4})",
# #         "Location and Date": r"स्थळ:\s*(.*?)\s*दिनांक:\s*(\d{2}/\d{2}/\d{4})"
# #     }

# #     # Extract fields using regex
# #     results = {}
# #     for field, pattern in patterns.items():
# #         match = re.search(pattern, text, re.DOTALL)
# #         results[field] = match.groups() if match else None
    
# #     return results

# # def extract_general_text(image_path):
# #     """
# #     Extracts plain text from the image.
# #     :param image_path: Path to the input image file.
# #     :return: Extracted plain text.
# #     """
# #     # Extract text using Tesseract OCR
# #     text = pytesseract.image_to_string(image_path, lang='eng')
# #     return text.strip()


# import cv2
# import numpy as np

# def preprocess_image(image_path):
#     """
#     Preprocess the image for better OCR results:
#     1. Convert to grayscale
#     2. Apply Gaussian blur
#     3. Perform adaptive thresholding
#     4. Remove noise and deskew the image
#     """
#     # Read the image in grayscale
#     img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
#     # Apply Gaussian Blur to reduce noise
#     img = cv2.GaussianBlur(img, (5, 5), 0)
    
#     # Adaptive thresholding for better text contrast
#     img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    
#     # Morphological operations to remove small noise
#     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
#     img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    
#     # Deskew the image
#     coords = np.column_stack(np.where(img > 0))
#     angle = cv2.minAreaRect(coords)[-1]
#     if angle < -45:
#         angle = -(90 + angle)
#     else:
#         angle = -angle
#     (h, w) = img.shape[:2]
#     center = (w // 2, h // 2)
#     M = cv2.getRotationMatrix2D(center, angle, 1.0)
#     img = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    
#     return img

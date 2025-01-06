# utils.py
import os
import fitz  # PyMuPDF
from concurrent.futures import ThreadPoolExecutor

def pdf_to_images(pdf_path, output_dir="output", dpi=300):
    """
    Converts a PDF file to individual images for each page.
    
    Args:
        pdf_path (str): Path to the input PDF file.
        output_dir (str): Directory where images will be saved.
        dpi (int): Resolution for the generated images (dots per inch).
    
    Returns:
        List[str]: List of file paths for the generated images.
    """
    try:
        doc = fitz.open(pdf_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        image_paths = []

        def process_page(page_num):
            page = doc[page_num]
            pix = page.get_pixmap(dpi=dpi)
            img_path = os.path.join(output_dir, f"page_{page_num + 1}.jpg")
            pix.save(img_path)
            return img_path

        with ThreadPoolExecutor() as executor:
            image_paths = list(executor.map(process_page, range(len(doc))))

        doc.close()
        return image_paths
    except Exception as e:
        logging.error(f"An error occurred during PDF conversion: {e}")
        return []














# # import cv2
# # import fitz  # PyMuPDF
# # import os


# # # Convert PDF to images
# # def pdf_to_images(pdf_path, output_dir="output", dpi=300):
# #     """
# #     Converts a PDF file to individual images for each page.
    
# #     Args:
# #         pdf_path (str): Path to the input PDF file.
# #         output_dir (str): Directory where images will be saved.
# #         dpi (int): Resolution for the generated images (dots per inch).
    
# #     Returns:
# #         List[str]: List of file paths for the generated images.
# #     """
# #     try:
# #         # Open the PDF file
# #         doc = fitz.open(pdf_path)

# #         # Create the output directory if it doesn't exist
# #         if not os.path.exists(output_dir):
# #             os.makedirs(output_dir)

# #         image_paths = []

# #         # Convert each page to an image
# #         for page_num in range(len(doc)):
# #             page = doc[page_num]
# #             # Render the page to a Pixmap
# #             pix = page.get_pixmap(dpi=dpi)
# #             # Define the output path
# #             img_path = os.path.join(output_dir, f"page_{page_num + 1}.jpg")
# #             # Save the image
# #             pix.save(img_path)
# #             image_paths.append(img_path)
# #             print(f"Saved: {img_path}")

# #         # Close the document
# #         doc.close()

# #         return image_paths

# #     except Exception as e:
# #         print(f"An error occurred: {e}")
# #         return []

# # # Example: Using the function
# # pdf_path = "income.pdf"
# # output_dir = "pdf_images"
# # image_paths = pdf_to_images(pdf_path, output_dir=output_dir)

# # # Optional: Process the images with OpenCV
# # for img_path in image_paths:
# #     # Read the image using OpenCV
# #     img = cv2.imread(img_path)
    
# #     # Example processing: Convert to grayscale
# #     gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
# #     # Save the processed image
# #     processed_path = img_path.replace(".jpg", "_gray.jpg")
# #     cv2.imwrite(processed_path, gray_img)
# #     print(f"Processed image saved: {processed_path}")





# # # import cv2
# # # from pdf2image import convert_from_path

# # # # Convert PDF to images
# # # def pdf_to_images(pdf_path):
# # #         # Specify the Poppler path explicitly
# # #     poppler_path = r"C:\poppler-24.08.0\Library\bin"

# # #     """
# # #     Converts a PDF file to individual images for each page.
# # #     :param pdf_path: Path to the input PDF file.
# # #     :return: List of file paths for the generated images.
# # #     """
# # #     # Convert PDF to images
# # #     images = convert_from_path(pdf_path, dpi=300)
# # #     image_paths = []

# # #     # Save each page as an image
# # #     for i, image in enumerate(images):
# # #         img_path = f'page_{i + 1}.jpg'
# # #         image.save(img_path, 'JPEG')
# # #         image_paths.append(img_path)
    
# # #     return image_paths


# import os
# import fitz  # PyMuPDF

# def pdf_to_images(pdf_path, output_dir="output", dpi=300):
#     """
#     Converts a PDF file to individual images for each page.
    
#     Args:
#         pdf_path (str): Path to the input PDF file.
#         output_dir (str): Directory where images will be saved.
#         dpi (int): Resolution for the generated images (dots per inch).
    
#     Returns:
#         List[str]: List of file paths for the generated images.
#     """
#     try:
#         doc = fitz.open(pdf_path)

#         if not os.path.exists(output_dir):
#             os.makedirs(output_dir)

#         image_paths = []
#         for page_num in range(len(doc)):
#             page = doc[page_num]
#             pix = page.get_pixmap(dpi=dpi)
#             img_path = os.path.join(output_dir, f"page_{page_num + 1}.jpg")
#             pix.save(img_path)
#             image_paths.append(img_path)
#             print(f"Saved image: {img_path}")

#         doc.close()
#         return image_paths

#     except Exception as e:
#         print(f"An error occurred during PDF conversion: {e}")
#         return []

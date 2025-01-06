# main.py
import logging
import json
from ocr import preprocess_image, extract_structured_fields, extract_general_text
from utils import pdf_to_images

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load configuration
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Main Function
if __name__ == '__main__':
    logging.info("Welcome to the OCR Prototype")
    print("1. Structured Document (e.g., Income Certificate)")
    print("2. General Image (Plain Text)")
    
    choice = input("Select the type of document (1 or 2): ").strip()
    
    if choice not in ['1', '2']:
        logging.error("Invalid choice. Exiting.")
        exit()

    file_path = input("Enter the path to your file (image or PDF): ").strip()
    
    # Convert PDF to images if applicable
    image_paths = []
    if file_path.endswith('.pdf'):
        logging.info("PDF detected, converting to images...")
        image_paths = pdf_to_images(file_path, output_dir=config['output_dir'], dpi=config['dpi'])
        logging.info(f"Converted PDF to images: {image_paths}")
    else:
        image_paths = [file_path]
    
    # Process each image
    for image_path in image_paths:
        try:
            logging.info(f"Processing: {image_path}")
            processed_img = preprocess_image(image_path, 
                                             blur_size=config['blur_size'], 
                                             threshold_method=config['threshold_method'])
            
            # Check user choice and apply the right function
            if choice == '1':
                result = extract_structured_fields(processed_img)
            else:
                result = extract_general_text(processed_img)
            
            print("\nExtracted Result:", result)
            
            # Ask user if they want to save the result
            save = input("Do you want to save the results? (y/n): ").strip().lower()
            if save == 'y':
                output_file = input("Enter the output file name (e.g., result.json): ").strip()
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(json.dumps(result, indent=4))
                logging.info(f"Results saved to {output_file}")
        except Exception as e:
            logging.error(f"An error occurred while processing {image_path}: {e}")
            





# # # from ocr import preprocess_image, extract_structured_fields, extract_general_text
# # # from utils import pdf_to_images

# # # # Main Function
# # # if __name__ == '__main__':
# # #     print("Welcome to the OCR Prototype")
# # #     print("1. Structured Document (e.g., Income Certificate)")
# # #     print("2. General Image (Plain Text)")
    
# # #     choice = input("Select the type of document (1 or 2): ").strip()
    
# # #     if choice not in ['1', '2']:
# # #         print("Invalid choice. Exiting.")
# # #         exit()

# # #     file_path = input("Enter the path to your file (image or PDF): ").strip()
    
# # #     if file_path.endswith('.pdf'):
# # #         image_paths = pdf_to_images(file_path)
# # #         print(f"Converted PDF to images: {image_paths}")
# # #     else:
# # #         image_paths = [file_path]
    
# # #     for image_path in image_paths:
# # #         processed_img = preprocess_image(image_path)
        
# # #         if choice == '1':
# # #             result = extract_structured_fields(processed_img)
# # #         else:
# # #             result = extract_general_text(processed_img)
        
# # #         print("\nExtracted Result:", result)
        
# # #         save = input("Do you want to save the results? (y/n): ").strip().lower()
# # #         if save == 'y':
# # #             output_file = input("Enter the output file name (e.g., result.json): ").strip()
# # #             with open(output_file, 'w', encoding='utf-8') as f:
# # #                 f.write(str(result))
# # #             print(f"Results saved to {output_file}")


# # from ocr import preprocess_image, extract_structured_fields, extract_general_text
# # from utils import pdf_to_images

# # # Main Function
# # if __name__ == '__main__':
# #     print("Welcome to the OCR Prototype")
# #     print("1. Structured Document (e.g., Income Certificate)")
# #     print("2. General Image (Plain Text)")
    
# #     choice = input("Select the type of document (1 or 2): ").strip()
    
# #     if choice not in ['1', '2']:
# #         print("Invalid choice. Exiting.")
# #         exit()

# #     file_path = input("Enter the path to your file (image or PDF): ").strip()
    
# #     # Convert PDF to images if applicable
# #     if file_path.endswith('.pdf'):
# #         print("PDF detected, converting to images...")
# #         image_paths = pdf_to_images(file_path)
# #         print(f"Converted PDF to images: {image_paths}")
# #     else:
# #         image_paths = [file_path]
    
# #     # Process each image
# #     for image_path in image_paths:
# #         try:
# #             print(f"Processing: {image_path}")
# #             processed_img = preprocess_image(image_path)
            
# #             # Extract results based on document type
# #             if choice == '1':
# #                 result = extract_structured_fields(processed_img)
# #             else:
# #                 result = extract_general_text(processed_img)
            
# #             print("\nExtracted Result:", result)
            
# #             # Save results if user opts to
# #             save = input("Do you want to save the results? (y/n): ").strip().lower()
# #             if save == 'y':
# #                 output_file = input("Enter the output file name (e.g., result.json): ").strip()
# #                 with open(output_file, 'w', encoding='utf-8') as f:
# #                     f.write(str(result))
# #                 print(f"Results saved to {output_file}")
# #         except Exception as e:
# #             print(f"An error occurred while processing {image_path}: {e}")



# from ocr import preprocess_image, extract_structured_fields, extract_general_text
# from utils import pdf_to_images

# # Main Function
# if __name__ == '__main__':
#     print("Welcome to the OCR Prototype")
#     print("1. Structured Document (e.g., Income Certificate)")
#     print("2. General Image (Plain Text)")
    
#     choice = input("Select the type of document (1 or 2): ").strip()
    
#     if choice not in ['1', '2']:
#         print("Invalid choice. Exiting.")
#         exit()

#     file_path = input("Enter the path to your file (image or PDF): ").strip()
    
#     # Convert PDF to images if applicable
#     image_paths = []
#     if file_path.endswith('.pdf'):
#         print("PDF detected, converting to images...")
#         image_paths = pdf_to_images(file_path)  # Converts PDF to images
#         print(f"Converted PDF to images: {image_paths}")
#     else:
#         image_paths = [file_path]  # If not a PDF, process the file directly as an image
    
#     # Process each image
#     for image_path in image_paths:
#         try:
#             print(f"Processing: {image_path}")
#             processed_img = preprocess_image(image_path)  # Preprocess the image
            
#             # Check user choice and apply the right function
#             if choice == '1':
#                 result = extract_structured_fields(processed_img)  # Structured fields for Option 1
#             else:
#                 result = extract_general_text(processed_img)  # General text for Option 2
            
#             print("\nExtracted Result:", result)
            
#             # Ask user if they want to save the result
#             save = input("Do you want to save the results? (y/n): ").strip().lower()
#             if save == 'y':
#                 output_file = input("Enter the output file name (e.g., result.json): ").strip()
#                 with open(output_file, 'w', encoding='utf-8') as f:
#                     f.write(str(result))
#                 print(f"Results saved to {output_file}")
#         except Exception as e:
#             print(f"An error occurred while processing {image_path}: {e}")



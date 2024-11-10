#**Image Processor Function**
#=====================================

#Below is an example of a Python function that processes image files in a specified directory. This function uses the Pillow library to open and manipulate the images.

import ollama
import os
#from PIL import Image

def process_images(directory, output_directory=None):
    """
    Process image files in a specified directory.

    Args:
        directory (str): The path to the directory containing the image files.
        output_directory (str, optional): The path to the directory where processed images will be saved. Defaults to None.

    Returns:
        list: A list of file paths for the processed images.
    """

    # Initialize an empty list to store the file paths of processed images
    processed_images = []

    # Iterate through each file in the specified directory
    for filename in os.listdir(directory):
        # Check if the file is an image (assuming it has a .jpg, .jpeg, or .png extension)
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            # Construct the full path to the image file
            image_path = os.path.join(directory, filename)

            try:
                # Open the image using llama3.2-vision
                with Image.open(image_path) as img:
                    # Process the image here (e.g., resize, apply filters, etc.)
                    # For demonstration purposes, we'll just convert it to grayscale
                    processed_img = img.convert('L')

                    # If an output directory is specified, save the processed image there
                    if output_directory:
                        output_path = os.path.join(output_directory, filename)
                        processed_img.save(output_path)
                        processed_images.append(output_path)
                    else:
                        # Otherwise, overwrite the original image with the processed one
                        processed_img.save(image_path)
                        processed_images.append(image_path)

            except Exception as e:
                print(f"Error processing {filename}: {e}")

    return processed_images

# Example usage
directory = "/home/roxasrr/code/ollama_vision_scripts/images"
output_directory = "/home/roxasrr/code/ollama_vision_scripts/processed"

processed_image_paths = process_images(directory, output_directory)
print(processed_image_paths)

#**Tips and Variations**

#* To apply different processing techniques (e.g., resizing, cropping, applying filters), modify the `process_img` variable assignment inside the loop.
#* If you want to handle other image formats (e.g., .gif, .bmp), add more extensions to the tuple in the `if filename.lower().endswith()` line.
#* To process images recursively through subdirectories, use `os.walk()` instead of `os.listdir()`.
#* For large directories or performance-critical applications, consider using a more efficient image processing library like OpenCV.
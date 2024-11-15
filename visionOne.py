import ollama
import os

#from PIL import Image
# Assuming the llama3.2-vision module is installed and contains process_image function
#from ollama import process_image

def process_images_and_save_results(image_paths, output_file_path):
    """
    Processes multiple images using the llama3.2-vision module and saves the results in a text file.

    Parameters:
        image_paths (list of str): List of paths to the images to be processed.
        output_file_path (str): Path to the text file where the results will be saved.
    """
    with open(output_file_path, 'w') as f:
        for image_path in image_paths:
            if not os.path.isfile(image_path):
                print(f"Warning: {image_path} does not exist. Skipping...")
                continue
            
            try:
              response = ollama.chat(
                  model='llama3.2-vision',
                  messages=[
                      'role': 'user',
                      'content': 'What is in this image?',
                # Open and process the image using llama3.2-vision model
                with Image.open(image_path) as img:
                    #result = process_image(img)
                    'images': ['bridy.jpg']
                    # Write the result to the output file
                    f.write(f"Image path: {image_path}\n")
                    f.write(f"Result: {result}\n\n")
            except Exception as e:
                print(f"Error processing {image_path}: {e}")
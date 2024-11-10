import cv2
import os
import ollama

def process_images(directory, output_directory):
        """
        Process multiple images in the specified directory.

        Args:
            directory (str): Path to the directory containing images.
            output_directory (str): Path to the directory where processed images will be saved.

        Returns:
            None
        """

response = ollama.chat(
    model='llama3.2-vision',
    messages=[{
        'role': 'user',
        'content': 'What is in this image?',
        'images': ['bridy.jpg']
    }]
)

print(response)

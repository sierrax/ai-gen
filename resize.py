#!/usr/bin/env python3

import os
from PIL import Image
import shutil
from tqdm import tqdm
from colorama import Fore, Style, init
from concurrent.futures import ThreadPoolExecutor, as_completed

# Initialize colorama
init(autoreset=True)

# Ignore PIL image size limits
Image.MAX_IMAGE_PIXELS = None

# Create the Resized directory if it doesn't exist
output_dir = 'Resized'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get a list of all image files in the current directory
image_files = [f for f in os.listdir('.') if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff'))]

# Define a function to resize or copy an image
def process_image(filename):
    try:
        with Image.open(filename) as img:
            width, height = img.size
            if height > 1080:
                new_height = 1080
                new_width = int((new_height / height) * width)
                resized_img = img.resize((new_width, new_height), Image.LANCZOS)
                resized_img.save(os.path.join(output_dir, filename))
            else:
                shutil.copy(filename, os.path.join(output_dir, filename))
    except Exception as e:
        print(f"{Fore.RED}Error processing {filename}: {e}{Style.RESET_ALL}")

# Starting message
print(f"{Fore.CYAN}Processing {len(image_files)} images...{Style.RESET_ALL}")

# Use ThreadPoolExecutor to process images concurrently
with ThreadPoolExecutor() as executor:
    futures = [executor.submit(process_image, filename) for filename in image_files]
    
    # Use tqdm to show progress bar
    for _ in tqdm(as_completed(futures), total=len(futures), desc=f"{Fore.GREEN}Resizing images{Style.RESET_ALL}", unit="image"):
        pass

# Completion message
print(f"\n{Fore.GREEN}Image processing complete!{Style.RESET_ALL}")
print(f"{Fore.CYAN}All resized images have been saved to the '{output_dir}' directory.{Style.RESET_ALL}")

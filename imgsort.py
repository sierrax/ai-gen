#!/usr/bin/env python3

import os
import shutil
from PIL import Image, ImageFile
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Disable the maximum image size limitation
Image.MAX_IMAGE_PIXELS = None
# Handle truncated images
ImageFile.LOAD_TRUNCATED_IMAGES = True

def get_aspect_ratio(file_path):
    with Image.open(file_path) as img:
        width, height = img.size
        aspect_ratio = width / height
    return aspect_ratio

def create_subfolders(directory, aspect_ratios):
    for ratio in aspect_ratios:
        subfolder = os.path.join(directory, f"{ratio:.2f}")
        os.makedirs(subfolder, exist_ok=True)

def copy_to_subfolder(file_path, aspect_ratios, directory):
    ratio = get_aspect_ratio(file_path)

    # Find the closest aspect ratio folder
    closest_ratio = min(aspect_ratios, key=lambda x: abs(x - ratio))
    destination_folder = os.path.join(directory, f"{closest_ratio:.2f}")

    # Copy the file to the destination folder
    shutil.copy(file_path, destination_folder)
    return file_path

def process_images_in_threads(directory, aspect_ratios):
    files = [f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(copy_to_subfolder, os.path.join(directory, filename), aspect_ratios, directory): filename for filename in files}

        for _ in tqdm(as_completed(futures), total=len(futures), desc=f"{Fore.GREEN}Processing Images{Style.RESET_ALL}", unit="image", colour='green'):
            pass

if __name__ == "__main__":
    current_directory = os.getcwd()
    aspect_ratios = [1.33, 1.5, 1.78, 2.0]  # Add your desired aspect ratios

    create_subfolders(current_directory, aspect_ratios)
    process_images_in_threads(current_directory, aspect_ratios)

    print(f"{Fore.CYAN}Image files copied to subfolders based on aspect ratio.{Style.RESET_ALL}")

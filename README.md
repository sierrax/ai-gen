# ChatGPT Jiggery-Pokery
These are a couple scripts that ChatGPT-4o came up with under guidance to perform operations on large numbers of image files that don't necessarily need constant attention.  Both scripts require Python 3, as well as pillow, tqdm, and colorama.  Install them with pip if you don't have them, you know how.  If you don't, what are you even doing here?
## imgsort.py
Copies images into subdirectories based on aspect ratio (by default 1.33, 1.5, 1.78, and 2.0 [4:3, 3:2, 16x9, and 2x1{I don't have anything else to add here, I just wanted to nest more brackets}]).  I'll probably change it to move images, but this is fine for now, though move would be faster.
## resize.py
Resizes images to a height of 1080 pixels (by default) if they're larger.

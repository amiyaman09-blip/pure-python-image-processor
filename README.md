# Pure Python Image Processor

## Overview
This project implements basic image processing using core Python only. No NumPy, OpenCV, or Pillow is used. It has two parts: grayscale processing on a small 5 x 5 grid, and a bonus part that processes real colour photos loaded from PPM files and saves the results as PNG images.

## Project Structure
- `main.py` - the grayscale 5 x 5 grid part.
- `image_handler.py` - all the functions for the colour image part (loading, processing and saving).
- `run_image.py` - the program that loads the photo, runs every operation and saves the results.
- `images/image.ppm` - the input colour photo.
- `output/` - the folder where the result images are saved. It is created automatically.
- `sample.ppm` - a small 2 x 2 test image with red, green, blue and yellow pixels.

## Part 1: Grayscale Image Processing (main.py)

### Image Representation
The image is represented as a 2D list containing pixel values from 0 to 255. Zero represents black, and 255 represents white.

### Implemented Functions

1. **print_image()** - Prints the image row by row.
2. **invert_image()** - Inverts every pixel using 255 minus its value.
3. **adjust_brightness()** - Adds or subtracts a specified amount while keeping pixel values between 0 and 255.
4. **threshold_image()** - Converts the grayscale image into black and white based on a threshold.
5. **flip_horizontal()** - Reverses each row to mirror the image horizontally.
6. **rotate_clockwise()** - Rotates the image 90 degrees clockwise.
7. **blur_image()** - Applies a 3 x 3 averaging filter to the inner pixels.

### Border Handling
The blur operation leaves the outermost border pixels unchanged because a complete 3 x 3 neighbourhood is unavailable at the edges.

### Output
The program prints the original image and the result of each operation in the terminal. This allows the pixel transformations to be checked directly.

## Part 2 (Bonus): Colour Images from PPM Files

I extended my Pure Python Image Processor so that it works on real colour photos. The photo is loaded from a PPM (Portable Pixmap) file, each of the operations from Part 1 is applied to it, and every result is saved as a PNG image that can be opened in any image viewer.

### Image Representation
The colour image is stored as a nested Python list. Each pixel is a list of three values, `[red, green, blue]`, so the image keeps its original colours. The maximum colour value (usually 255) is read from the file and used by the operations.

### Loading PPM Files: load_ppm()
- Opens the file in binary mode using Python's built-in file handling.
- Reads the header: the format (`P3` or `P6`), the width, the height and the maximum colour value. Comment lines starting with a hash symbol in the header are skipped.
- Supports both plain-text `P3` files and binary `P6` files. Most photos exported from image editors are `P6`.
- Reads the RGB values and groups them into rows and pixels.
- Returns the image as a nested list together with the maximum colour value.
- Prints a message and returns nothing if the format is not supported or the file does not contain enough pixel data.

### Operations on Colour Images
All operations are written in plain Python using loops.

1. **print_image()** - Prints the pixel values when the image is 10 x 10 or smaller. For larger photos it prints only the image size.
2. **invert_image()** - Replaces each of the red, green and blue values with the maximum value minus that value, which gives a colour negative.
3. **adjust_brightness()** - Adds an amount to each of the three channels and keeps every value between 0 and the maximum.
4. **threshold_image()** - Works out the brightness of each pixel using `0.299 x red + 0.587 x green + 0.114 x blue`. Pixels at or above the threshold keep their original colour, and darker pixels become black.
5. **flip_horizontal()** - Reverses each row to mirror the image.
6. **rotate_clockwise()** - Rotates the image 90 degrees clockwise.
7. **blur_image()** - Applies a 3 x 3 averaging filter separately to the red, green and blue channels. Border pixels are left unchanged.

### Saving PNG Images: save_png()
The results are saved as PNG files, so they can be opened by double-clicking them. The PNG file is written by hand using only Python's built-in `zlib` and `struct` modules. The function builds the PNG header, the compressed pixel data and the end chunk, and scales the colour values to 8 bits if the file uses a different maximum value. A `save_ppm()` function is also included for saving results back to PPM format.

### Output Folder
When `run_image.py` runs, it creates a folder called `output` automatically if it does not exist, and saves these images inside it:
- `original.png`
- `inverted.png`
- `brighter.png`
- `threshold.png`
- `flipped.png`
- `rotated.png`
- `blurred.png`

Running the program again overwrites these files.

### How to Run
1. Put the colour photo in the `images` folder and name it `image.ppm`.
2. Run `py run_image.py` in the terminal from the project folder.
3. Open the result images from the `output` folder.

Run `py main.py` to see the grayscale 5 x 5 grid part.

### Test Files
I created a sample file named `sample.ppm` containing a 2 x 2 colour image with red, green, blue and yellow pixels, which was used to check the loader on a small image before using a real photo.

### Limitations
- The loader supports only P3 and P6 PPM files. PGM and other formats must be converted to PPM first.
- The colours in the output depend on the input file. A PPM file that was converted from a grayscale PGM image contains no colour information, so its results also look gray.
- The blur leaves border pixels unchanged.
- Because everything is written in plain Python, blurring a very large photo can be slow.
- PNG files are saved as 8-bit RGB images without any filtering, so they are larger than files made by dedicated image libraries.
- The program checks the file header and the amount of pixel data, but it does not fully validate every kind of damaged file.

### Libraries Used
Only core Python and its built-in standard library modules (`os`, `zlib` and `struct`) were used. No NumPy, OpenCV, or Pillow were used for image processing.

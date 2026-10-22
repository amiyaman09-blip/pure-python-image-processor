# Pure Python Image Processor

## Overview
This project implements basic grayscale image processing using core Python only. No NumPy, OpenCV, or Pillow is used.

## Image Representation
The image is represented as a 2D list containing pixel values from 0 to 255. Zero represents black, and 255 represents white.

## Implemented Functions

1. **print_image()** — Prints the image row by row.
2. **invert_image()** — Inverts every pixel using 255 minus its value.
3. **adjust_brightness()** — Adds or subtracts a specified amount while keeping pixel values between 0 and 255.
4. **threshold_image()** — Converts the grayscale image into black and white based on a threshold.
5. **flip_horizontal()** — Reverses each row to mirror the image horizontally.
6. **rotate_clockwise()** — Rotates the image 90 degrees clockwise.
7. **blur_image()** — Applies a 3 × 3 averaging filter to the inner pixels.

## Border Handling
The blur operation leaves the outermost border pixels unchanged because a complete 3 × 3 neighbourhood is unavailable at the edges.

## Output
The program prints the original image and the result of each operation in the terminal. This allows the pixel transformations to be checked directly.

## Libraries
Only core Python is used for the image-processing logic.
## Bonus: PPM Image Loading

I extended my Pure Python Image Processor by adding a function called `load_ppm()` to load colour images from PPM (Portable Pixmap) files.

The function reads a P3 PPM file, extracts the image dimensions and RGB pixel values, and stores the image as a nested Python list. Each pixel is represented by three values: Red, Green, and Blue, ranging from 0 to 255.

### How It Works
- Opens and reads a PPM file using Python's built-in file handling.
- Extracts the image format, width, height, and maximum colour value.
- Reads the RGB values and groups them into rows and pixels.
- Returns the loaded colour image as a nested list.

### Test File
I created a sample file named `sample.ppm` containing a 2 × 2 colour image with red, green, blue, and yellow pixels.

### Limitations
The loader supports plain-text P3 PPM files. It does not currently support binary P6 files or comprehensive validation of malformed files.

### Libraries Used
Only core Python features were used. No NumPy, OpenCV, or Pillow were used for image processing.

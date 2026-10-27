import os

from image_handler import (
    load_ppm,
    save_png,
    print_image,
    invert_image,
    adjust_brightness,
    threshold_image,
    flip_horizontal,
    rotate_clockwise,
    blur_image
)


def main():
    base_folder = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(base_folder, "images", "image.ppm")
    output_folder = os.path.join(base_folder, "output")

    if not os.path.exists(input_file):
        print("images/image.ppm not found. Put your photo there.")
        return

    os.makedirs(output_folder, exist_ok=True)

    image, max_value = load_ppm(input_file)

    if image is None:
        return

    print_image("ORIGINAL IMAGE", image)
    save_png(os.path.join(output_folder, "original.png"), image, max_value)

    inverted = invert_image(image, max_value)
    print_image("INVERTED IMAGE", inverted)
    save_png(os.path.join(output_folder, "inverted.png"), inverted, max_value)

    brighter = adjust_brightness(image, 40, max_value)
    print_image("BRIGHTER IMAGE", brighter)
    save_png(os.path.join(output_folder, "brighter.png"), brighter, max_value)

    thresholded = threshold_image(image, 100, max_value)
    print_image("THRESHOLDED IMAGE", thresholded)
    save_png(os.path.join(output_folder, "threshold.png"), thresholded, max_value)

    flipped = flip_horizontal(image)
    print_image("HORIZONTALLY FLIPPED IMAGE", flipped)
    save_png(os.path.join(output_folder, "flipped.png"), flipped, max_value)

    rotated = rotate_clockwise(image)
    print_image("ROTATED IMAGE", rotated)
    save_png(os.path.join(output_folder, "rotated.png"), rotated, max_value)

    blurred = blur_image(image)
    print_image("BLURRED IMAGE", blurred)
    save_png(os.path.join(output_folder, "blurred.png"), blurred, max_value)

    print("\nAll images saved in the output folder.")


main()
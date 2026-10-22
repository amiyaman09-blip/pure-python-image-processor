
image = [
    [0, 0, 0, 0, 0],
    [0, 50, 50, 50, 0],
    [0, 50, 255, 50, 0],
    [0, 50, 50, 50, 0],
    [0, 0, 0, 0, 0]
]


def print_image(img):
    for row in img:
        print(row)

print("ORIGINAL IMAGE:")
print_image(image)


def invert_image(img):
    result = []

    for row in img:
        new_row = []

        for pixel in row:
            new_pixel = 255 - pixel
            new_row.append(new_pixel)

        result.append(new_row)

    return result

print("\nINVERTED IMAGE:")
inverted = invert_image(image)
print_image(inverted)

# Function to adjust image brightness
def adjust_brightness(img, amount):
    result = []

    for row in img:
        new_row = []

        for pixel in row:
            new_pixel = pixel + amount

            if new_pixel > 255:
                new_pixel = 255

            if new_pixel < 0:
                new_pixel = 0

            new_row.append(new_pixel)

        result.append(new_row)

    return result


print("\nBRIGHTER IMAGE:")
brighter = adjust_brightness(image, 40)
print_image(brighter)

# Function to convert image to black and white
def threshold_image(img, threshold):
    result = []

    for row in img:
        new_row = []

        for pixel in row:
            if pixel >= threshold:
                new_row.append(255)
            else:
                new_row.append(0)

        result.append(new_row)

    return result


print("\nTHRESHOLDED IMAGE:")
thresholded = threshold_image(image, 100)
print_image(thresholded)

# Function to flip the image horizontally
def flip_horizontal(img):
    result = []

    for row in img:
        new_row = row[::-1]
        result.append(new_row)

    return result


print("\nHORIZONTALLY FLIPPED IMAGE:")
flipped = flip_horizontal(image)
print_image(flipped)

# Function to rotate the image 90 degrees clockwise
def rotate_clockwise(img):
    rows = len(img)
    cols = len(img[0])

    result = []

    for col in range(cols):
        new_row = []

        for row in range(rows - 1, -1, -1):
            new_row.append(img[row][col])

        result.append(new_row)

    return result


print("\nROTATED IMAGE:")
rotated = rotate_clockwise(image)
print_image(rotated)

# Function to blur the image
def blur_image(img):
    rows = len(img)
    cols = len(img[0])

    # Copy the original image
    result = [row[:] for row in img]

    # Process only the inner pixels
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            total = 0

            # Look at the 3x3 neighbourhood
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    total += img[r + dr][c + dc]

            result[r][c] = round(total / 9)

    return result


print("\nBLURRED IMAGE:")
blurred = blur_image(image)
print_image(blurred)


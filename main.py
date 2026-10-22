
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

def flip_horizontal(img):
    result = []

    for row in img:
        new_row = row[::-1]
        result.append(new_row)

    return result


print("\nHORIZONTALLY FLIPPED IMAGE:")
flipped = flip_horizontal(image)
print_image(flipped)


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


def blur_image(img):
    rows = len(img)
    cols = len(img[0])

    
    result = [row[:] for row in img]

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            total = 0

            
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    total += img[r + dr][c + dc]

            result[r][c] = round(total / 9)

    return result


print("\nBLURRED IMAGE:")
blurred = blur_image(image)
print_image(blurred)

def load_ppm(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    data = []

    for line in lines:
        line = line.strip()

        if line and not line.startswith("#"):
            data.extend(line.split())

    if data[0] != "P3":
        print("Unsupported file format")
        return None

    width = int(data[1])
    height = int(data[2])
    max_value = int(data[3])

    values = data[4:]

    image = []
    index = 0

    for r in range(height):
        row = []

        for c in range(width):
            red = int(values[index])
            green = int(values[index + 1])
            blue = int(values[index + 2])

            row.append([red, green, blue])
            index += 3

        image.append(row)

    return image


print("\nPPM IMAGE:")
color_image = load_ppm("sample.ppm")

if color_image is not None:
    for row in color_image:
        print(row)



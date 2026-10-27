import os
import zlib
import struct


def read_header_token(data, pos):
    length = len(data)

    while pos < length:
        if data[pos] in b" \t\r\n":
            pos += 1
        elif data[pos] == ord("#"):
            while pos < length and data[pos] != ord("\n"):
                pos += 1
        else:
            break

    start = pos
    while pos < length and data[pos] not in b" \t\r\n":
        pos += 1

    return data[start:pos].decode("ascii"), pos


def load_ppm(filename):
    with open(filename, "rb") as file:
        data = file.read()

    magic, pos = read_header_token(data, 0)

    if magic != "P3" and magic != "P6":
        print("Unsupported file format (only P3 and P6 PPM are supported)")
        return None, None

    token, pos = read_header_token(data, pos)
    width = int(token)
    token, pos = read_header_token(data, pos)
    height = int(token)
    token, pos = read_header_token(data, pos)
    max_value = int(token)

    values = []

    if magic == "P3":
        rest = data[pos:].decode("ascii")
        for line in rest.split("\n"):
            if "#" in line:
                line = line[:line.index("#")]
            for part in line.split():
                values.append(int(part))
    else:
        pos += 1
        raw = data[pos:]
        if max_value < 256:
            for byte in raw:
                values.append(byte)
        else:
            for i in range(0, len(raw) - 1, 2):
                values.append(raw[i] * 256 + raw[i + 1])

    if len(values) < width * height * 3:
        print("File does not contain enough pixel data")
        return None, None

    image = []
    index = 0
    for r in range(height):
        row = []
        for c in range(width):
            row.append([values[index], values[index + 1], values[index + 2]])
            index += 3
        image.append(row)

    return image, max_value


def save_ppm(filename, img, max_value):
    height = len(img)
    width = len(img[0])

    with open(filename, "w") as file:
        file.write("P3\n")
        file.write(str(width) + " " + str(height) + "\n")
        file.write(str(max_value) + "\n")

        for row in img:
            parts = []
            for pixel in row:
                parts.append(str(pixel[0]))
                parts.append(str(pixel[1]))
                parts.append(str(pixel[2]))
            file.write(" ".join(parts) + "\n")


def print_image(title, img):
    print("\n" + title + ":")

    if len(img) <= 10 and len(img[0]) <= 10:
        for row in img:
            print(row)
    else:
        print("Size:", len(img[0]), "x", len(img), "(too large to print)")


def create_sample_ppm(filename):
    width = 8
    height = 8
    img = []

    for r in range(height):
        row = []
        for c in range(width):
            if r == 0 or c == 0 or r == height - 1 or c == width - 1:
                row.append([200, 30, 30])
            elif r == 3 and c == 4:
                row.append([255, 255, 255])
            elif c < 4:
                row.append([30, 80 + r * 15, 200])
            else:
                row.append([240, 180 - r * 10, 40])
        img.append(row)

    save_ppm(filename, img, 255)


def invert_image(img, max_value):
    result = []

    for row in img:
        new_row = []
        for pixel in row:
            new_row.append([
                max_value - pixel[0],
                max_value - pixel[1],
                max_value - pixel[2]
            ])
        result.append(new_row)

    return result


def adjust_brightness(img, amount, max_value):
    result = []

    for row in img:
        new_row = []
        for pixel in row:
            new_pixel = []
            for channel in pixel:
                value = channel + amount

                if value > max_value:
                    value = max_value

                if value < 0:
                    value = 0

                new_pixel.append(value)
            new_row.append(new_pixel)
        result.append(new_row)

    return result


def threshold_image(img, threshold, max_value):
    result = []

    for row in img:
        new_row = []
        for pixel in row:
            gray = 0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2]

            if gray >= threshold:
                new_row.append(pixel[:])
            else:
                new_row.append([0, 0, 0])
        result.append(new_row)

    return result


def flip_horizontal(img):
    result = []

    for row in img:
        result.append(row[::-1])

    return result


def rotate_clockwise(img):
    rows = len(img)
    cols = len(img[0])

    result = []

    for col in range(cols):
        new_row = []
        for row in range(rows - 1, -1, -1):
            new_row.append(img[row][col][:])
        result.append(new_row)

    return result


def blur_image(img):
    rows = len(img)
    cols = len(img[0])

    result = []
    for row in img:
        result.append([pixel[:] for pixel in row])

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            totals = [0, 0, 0]

            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    neighbour = img[r + dr][c + dc]
                    totals[0] += neighbour[0]
                    totals[1] += neighbour[1]
                    totals[2] += neighbour[2]

            result[r][c] = [
                round(totals[0] / 9),
                round(totals[1] / 9),
                round(totals[2] / 9)
            ]

    return result


def save_png(filename, img, max_value=255):
    height = len(img)
    width = len(img[0])

    raw = bytearray()
    for row in img:
        raw.append(0)
        for pixel in row:
            for channel in pixel:
                if max_value == 255:
                    raw.append(channel)
                else:
                    raw.append(round(channel * 255 / max_value))

    def make_chunk(tag, data):
        body = tag + data
        return (struct.pack(">I", len(data)) + body
                + struct.pack(">I", zlib.crc32(body) & 0xffffffff))

    header = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)

    with open(filename, "wb") as file:
        file.write(b"\x89PNG\r\n\x1a\n")
        file.write(make_chunk(b"IHDR", header))
        file.write(make_chunk(b"IDAT", zlib.compress(bytes(raw))))
        file.write(make_chunk(b"IEND", b""))
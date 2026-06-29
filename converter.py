from PIL import Image

ASCII = "@%#*+=-:. "


def image_to_ascii(path):
    image = Image.open(path)

    image = image.convert("L")

    width = 100
    height = int(image.height * width / image.width / 2)

    image = image.resize((width, height))

    pixels = image.getdata()

    chars = "".join(ASCII[pixel * len(ASCII) // 256] for pixel in pixels)

    ascii_image = ""

    for i in range(0, len(chars), width):
        ascii_image += chars[i:i+width] + "\n"

    with open("output.txt", "w") as file:
        file.write(ascii_image)

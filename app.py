from PIL import Image, ImageFont, ImageDraw
import numpy as np
import os

width = 1100
height = 1100
font = ImageFont.truetype("fonts/Play-Regular.ttf", 55)

if not os.path.isdir("output"):
    os.mkdir("output")


def make_table(f_name):
    digit_pool = np.array(list(range(1, 101)))
    np.random.shuffle(digit_pool)
    sliced_pool = digit_pool.reshape((10, 10))
    coord = list(range(100, 1100, 100))

    img = Image.new(mode="RGB", size=(width, height), color=(255, 255, 255))
    cell = ImageDraw.Draw(img)
    cell.line(
        [(30, 30), (30, 1070), (1070, 1070), (1070, 30), (30, 30)],
        fill="black",
        width=4,
    )

    for x, row in zip(coord, sliced_pool):
        for y, col in zip(coord, row):
            cell.text((x, y), f"{col}", (0, 0, 0), font=font, anchor="mm")

    img.save(f"output/{f_name}.jpg")


if __name__ == "__main__":
    for i in range(10):
        make_table(f_name=i)

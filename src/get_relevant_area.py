from pathlib import Path

from PIL import Image

import config


def is_color_within_tolerance(color1, color2, tolerance=0.01):
    return all(abs(c1 - c2) <= 255 * tolerance for c1, c2 in zip(color1, color2))


def find_largest_rectangle_with_color(image, target_color, tolerance=0.01):
    image_width, image_height = image.size
    pixels = image.load()

    max_area = 0
    max_rectangle = None
    x = 0
    y = 0

    while x < image_width and y < image_height:
        if is_color_within_tolerance(pixels[x, y][:3], target_color, tolerance):
            w = 0
            h = 0

            while is_color_within_tolerance(pixels[x + w, y][:3], target_color, tolerance):
                w += 1

                if x + w == image_width:
                    break

            while is_color_within_tolerance(pixels[x, y + h][:3], target_color, tolerance):
                h += 1

                if y + h == image_height:
                    break

            area = w * h

            if area > max_area:
                max_area = area
                max_rectangle = (x, y, x + w, y + h)

            x += w
            y += h
        else:
            x += 1

            if x == image_width:
                x = 0
                y += 1

    return max_rectangle


def extract_rectangle_from_image(image_path: Path, output_path: Path, tolerance=0.01):
    image = Image.open(image_path).convert("RGB")

    if rectangle := find_largest_rectangle_with_color(image, tuple(int(config.target_color[i:i + 2], 16) for i in (0, 2, 4)), tolerance):
        output_path = output_path
        image.crop(rectangle).save(output_path)
        return output_path

    raise ValueError(f"Could not find a rectangle with color {config.target_color} +- {tolerance * 100}% in the image {image_path.absolute()}")

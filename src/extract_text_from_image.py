from pathlib import Path

import pytesseract
from PIL import Image
import config


def extract_question_from_image(image_path: Path, output_path: Path):
    pytesseract.pytesseract.tesseract_cmd = config.tesseract_bin

    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang=config.tesseract_lang)

    with open(output_path, 'w+') as file:
        file.write(text.split('\n\n')[0])

    return output_path

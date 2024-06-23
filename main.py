import time
from pathlib import Path

import config
from src.display_dialog import display_dialog
from src.extract_text_from_image import extract_question_from_image
from src.get_ai_answer import ask_gpt_img
from src.get_relevant_area import extract_rectangle_from_image
from src.helpers import random_string
from src.screenshot import take_screenshot


def main():
    time.sleep(config.sleep_on_start)

    while True:
        try:
            base_path = Path.cwd() / 'images'
            file_path = take_screenshot(base_path / 'raw' / (random_string() + '.png'))
            cropped_file_path = extract_rectangle_from_image(file_path, base_path / 'cro' / file_path.name, 0.01)
            ocr_file_path = extract_question_from_image(cropped_file_path, base_path / 'ocr' / cropped_file_path.name.replace('.png', '.txt'))
            answer_path = ask_gpt_img(cropped_file_path, base_path / 'ans' / cropped_file_path.name.replace('.png', '.txt'), config.api_key)

            if "button returned:OK" not in display_dialog(answer_path, ocr_file_path):
                break

            time.sleep(config.sleep_on_success)
        except ValueError as e:
            print(f'Error: {e}')
            time.sleep(config.sleep_on_error)
        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    main()

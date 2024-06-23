import subprocess
from pathlib import Path


def read_text_file(file_path: Path) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def display_dialog(file_path, question_file_path=None):
    text = ""

    if question_file_path:
        question = read_text_file(question_file_path)
        text = f"Question: {question}\n\n"

    text += read_text_file(file_path)
    result = subprocess.run(["osascript", "-e", f'display dialog "{text}"'], capture_output=True, text=True)
    return result.stdout

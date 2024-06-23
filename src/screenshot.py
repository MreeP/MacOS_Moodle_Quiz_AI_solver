import os
from pathlib import Path


def take_screenshot(file_path: Path):
    os.system(f"screencapture -x -R 0,0,3024,1964 {file_path.absolute()}")
    return file_path

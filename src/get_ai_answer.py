import base64
from pathlib import Path

from openai import Client


def read_text_file(file_path: Path) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def get_openai_image_response(b64_image: str, api_key: str) -> str:
    response = Client(api_key=api_key).chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant who solves whatever task he is given and answers questions. Please include the answer in the text below and match its format with the question from image. If there are multiple choices please display list with: [] Wrong and [x] Right answers."
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What is the answer for the task in the image below? Select all correct answers."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{b64_image}"
                        }
                    }
                ]
            }
        ],
        max_tokens=200,
    )

    return response.choices[0].message.content.strip()


def encode_img(image_path: Path) -> str:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def ask_gpt_img(file_path: Path, output_path: Path, api_key: str):
    b64_image = encode_img(file_path)
    answer = get_openai_image_response(b64_image, api_key)

    with open(output_path, 'w+') as file:
        file.write(answer)

    return output_path

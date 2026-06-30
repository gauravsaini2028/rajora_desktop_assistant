import pyautogui
import base64
from pathlib import Path
from datetime import datetime
from openai import OpenAI 
from .config import(
    OPENROUTER_API_KEY,
    MODEL_NAME,
    DEFAULT_PROMPT,
    MAX_TOKENS,
    TEMPERATURE,
)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

SCREENSHOT_DIR = Path("screenshots")


def capture_screen():
    SCREENSHOT_DIR.mkdir(exist_ok=True)
    filename = datetime.now().strftime("%Y%m%d_%H%M%S.png")
    image_path = SCREENSHOT_DIR / filename
    screenshot = pyautogui.screenshot()
    screenshot.save(image_path)
    return image_path


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(
            image_file.read()
        ).decode("utf-8")
     

def build_messages(prompt, image_base64):

    return [
        {
            "role": "system",
            "content": """You are Rajora AI, an AI desktop assistant.
                        Analyze the screenshot.
                        Respond ONLY in this format:
                        ## Open Applications
                        ## Active Window
                        ## Visible Text
                        ## Errors
                        ## Summary
                        Be concise.
                        Do not describe colors or UI decorations unless asked.
                        Focus on information useful for desktop automation.
                        """
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompt,
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{image_base64}"
                    },
                },
            ],
        },
    ]


def call_model(messages):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
    )

    print("=" * 80)
    print(response.model_dump())
    print("=" * 80)

    return response.choices[0].message.content


def analyze_screen(prompt=DEFAULT_PROMPT):
    image_path = capture_screen()

    image_base64 = encode_image(image_path)

    messages = build_messages(
        prompt,
        image_base64,
    )

    return call_model(messages)
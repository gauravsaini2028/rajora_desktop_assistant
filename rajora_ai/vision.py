import pyautogui
import base64
from pathlib import Path
from datetime import datetime
from openai import OpenAI 
from .logger import logger
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
    logger.info("Capturing desktop screenshot")
    SCREENSHOT_DIR.mkdir(exist_ok=True)
    filename = datetime.now().strftime("%Y%m%d_%H%M%S.png")
    image_path = SCREENSHOT_DIR / filename
    screenshot = pyautogui.screenshot()
    screenshot.save(image_path)
    logger.info(f"Screenshot saved to {image_path}")
    return image_path


def encode_image(image_path):
    logger.info("Encoding screenshot to Base64")
    with open(image_path, "rb") as image_file:
        return base64.b64encode(
            image_file.read()
        ).decode("utf-8")
     

def build_messages(prompt, image_base64):
    logger.info("Building messages for vision model")
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
    logger.info(f"Sending request to model: {MODEL_NAME}")
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
        )
    except Exception:
        logger.exception("Failed to communicate with OpenRouter")
        raise

    print("=" * 80)
    print(response.model_dump())
    print("=" * 80)
    logger.info("Received response from vision model")
    return response.choices[0].message.content


def analyze_screen(prompt=DEFAULT_PROMPT):
    image_path = capture_screen()

    image_base64 = encode_image(image_path)

    messages = build_messages(
        prompt,
        image_base64,
    )

    return call_model(messages)
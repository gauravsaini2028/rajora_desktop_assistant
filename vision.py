import pyautogui
import base64
from openai import OpenAI 
from config import OPENROUTER_API_KEY

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

def take_screenshot(path="screenshots/screen.png"):
    image = pyautogui.screenshot()
    image.save(path)
    return path

def encode_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")
    
def analyze_screen():
    image_path = take_screenshot()
    image_base64 = encode_image(image_path)

    response = client.chat.completions.create(
        model="google/gemma-4-31b-it:free",
        messages=[
            {
                "role": "user",
                "content" : [
                    {"type": "text", "text": "Describe everything visible on my screen."},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_base64}"
                        }
                    }
                ]
            }
        ]
    )
    return response.choices[0].message.content
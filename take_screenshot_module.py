import platform
import os
from PIL import ImageGrab
import pyautogui

def take_screenshot():
    try:
        system_name = platform.system()

        if system_name == "Windows" or system_name == "Darwin":
            screenshot = ImageGrab.grab()
            screenshot.save("screenshot.png")
            print("Screenshot saved as screenshot.png")

        elif system_name == "Linux":
            os.system("xhost +")
            try:
                screenshot = pyautogui.screenshot()
                screenshot.save("screenshot2.png")
                print("Screenshot saved as screenshot2.png")
            except Exception as e:
                print(f"Failed to capture screenshot: {str(e)}")
                
        else:
            print(f"Unsupported platform: {system_name}")

    except Exception as e:
        print(f"Failed to capture screenshot: {str(e)}")

take_screenshot()

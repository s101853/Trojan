import platform
import os
from PIL import ImageGrab 
import pyautogui 

def take_screenshot():
    try:
        system_name = platform.system()

        if system_name == "Windows" or system_name == "Darwin": 
            # Use ImageGrab for Windows and macOS
            screenshot = ImageGrab.grab()
            screenshot.save("screenshot.png")
            print("Screenshot saved as screenshot.png")

        elif system_name == "Linux":
            def take_screenshot():
                try:
                    screenshot = pyautogui.screenshot()
                    screenshot.save("screenshot.png")
                    print("Screenshot saved as screenshot.png")
                except Exception as e:
                    print(f"Failed to capture screenshot: {str(e)}")
            
            take_screenshot()

        else:
            print(f"Unsupported platform: {system_name}")

    except Exception as e:
        print(f"Failed to capture screenshot: {str(e)}")

take_screenshot()

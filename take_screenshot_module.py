import platform
import os
from PIL import ImageGrab  # For Windows and macOS
import mss  # For Linux
import pyautogui  # For cross-platform support

def take_screenshot():
    try:
        system_name = platform.system()

        if system_name == "Windows" or system_name == "Darwin":  # "Darwin" is macOS
            # Use ImageGrab for Windows and macOS
            screenshot = ImageGrab.grab()
            screenshot.save("screenshot.png")
            print("Screenshot saved as screenshot.png")

        elif system_name == "Linux":
            # On Linux, use mss to capture the screenshot (works in headless environments)
            if os.environ.get("DISPLAY", "") == "":
                print("No display found, running in headless mode, using mss to capture screenshot.")
            
            # Using mss for Linux (avoids the XGetImage() failure)
            with mss.mss() as sct:
                screenshot = sct.shot(output="screenshot.png")
                print("Screenshot saved as screenshot.png")

        else:
            print(f"Unsupported platform: {system_name}")

    except Exception as e:
        print(f"Failed to capture screenshot: {str(e)}")

take_screenshot()

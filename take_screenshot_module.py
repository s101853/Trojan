import platform
from PIL import ImageGrab  # For Windows and macOS
import pyautogui  # For cross-platform support
import mss  # For cross-platform support on Linux

def take_screenshot():
    try:
        system_name = platform.system()

        if system_name == "Windows" or system_name == "Darwin":  # "Darwin" is macOS
            # Use ImageGrab for Windows and macOS
            screenshot = ImageGrab.grab()
            screenshot.save("screenshot.png")
            print("Screenshot saved as screenshot.png")

        elif system_name == "Linux":
            # Use mss for Linux (Ubuntu)
            with mss.mss() as sct:
                screenshot = sct.shot(output="screenshot.png")
                print("Screenshot saved as screenshot.png")

        else:
            print(f"Unsupported platform: {system_name}")
    
    except Exception as e:
        print(f"Failed to capture screenshot: {str(e)}")

take_screenshot()

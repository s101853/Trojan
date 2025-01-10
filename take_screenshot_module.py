utabimport platform
import os
from PIL import ImageGrab
import pyautogui
import subprocess

def take_screenshot():
    try:
        system_name = platform.system()

        if system_name == "Windows" or system_name == "Darwin":
            # Use ImageGrab for Windows and macOS
            screenshot = ImageGrab.grab()
            screenshot.save("screenshot.png")
            print("Screenshot saved as screenshot.png")

        elif system_name == "Linux":
            # Use subprocess to run xhost +
            subprocess.run("xhost +", executable="/bin/bash", shell=True, check=True)
            try:
                screenshot = pyautogui.screenshot()
                screenshot.save("screenshot2.png")
                print("Screenshot saved as screenshot2.png")
            except Exception as e:
                print(f"Failed to capture screenshot: {str(e)}")
            finally:
                # Revoke the permission after taking the screenshot
                subprocess.run("xhost -", executable="/bin/bash", shell=True, check=True)

        else:
            print(f"Unsupported platform: {system_name}")

    except Exception as e:
        print(f"Failed to capture screenshot: {str(e)}")

take_screenshot()

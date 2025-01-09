from PIL import ImageGrab

def take_screenshot():
    try:
        screenshot = ImageGrab.grab()
        screenshot.save("screenshot2.png")

    except Exception as e:
        print(f"Failed to capture screenshot: {str(e)}")

take_screenshot()


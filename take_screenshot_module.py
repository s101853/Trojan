def take_screenshot():
    try:
        # Capture the screenshot
        screenshot = pyautogui.screenshot()

        # Save the screenshot
        screenshot.save("screenshot.png")

        print("Screenshot captured successfully.")
    except Exception as e:
        print(f"Failed to capture screenshot: {str(e)}")

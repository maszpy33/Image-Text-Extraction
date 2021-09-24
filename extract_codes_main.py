import cv2
import pytesseract as pt
import time
import re
import pyautogui
import os

SCREENSHOT_NAME = "my_screenshot.png"


def regexMatch(word: str) -> (bool, str):
    # \w matches a-z, A-Z and 0-9
    pattern = re.compile(r"\w\w\w\w\w[-]\w\w\w\w\w")

    if (re.search(pattern, word)):
        print("valid code")
        matches = pattern.search(word)
        code = matches.group()
        print("Code:", code)

        return True, code
    else:
        print("no code found")
        return False, "non"


def handleScreenshot():
    if os.path.exists(SCREENSHOT_NAME):
        os.remove(SCREENSHOT_NAME)
        print("DELETED CURRENT SCREENSHOT")
        
        screenshot = pyautogui.screenshot(SCREENSHOT_NAME)
        print("TOOK NEW SCREENSHOT")
    else:
        print("TAKE SCREENSHOT")
        screenshot = pyautogui.screenshot(SCREENSHOT_NAME)


def writeToFile(code: str):
    with open("rabatt_codes.txt", "a") as codesFile:
        codesFile.write(code + "\n") 


if __name__ == "__main__":

    while True:
        print("------------START------------")
        start = time.time()

        # take or delete screenshot
        handleScreenshot()

        # image as an np.array
        img = cv2.imread(SCREENSHOT_NAME)

        # extract text from image
        text = pt.image_to_string(img)
        
        # extract code from string with regex
        is_valid_code, code = regexMatch(text)

        # write code to txt file
        writeToFile(code)

        print("------------END------------")
        end = time.time() 
        print("Time needed: {0}sec".format(round(end-start, 4)))

        time.sleep(4)
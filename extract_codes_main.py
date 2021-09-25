import cv2
import pytesseract as pt
import time
import re
import pyautogui
import os
import pync


SCREENSHOT_NAME = "my_screenshot.png"
code_list = []


def regexMatch(text: str) -> (bool, str):
    # \w matches a-z, A-Z and 0-9
    # pattern = re.compile(r"\w\w\w\w\w[-]\w\w\w\w\w")
    pattern = re.compile(r"[A-Z]{5}[-][A-Z]{5}")

    matches = re.findall(pattern, text)
    if len(matches) == 0:
        return False, []
    else:
        return True, matches


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
        # start time measurment for one loop
        print("------------START------------")
        start = time.time()

        # take or delete screenshot
        handleScreenshot()

        # image as an np.array
        img = cv2.imread(SCREENSHOT_NAME)

        # extract text from image
        text = pt.image_to_string(img)
        
        # extract code from string with regex
        is_valid_code, codes = regexMatch(text)

        if is_valid_code:
            for code in codes:
                # notification if a valid code is found -> by click on show in the 
                # notification window, google will be opened automatically 
                if code in code_list:
                    pass
                else:
                    # Save the code to the clipboard
                    os.system("echo '%s' | pbcopy" % code)

                    # pushup notification with button to open google
                    pync.notify("Code {0} is in clipboard".format(code), open='http://google.com/')

                    # add code to list, to prefent endless notification loop
                    code_list.append(code)

                    # write code to txt file
                    writeToFile(code)

                    print("Found Codes:")
                    print(code_list)

                    # wait for user input to continue
                    user_input = input("Press enter to continue...")

        # mesure time, how long one loop took
        print("------------END------------")
        end = time.time() 
        print("Time needed: {0}sec".format(round(end-start, 4)))

        # time.sleep(4)
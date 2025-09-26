"""
Wild Gunman autoplay.
- Use grayscale
- Use minimum confidence 0.75
- Use retroarch Fceum core
- Using 2x window in RetroAarch
- Max up zapper tolerance (fceum core options)
"""

import pyautogui
import time
from PIL import Image, ImageOps


GAMEMODES = ['A', 'B', 'C']
GAMEA = (270, 220, 80, 80)    # Small area around the eyes
GAMEBLEFT = (140, 190, 120, 120)
GAMEBRIGHT = (350, 190, 120, 120)
GAMEBFLIP = [8, 11, 13, 14, 16, 18, 25, 28, 31, 33, 38, 40, 41, 46, 48]    # Handles some exceptions in game B
SALOON = (30, 70, 500, 300)
pyautogui.FAILSAFE = True


def main(game: str):
    if game not in GAMEMODES:
        print('\nCHOOSE A GAME MODE!!!!! - A B OR C (UPPERCASE')
        quit(1)

    mendown = 0

    if game == 'C':
        gang1 = ImageOps.grayscale(Image.open('../opt/wg/b1.png'))
        gang2 = ImageOps.grayscale(Image.open('../opt/wg/b2.png'))
        gang3 = ImageOps.grayscale(Image.open('../opt/wg/b3.png'))
        gang4 = ImageOps.grayscale(Image.open('../opt/wg/b4.png'))
        gang5 = ImageOps.grayscale(Image.open('../opt/wg/b5.png'))
        mendown = 0
        while True:
            try:
                t1 = pyautogui.locateOnScreen(gang1, region=SALOON, confidence=0.85, grayscale=True)
                if t1 is not None:
                    pyautogui.mouseDown(t1[0], t1[1])
                    pyautogui.mouseUp()
                    mendown += 1
                    print(f'Gang 1 down! - Total {mendown}')

                t2 = pyautogui.locateOnScreen(gang2, region=SALOON, confidence=0.85, grayscale=True)
                if t2 is not None:
                    pyautogui.mouseDown(t2[0], t2[1])
                    pyautogui.mouseUp()
                    mendown += 1
                    print(f'Gang 2 down! - Total {mendown}')

                t3 = pyautogui.locateOnScreen(gang3, region=SALOON, confidence=0.85, grayscale=True)
                if t3 is not None:
                    pyautogui.mouseDown(t3[0], t3[1])
                    pyautogui.mouseUp()
                    mendown += 1
                    print(f'Gang 3 down! - Total {mendown}')

                t4 = pyautogui.locateOnScreen(gang4, region=SALOON, confidence=0.7, grayscale=True)
                if t4 is not None:
                    pyautogui.mouseDown(t4[0] + 10, t4[1] + 10)
                    pyautogui.mouseUp()
                    mendown += 1
                    print(f'Gang 4 down! - Total {mendown}')

                t5 = pyautogui.locateOnScreen(gang5, region=SALOON, confidence=0.85, grayscale=True)
                if t5 is not None:
                    pyautogui.mouseDown(t5[0], t5[1])
                    pyautogui.mouseUp()
                    mendown += 1
                    print(f'Gang 5 down! - Total {mendown}')
            except pyautogui.ImageNotFoundException:
                print("\rSearching...", end='')


    elif game == 'A':
        fire = ImageOps.grayscale(Image.open('../opt/wg/fireeye.png'))   # Shared by every target
        while True:
            try:
                target = pyautogui.locateOnScreen(fire, region=GAMEA, confidence=0.85, grayscale=True)
                if target is not None:
                    pyautogui.mouseDown(target[0], target[1])
                    pyautogui.mouseUp()
                    mendown += 1
                    print(f'Gang down! - Total {mendown}')
                    time.sleep(4)    # Prevents from shooting twice and saves a little processing
            except pyautogui.ImageNotFoundException:
                print("\rSearching...", end='')


    elif game == 'B':
        level = 1
        offset = 210
        fire = ImageOps.grayscale(Image.open('../opt/wg/fireeye.png'))  # Shared by every target
        while True:
            try:
                if level not in GAMEBFLIP:
                    target = pyautogui.locateOnScreen(fire, region=GAMEBLEFT, confidence=0.85, grayscale=True)
                else:
                    target = pyautogui.locateOnScreen(fire, region=GAMEBRIGHT, confidence=0.85, grayscale=True)
                    offset = -abs(offset)
                if target is not None:
                    pyautogui.mouseDown(target[0], target[1])
                    pyautogui.mouseUp()
                    pyautogui.mouseDown(target[0] + offset, target[1] - 10)
                    pyautogui.mouseUp()
                    print(f'Cleared round: {level}')
                    # time.sleep(2)
                    level += 1
                    offset = abs(offset)
            except pyautogui.ImageNotFoundException:
                print("\rSearching...", end='')


if __name__ == '__main__':
    main(game='C')

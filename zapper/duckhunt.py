"""
Duck Hunt autoplay.
- Use grayscale
- Use minimum confidence 0.8
- Use retroarch Fceum core
- Use max 2x window scale on RA
- Max up zapper tolerance (fceum core options)
"""

import pyautogui
from PIL import Image, ImageOps


REGIAO = (10, 60, 280, 130)

D1 = ImageOps.grayscale(Image.open('../opt/dh/d1.png'))
D2 = ImageOps.grayscale(Image.open('../opt/dh/d2.png'))
D3 = ImageOps.grayscale(Image.open('../opt/dh/d3.png'))


def main():
    while True:
        duck1 = pyautogui.locateOnScreen(D1, region=REGIAO, confidence=0.85, grayscale=True)
        if duck1 is not None:
            pyautogui.mouseDown(duck1[0], duck1[1])
            pyautogui.mouseUp()
            print(f'Duck template 1 down!: {duck1}')

        duck2 = pyautogui.locateOnScreen(D2, region=REGIAO, confidence=0.85, grayscale=True)
        if duck2 is not None:
            pyautogui.mouseDown(duck2[0], duck2[1])
            pyautogui.mouseUp()
            print(f'Duck template 2 down!: {duck2}')

        duck3 = pyautogui.locateOnScreen(D3, region=REGIAO, confidence=0.85, grayscale=True)
        if duck3 is not None:
            pyautogui.mouseDown(duck3[0], duck3[1])
            pyautogui.mouseUp()
            print(f'Duck template 3 down!: {duck3}')


if __name__ == '__main__':
    main()


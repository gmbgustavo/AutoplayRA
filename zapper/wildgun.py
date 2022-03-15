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


SALOON = (20, 70, 530, 320)

B1 = ImageOps.grayscale(Image.open('../opt/wg/b1.png'))
B2 = ImageOps.grayscale(Image.open('../opt/wg/b2.png'))
B3 = ImageOps.grayscale(Image.open('../opt/wg/b3.png'))
B4 = ImageOps.grayscale(Image.open('../opt/wg/b4.png'))
B5 = ImageOps.grayscale(Image.open('../opt/wg/b5.png'))


def main():
    while True:
        t1 = pyautogui.locateOnScreen(B1, region=SALOON, confidence=0.85, grayscale=True)
        if t1 is not None:
            pyautogui.mouseDown(t1[0], t1[1])
            pyautogui.mouseUp()
            print(f'Target 1 down!: {t1}')

        t2 = pyautogui.locateOnScreen(B2, region=SALOON, confidence=0.85, grayscale=True)
        if t2 is not None:
            pyautogui.mouseDown(t2[0], t2[1])
            pyautogui.mouseUp()
            print(f'Target 2 down!: {t2}')

        t3 = pyautogui.locateOnScreen(B3, region=SALOON, confidence=0.85, grayscale=True)
        if t3 is not None:
            pyautogui.mouseDown(t3[0], t3[1])
            pyautogui.mouseUp()
            print(f'Target 3 down!: {t3}')

        t4 = pyautogui.locateOnScreen(B4, region=SALOON, confidence=0.85, grayscale=True)
        if t4 is not None:
            pyautogui.mouseDown(t4[0], t4[1])
            pyautogui.mouseUp()
            print(f'Target 4 down!: {t4}')

        t5 = pyautogui.locateOnScreen(B5, region=SALOON, confidence=0.85, grayscale=True)
        if t5 is not None:
            pyautogui.mouseDown(t5[0], t5[1])
            pyautogui.mouseUp()
            print(f'Target 5 down!: {t5}')


if __name__ == '__main__':
    main()


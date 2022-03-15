"""
Usar grayscale

"""

import pyautogui
from PIL import Image, ImageOps


REGIAO = (10, 60, 550, 350)

GA = ImageOps.grayscale(Image.open('../opt/ha/ga.png'))
GB = ImageOps.grayscale(Image.open('../opt/ha/gb.png'))
GC = ImageOps.grayscale(Image.open('../opt/ha/gc.png'))


def main():
    while True:
        bandido = pyautogui.locateOnScreen(GA, region=REGIAO, confidence=0.8, grayscale=True)
        if bandido is not None:
            pyautogui.mouseDown(bandido[0], bandido[1])
            pyautogui.mouseUp()
            print(f'GANG-A: {bandido}')

        bandido2 = pyautogui.locateOnScreen(GB, region=REGIAO, confidence=0.8, grayscale=True)
        if bandido2 is not None:
            pyautogui.mouseDown(bandido2[0], bandido2[1])
            pyautogui.mouseUp()
            print(f'GANG-B: {bandido2}')

        bandido3 = pyautogui.locateOnScreen(GC, region=REGIAO, confidence=0.8, grayscale=True)
        if bandido3 is not None:
            pyautogui.mouseDown(bandido3[0], bandido3[1])
            pyautogui.mouseUp()
            print(f'GANG-C: {bandido3}')


if __name__ == '__main__':
    main()


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


REGIAO = (10, 60, 550, 350)
TRICKSHOT = (60, 290, 520, 70)

GA = ImageOps.grayscale(Image.open('../opt/ha/ga.png'))
GB = ImageOps.grayscale(Image.open('../opt/ha/gb.png'))
GC = ImageOps.grayscale(Image.open('../opt/ha/gc.png'))
CAN1 = ImageOps.grayscale(Image.open('../opt/ha/can1.png'))
CAN2 = ImageOps.grayscale(Image.open('../opt/ha/can2.png'))


def main():
    while True:
        try:
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
        except pyautogui.ImageNotFoundException:
            print("\rSearching...", end='')


def trickshot():
    pass


if __name__ == '__main__':
    main()
    # trickshot()


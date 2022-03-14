import pyautogui
from PIL import Image, ImageOps


POSICAO = (10, 60, 550, 350)

GA = ImageOps.grayscale(Image.open('./opt/ha/ga.png'))
GB = ImageOps.grayscale(Image.open('./opt/ha/gb.png'))
GC = ImageOps.grayscale(Image.open('./opt/ha/gc.png'))


def main():
    while True:
        bandido = pyautogui.locateOnScreen(GA, region=POSICAO, confidence=0.8, grayscale=True)
        if bandido is not None:
            tiro = pyautogui.center(bandido)
            pyautogui.moveTo(tiro)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            pyautogui.moveTo(800, 800)
            print(f'GANG-A: {tiro}')

        bandido = pyautogui.locateOnScreen(GB, region=POSICAO, confidence=0.8, grayscale=True)
        if bandido is not None:
            tiro = pyautogui.center(bandido)
            pyautogui.moveTo(tiro)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            pyautogui.moveTo(800, 800)
            print(f'GANG-B: {tiro}')

        bandido = pyautogui.locateOnScreen(GC, region=POSICAO, confidence=0.8, grayscale=True)
        if bandido is not None:
            tiro = pyautogui.center(bandido)
            pyautogui.moveTo(tiro)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            pyautogui.moveTo(800, 800)
            print(f'GANG-C: {tiro}')


if __name__ == '__main__':
    main()


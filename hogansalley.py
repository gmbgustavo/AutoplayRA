import pyautogui


POSICAO = (10, 60, 280, 170)


def main():
    while True:
        bandido = pyautogui.locateOnScreen('./opt/ha/b1.png', region=POSICAO, confidence=0.8)
        if bandido is not None:
            tiro = pyautogui.center(bandido)
            pyautogui.moveTo(tiro)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            pyautogui.moveTo(800, 800)
            print(f'GANG-B: {tiro}')

        bandido = pyautogui.locateOnScreen('./opt/ha/b2.png', region=POSICAO, confidence=0.8)
        if bandido is not None:
            tiro = pyautogui.center(bandido)
            pyautogui.moveTo(tiro)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            pyautogui.moveTo(800, 800)
            print(f'GANG-A: {tiro}')

        bandido = pyautogui.locateOnScreen('./opt/ha/b3.png', region=POSICAO, confidence=0.8)
        if bandido is not None:
            tiro = pyautogui.center(bandido)
            pyautogui.moveTo(tiro)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            pyautogui.moveTo(800, 800)
            print(f'GANG-C: {tiro}')


if __name__ == '__main__':
    main()


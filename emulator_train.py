import cv2
import numpy as np
from stable_baselines3 import DQN
from stable_baselines3.common.vec_env import DummyVecEnv, VecFrameStack


# Dimensões da janela do jogo
window_width = 105
window_height = 80


def make_env():
    return DummyVecEnv(lambda: CustomEnv(preprocess_screen))


def preprocess_screen(screen):
    # Redimensionar a imagem para 105x80 pixels
    resized_screen = cv2.resize(screen, (105, 80))
    # Converter a imagem para escala de cinza
    gray_screen = cv2.cvtColor(resized_screen, cv2.COLOR_BGR2GRAY)
    return gray_screen


def get_env():
    # Capturar a janela do jogo
    screenshot = pyautogui.screenshot(region=(0, 0, window_width, window_height))
    # Converter screenshot para um array numpy
    img_array = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)
    return img_array


while True:
    # Passar a imagem processada para o agente de reinforcement learning
    action = agent.act(processed_img)

    # Executar ação no jogo usando pydirectinput
    perform_action(action)

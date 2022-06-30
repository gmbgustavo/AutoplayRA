"""
DQN Reinforcement Learning using game screenshots
Exmple using Chrome Dino Game
It captures a screenshot, preprocess the image and then use it as the environment
The inputs are keyboard strikes done with pydirectinput

- Requirements:
    pytorch, stable_baselines3, pydirectinput, opencv, protobuf(3.20), pytesseract (optional, for text)
    mss (for screenshot, faster),

"""

import pydirectinput    # Send commands
import numpy as np
import pytesseract
import time
import cv2
from mss import mss    # Get screenshots
from gym import Env
from gym.spaces import Discrete, Box    # Discrete for commands and Box to environment


class ScreenGame(Env):

    def __init__(self):
        super().__init__()
        self.observation_space = Box(low=0, high=255, shape=(1, 83, 100), dtype=np.uint8)
        self.action_space = Discrete(3)    # Jump, get down, noop
        self.cap = mss()    # Instancia a função de screenshot
        # Coordenadas do jogo, o espaço de observação.
        self.game_location = {'top': 300, 'left': 0, 'width': 600, 'height': 500}
        # Coordenadas da tela onde está a informação de game over para definir se o episodio terminou.
        self.done_location = {'top': 405, 'left': 630, 'width': 660, 'height': 70}

    def step(self, action):    # Step é como passamos as ações para o jogo
        # 0 - Jump. 1 - Duck. 2 - No op.
        pass

    def render(self, mode="human"):
        pass

    def reset(self, *args):
        pass

    def get_observation(self):
        # Grab a raw captura of the game. mss returns 4 channels, we are grabbing just 3 (rgb)
        raw = np.array(self.cap.grab(self.game_location))[:, :, :3]    # Toda altura, toda largura e 3 canais
        # Tratamento da imagem para redução de tamanho
        gray = cv2.cvtColor(raw, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray, (100, 83))    # Coloca do tamanho do Box
        observation = np.reshape(resized, (1, 83, 100))    # Troca a ordem para coincidir com o padrão Box
        return observation

    def get_done(self):
        pass

    def close(self):
        pass


if __name__ == "__main__":
    env = ScreenGame()
    env.action_space.sample()
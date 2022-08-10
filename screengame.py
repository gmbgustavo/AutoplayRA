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
import pyautogui
import numpy as np
import time
import cv2
from mss import mss    # Get screenshots
from gym import Env
from gym.spaces import Discrete, Box    # Discrete for commands and Box to environment
from PIL import Image, ImageOps


class ScreenGame(Env):

    def __init__(self):
        super().__init__()
        self.observation_space = Box(low=0, high=255, shape=(1, 120, 190), dtype=np.uint8)
        self.action_space = Discrete(2)    # Up, noop
        self.cap_obs = mss()    # Instancia a função de screenshot
        # Coordenadas do jogo, o espaço de observação.
        self.game_location = {'top': 30, 'left': 60, 'width': 240, 'height': 380}
        self.score_location = {'top': 140, 'left': 410, 'width': 60, 'height': 40}    # 180 460
        # Coordenadas da tela onde está a informação de game over para definir se o episodio terminou.
        self.begin_time = int(time.time())
        self.done_time = 136    # Tempo de cada episodio
        self.reward = 0
        self.galinha = ImageOps.grayscale(Image.open('./resources/galinha.png'))

        self.action_map = {
            0: 'up',    # Seta para cima
            1: 'noop',    # Nothing
        }

    def step(self, action):    # Step é como passamos as ações para o jogo
        # 0 - UP . 1 - NOOP
        if action != 1:
            pydirectinput.press(self.action_map[action])    # Ação será passada pelo treinamento
        # Check if done
        done = self.get_done()
        new_obs = self.get_observation()
        self.reward = self.get_points()
        info = {'reward': self.reward}
        return new_obs, self.reward, done, info

    def render(self, mode="human"):
        pass

    def reset(self, *args):
        time.sleep(0.02)
        pydirectinput.press('h')
        pydirectinput.press('enter')
        self.begin_time = int(time.time())
        self.reward = 0
        return self.get_observation()

    def get_observation(self):
        # Grab a raw captura of the game. mss returns 4 channels, we are grabbing just 3 (rgb)
        raw = np.array(self.cap_obs.grab(self.game_location))[:, :, :3]    # Toda altura, toda largura e 3 canais
        # Tratamento da imagem para redução de tamanho
        gray = cv2.cvtColor(raw, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray, (120, 190))    # Coloca do tamanho do Box
        observation = np.reshape(resized, (1, 120, 190))    # Troca a ordem para coincidir com o padrão Box
        return observation

    def get_done(self):
        done = False
        time_elapsed = int(time.time()) - int(self.begin_time)
        if time_elapsed >= self.done_time:
            return True
        else:
            return done

    def get_points(self):
        # score = np.array(self.cap_obs.grab(self.score_location))
        score = pyautogui.locateOnScreen(self.galinha, region=self.score_location, confidence=0.8, grayscale=True)
        if score is not None:
            return 1
        else:
            return 0

        return score

    def close(self):
        pydirectinput.keyDown('alt')
        pydirectinput.press('f4')
        pydirectinput.keyUp('alt')
        return None


if __name__ == "__main__":
    print('Essa classe não deve ser executada diretamente.')

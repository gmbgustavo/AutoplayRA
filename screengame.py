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
import cv2
import numpy as np
import pytesseract
import time
from mss import mss    # Get screenshots
from gym import Env
from gym.spaces import Discrete, Box    # Discrete for commands and Box to environment


class ScreenGame(Env):

    def __init__(self):
        super().__init__()
        self.observation_space = Box(low=0, high=255, shape=(1, 83, 100), dtype=np.uit8)
        self.action_space = Discrete(3)    # Jump, get down, noop

    def step(self, action):    # Step é como passamos as ações para o jogo
        pass

    def render(self, mode="human"):
        pass

    def reset(self, *args):
        pass

    def get_observation(self):
        pass

    def get_done(self):
        pass

    def close(self):
        pass


if __name__ == "__main__":
    pass

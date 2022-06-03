"""
Dependencias: gym, stable_baselines3
Importação das roms python -m retro.import  ./romfolder
Essa classe cria um jogo usando um ambiente custmoizado
"""

import numpy as np
import gym
import cv2
from gym.spaces import Box, Discrete    # Wrappers
from gym import Env    # Clase ambiente básica
from stable_baselines3.common.env_util import make_atari_env
from stable_baselines3.common.vec_env import VecFrameStack


JOGO = 'ALE/SpaceInvaders-v5'


class AtariGames(Env):

    def __init__(self, mode=None):
        super().__init__()
        self.observation_space = Box(low=0, high=255, shape=(84, 84, 3), dtype=np.uint8)
        self.action_space = Discrete(6)
        self.game = VecFrameStack(make_atari_env(JOGO, n_envs=1), 3)
        self.vidas = 3
        self.total_score = 0

    def reset(self, *args):
        obs = self.game.reset()
        self.vidas = 3
        self.total_score = 0
        return obs

    def step(self, action: np.ndarray):
        obs, reward, done, info = self.game.step(action)
        self.total_score = reward
        return obs, reward, done, info

    def render(self, mode=None):
        pass

    def close(self):
        self.game.close()


if __name__ == '__main__':
    print('\nEssa classe deve ser importada e não executada diretamente.')

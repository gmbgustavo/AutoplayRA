"""
Dependencias: gym, gym-retro
Importação das roms python -m retro.import  ./romfolder
Essa classe cria um jogo usando um ambiente custmoizado
"""

import time    # Reduzir velocidade do jogo
import numpy as np
import cv2
import gym
from gym.spaces import MultiBinary, Box, Discrete    # Wrappers
from gym import Env    # Clase ambiente básica


JOGO = 'SpaceInvaders-v0'


class AtariGames(Env):

    def __init__(self):
        super().__init__()
        self.observation_space = Box(low=0, high=255, shape=(210, 160, 1), dtype=np.uint8)
        self.action_space = Discrete(4)
        self.game = gym.make(JOGO, render_mode=None)
        self.vidas = 3
        self.score = 0

    def reset(self, *args):
        obs = self.game.reset()
        obs = self.preprocess(obs)
        self.score = 0
        self.vidas = 3
        return obs

    def step(self, action):
        obs, reward, done, info = self.game.step(action)
        obs = self.preprocess(obs)
        # Reward
        if info['lives'] < self.vidas:
            reward -= 20
            self.vidas = info['lives']
        reward = reward + info['episode_frame_number'] // 1000
        return obs, reward, done, info

    def render(self, mode='human'):
        self.game.render()

    def close(self):
        self.game.close()

    @staticmethod
    def preprocess(observation):
        """
        Deixar o jogo mais leve para o processamento: reduzindo resolução, passando para escala de cinza.
        Fazer frame Delta: "Empilhar" Frames sequenciais para que seja possível saber a ação em si e os movimentos,
        com um frame simples não é possivel inferir qual vai ser a movimentação.
        Filtrar ações: Deixar apenas os comandos relevantes.
        Mudar a função de recompensa: otimizar o aprendizado.
        :return:
        """
        gray = cv2.cvtColor(observation, cv2.COLOR_BGR2GRAY)    # Grayscale
        # resize = cv2.resize(gray, (210, 160), interpolation=cv2.INTER_CUBIC)    # Diminiu a observação
        channels = np.reshape(gray, (210, 160, 1))
        return channels


if __name__ == '__main__':
    print('\nEssa classe deve ser importada e não executada diretamente.')


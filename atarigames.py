"""
Dependencias: gym, gym-retro
Importação das roms python -m retro.import  ./romfolder
Essa classe cria um jogo usando um ambiente custmoizado
"""

import time    # Reduzir velocidade do jogo
import numpy as np
import cv2
import gym
from gym.spaces import Box, Discrete    # Wrappers
from gym import Env    # Clase ambiente básica


JOGO = 'ALE/SpaceInvaders-v5'


class AtariGames(Env):

    def __init__(self):
        super().__init__()
        self.observation_space = Box(low=0, high=255, shape=(210, 160, 1), dtype=np.uint8)
        self.action_space = Discrete(4)
        self.game = gym.make(JOGO,
                             obs_type='grayscale',    # ram | rgb | grayscale
                             frameskip=2,    # frame skip
                             mode=0,    # game mode, see Machado et al. 2018
                             difficulty=0,    # game difficulty, see Machado et al. 2018
                             repeat_action_probability=0.20,    # Sticky action probability
                             full_action_space=True,    # Use all actions
                             render_mode='rgb_array')    # None | human | rgb_array
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
        self.score = info['score'] - self.score
        self.score = info['score']
        if info['lives'] < self.vidas:
            reward -= 1000
            self.vidas = info['lives']
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
        # gray = cv2.cvtColor(observation, cv2.COLOR_BGR2GRAY)    # Grayscale - já aplicado na instância do gym
        resize = cv2.resize(observation, (210, 160), interpolation=cv2.INTER_CUBIC)    # Diminiu a observação
        channels = np.reshape(resize, (210, 160, 1))
        return channels


if __name__ == '__main__':
    print('\nEssa classe deve ser importada e não executada diretamente.')

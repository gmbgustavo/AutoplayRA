"""
Dependencias: gym, gym-retro
Importação das roms python -m retro.import  ./romfolder
Essa classe cria um jogo usando um ambiente custmoizado
"""

import retro
import time    # Reduzir velocidade do jogo
import numpy as np
import cv2
from gym.spaces import MultiBinary, Box    # Wrappers
from gym import Env    # Clase ambiente básica


JOGO = 'BalloonFight-Nes'
SHAPE = (112, 120, 3)


class OtherGames(Env):

    def __init__(self):
        super().__init__()
        self.observation_space = Box(low=0, high=255, shape=SHAPE, dtype=np.uint8)
        self.action_space = MultiBinary(9)
        self.game = retro.make(game=JOGO, use_restricted_actions=retro.Actions.FILTERED)
        # self.unwrapped.buttons = self.game.unwrapped.buttons
        # self.button_combos = self.game.unwrapped.button_combos
        self.score = 0
        self.vidas = 3

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
        reward = info['score'] - self.score    # Pontos atuais - pontos anteriores: Ganhou pontos.
        self.score = info['score']    # Armazena o atual para calcular no proximo step
        if info['lives'] < self.vidas:
            reward -= 100
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
        gray = cv2.cvtColor(observation, cv2.COLOR_BGR2GRAY)    # Grayscale
        resize = cv2.resize(gray, (112, 120), interpolation=cv2.INTER_CUBIC)    # Diminiu a observação
        channels = np.reshape(resize, (112, 120, 1))
        return channels


if __name__ == '__main__':
    print('\nEssa classe deve ser importada e não executada diretamente.')


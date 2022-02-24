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


JOGO = 'StreetFighterIISpecialChampionEdition-Genesis'


class StreetFighter(Env):

    def __init__(self):
        super().__init__()
        self.observation_space = Box(low=0, high=255, shape=(84, 84, 1), dtype=np.uint8)
        self.action_space = MultiBinary(12)
        self.game = retro.make(game=JOGO, use_restricted_actions=retro.Actions.FILTERED)
        self.score = 0
        self.vida = 176
        self.vida_oponente = 176
        self.vitorias = 0

    def reset(self, *args):
        obs = self.game.reset()
        obs = self.preprocess(obs)
        self.score = 0
        self.vida = 176
        self.vida_oponente = 176
        self.vitorias = 0
        return obs

    def step(self, action):
        obs, reward, done, info = self.game.step(action)
        obs = self.preprocess(obs)
        # Reward
        reward = info['score'] - self.score    # Pontos atuais - pontos anteriores: Ganhou pontos.
        self.score = info['score']    # Armazena o atual para calcular no proximo step
        # Colocando o fator vida na recompensa - Se houve decréscimo, penaliza com -100
        if info['health'] < self.vida:
            reward -= 200
        self.vida = info['health']
        if info['enemy_health'] < self.vida_oponente:
            reward += 150
        self.vida_oponente = info['enemy_health']
        # Colocando numero de rounds vencidos como fator de recompensa
        if info['matches_won'] > self.vitorias:
            reward += 1000
        self.vida = info['matches_won']
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
        resize = cv2.resize(gray, (84, 84), interpolation=cv2.INTER_CUBIC)    # Diminiu a observação
        channels = np.reshape(resize, (84, 84, 1))
        return channels


if __name__ == '__main__':
    print('\nEssa classe deve ser importada e não executada diretamente.')


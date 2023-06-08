"""
Dependencias: gym, gym-retro
Importação das roms python -m retro.import  ./romfolder
Essa classe cria um jogo usando um ambiente custmoizado
"""

import cv2
import numpy as np
from gym.spaces import Discrete, Box
from gym import Env
from stable_baselines3 import DQN
from stable_baselines3.common.vec_env import DummyVecEnv, VecFrameStack
import gym

JOGO = 'ALE/Frogger-v5'


class AtariGames(Env):
    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 3}

    def __init__(self, mode=None, game=JOGO):
        super().__init__()
        self.observation_space = Box(low=0, high=255, shape=(105, 80, 1), dtype=np.uint8)
        self.action_space = Discrete(5)
        self.game = gym.make(game,
                             obs_type='grayscale',    # ram | rgb | grayscale
                             frameskip=1,    # frame skip
                             mode=0,    # game mode, see Machado et al. 2018
                             difficulty=0,    # game difficulty, see Machado et al. 2018
                             repeat_action_probability=0.4,    # Sticky action probability
                             full_action_space=False,    # Use all actions or just the useful ones(False)
                             render_mode=mode,     # None | human | rgb_array
                             max_episode_steps=40000,
                             autoreset=True)
        self.vidas = 4
        self.total_score = 0

    def reset(self, *args):
        obs = self.game.reset()
        obs = self.preprocess(obs)
        self.vidas = 4
        self.total_score = 0
        return obs

    def step(self, action):
        obs, reward, done, _, info = self.game.step(action)
        obs = self.preprocess(obs)
        self.total_score += reward
        return obs, reward, done, info

    def render(self, mode=None):
        pass

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
        observation = np.asarray(observation[0])
        resize = cv2.resize(observation, (105, 80), interpolation=cv2.INTER_CUBIC)    # Diminiu a observação
        channels = np.reshape(resize, (105, 80, 1))
        return channels


if __name__ == '__main__':
    print('\nEssa classe deve ser importada e não executada diretamente.')

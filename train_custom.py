"""
Treinamento da classe do ambiente gym customizado
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113

"""

import callback    # Classe personalizada. Esta na mesma pasta
from atarigames import AtariGames
from stable_baselines3 import DQN
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.vec_env import DummyVecEnv, VecFrameStack
from stable_baselines3.common.monitor import Monitor

LOG_DIR = './logs'
OPT_DIR = './opt'    # Diretorio para otimizações dos hiperparametros
SAVE_DIR = './save'
callback = callback.TrainAndLoggingCallback(check_freq=250_000, save_path=SAVE_DIR)

JOGO = 'ALE/SpaceInvaders-v5'


def train(pesos=None):
    env = AtariGames()
    env = Monitor(env, LOG_DIR)
    env = VecFrameStack(DummyVecEnv([lambda: env]), 4, channels_order='last')
    model = DQN('CnnPolicy', env, exploration_fraction=0.25, tensorboard_log=LOG_DIR, device='cuda', verbose=1)
    if pesos is not None:
        model.load(pesos)
    model.learn(total_timesteps=2_000_000, callback=callback)
    return None


def avaliar(pesos=None):
    env = AtariGames(mode='human')
    env = Monitor(env, LOG_DIR)
    env = VecFrameStack(DummyVecEnv([lambda: env]), 4, channels_order='last')
    model = DQN.load(pesos)
    mean_reward, desvio = evaluate_policy(model, env, render=True, n_eval_episodes=3)
    return [mean_reward, desvio]


# Apresenta um jogo de demonstração com ações aleatórias, não treina e não carrega o treinamento
def samplegame():
    env = AtariGames(mode='human')
    done = False
    env.reset()
    while not done:
        env.render()
        obs, reward, done, info = env.step(env.action_space.sample())   # Ações aleatórias
        if reward != 0:
            print(info)
            print(reward)
    env.close()
    return None


def main():
    # print(avaliar('./save/best_model_'))
    train()
    # samplegame()


if __name__ == '__main__':
    main()

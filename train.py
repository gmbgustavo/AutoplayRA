"""
Treinamento da classe do ambiente gym customizado
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113
"""

from callback import TrainAndLoggingCallback    # Classe personalizada. Esta na mesma pasta
from screengame import ScreenGame
from stable_baselines3 import DQN
import time


LOG_DIR = './logs'
OPT_DIR = './opt'    # Diretorio para otimizações dos hiperparametros
SAVE_DIR = './save'
callback = TrainAndLoggingCallback(check_freq=1000, save_path=SAVE_DIR)


def train(pesos=None):
    env = ScreenGame()
    model = DQN('CnnPolicy', env, exploration_fraction=0.70, optimize_memory_usage=True,
                learning_rate=0.0099, buffer_size=500_000,
                gamma=0.98, exploration_initial_eps=0.99, exploration_final_eps=0.15,
                tensorboard_log=LOG_DIR, device='cuda', verbose=1, learning_starts=10)
    if pesos is not None:
        model.load(pesos)
    model.learn(total_timesteps=20_000_000, callback=callback)
    return None


def jogar(modelo: str):
    # Fazendo jogar com o modelo salvo
    env = ScreenGame()
    model = DQN.load(modelo)
    for episode in range(1):
        obs = env.reset()
        total_reward = 0
        done = False
        while not done:
            action, _ = model.predict(obs)
            obs, reward, done, info = env.step(int(action))
            time.sleep(0.01)
            total_reward += reward
        print(f'Pontuação total do episódio {episode} foi de {total_reward}.')
        time.sleep(2)


def samplegame(episodes):
    env = ScreenGame()
    _ = env.reset()
    for episode in range(episodes):
        total_reward = 0
        done = False
        while not done:
            obs, reward, done, info = env.step(env.action_space.sample())
            total_reward += reward
        print(f'Total reward for episode {episode} is {total_reward}.')


def main():
    jogar('./save/model_000000.zip')
    train(pesos=None)
    # samplegame()


if __name__ == '__main__':
    main()

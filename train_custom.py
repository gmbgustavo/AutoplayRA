"""
Treinamento da classe do ambiente gym customizado
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

"""

import callback    # Classe personalizada. Esta na mesma pasta
from atarigames import AtariGames
from stable_baselines3 import DQN
from stable_baselines3.common.vec_env import DummyVecEnv, VecFrameStack
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.evaluation import evaluate_policy

LOG_DIR = './logs'
OPT_DIR = './opt'    # Diretorio para otimizações dos hiperparametros
SAVE_DIR = './save'
callback = callback.TrainAndLoggingCallback(check_freq=2_000_000, save_path=SAVE_DIR)


def train(steps, pesos=None):
    env = AtariGames()
    env = Monitor(env, LOG_DIR)
    env = VecFrameStack(DummyVecEnv([lambda: env]), n_stack=4, channels_order='last')
    model = DQN('CnnPolicy', env, exploration_fraction=0.75, optimize_memory_usage=False,
                learning_rate=0.01, buffer_size=1_000,
                gamma=0.98, exploration_initial_eps=0.99, exploration_final_eps=0.2,
                tensorboard_log=LOG_DIR, device='cuda', verbose=1)
    if pesos is not None:
        model.load(pesos)
    model.learn(total_timesteps=steps, callback=callback)
    return None


# Apresenta um jogo de demonstração com ações aleatórias, não treina e não carrega o treinamento
def samplegame():
    env = AtariGames(mode='human')
    done = False
    env.reset()
    while not done:
        env.render()
        obs, reward, done, info, _ = env.step(env.action_space.sample())   # Ações aleatórias
        if reward != 0:
            print(info, reward)
    env.close()
    return None


def avaliar(pesos=None):
    env = AtariGames(mode='human')
    env = Monitor(env, LOG_DIR)
    env = VecFrameStack(DummyVecEnv([lambda: env]), 4, channels_order='last')
    model = DQN.load(pesos)
    mean_reward, desvio = evaluate_policy(model, env, render=True, n_eval_episodes=2)
    return [mean_reward, desvio]


def main():
    # print(avaliar('./save/model_30000000'))
    train(pesos=None, steps=300_000)


if __name__ == '__main__':
    main()

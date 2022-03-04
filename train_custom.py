"""
Treinamento da classe do ambiente gym customizado
pip install torch==1.10.2+cu113 -f https://download.pytorch.org/whl/torch_stable.html

"""

import optuna
import retro
import atarigames
import callback    # Classe personalizada. Esta na mesma pasta
import os
from stable_baselines3 import PPO, A2C
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.vec_env import DummyVecEnv, VecFrameStack
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.atari_wrappers import AtariWrapper

import othergames
from othergames import OtherGames

LOG_DIR = './logs'
OPT_DIR = './opt'    # Diretorio para otimizações dos hiperparametros
SAVE_DIR = './save/checkpoint'
callback = callback.TrainAndLoggingCallback(check_freq=100_000, save_path=SAVE_DIR)
JOGO = 'SpaceInvaders-Atari2600'
BEST = {'n_steps': 6400,
        'gamma': 0.92,
        'learning_rate': 2e-5,
        }


# Função para testar os hiperparametros
def ppo_opt(trial):
    return {
        'n_steps': trial.suggest_int('n_steps', 2048, 8192),
        'gamma': trial.suggest_loguniform('gamma', 0.8, 0.9999),
        'learning_rate': trial.suggest_loguniform('learning_rate', 1e-7, 1e-5),
        'clip_range': trial.suggest_uniform('clip_range', 0.1, 0.4),
        'gae_lambda': trial.suggest_uniform('gae_lambda', 0.8, 0.99)
    }


def agent_opt(trial):
    try:
        model_params = ppo_opt(trial)
        # Criar o ambiente
        env = OtherGames()
        env = atarigames.spaceinvader_discretizer(env)
        env = Monitor(env, LOG_DIR)
        env = VecFrameStack(DummyVecEnv([lambda: env]), 3, channels_order='last')
        # Criar o modelo
        save_dir = os.path.join('./save', 'trial_{}'.format(trial.number))
        model = PPO('CnnPolicy', env, tensorboard_log=LOG_DIR, device='cuda', verbose=0, **model_params)
        model.learn(total_timesteps=300_000)

        # Avaliar o modelo - O underline significa que "não vou usar essas variaveis desempacotadas"
        mean_reward, _ = evaluate_policy(model, env, n_eval_episodes=10)    # Desempacota, mas precisamos somente de 1
        env.close()
        model.save(save_dir)
        return mean_reward

    except Exception as e:    # Se houver alguma exceção ele vai continuar testando os outros parametros sem parar
        print(e)
        return -1000


def estudar_ppo():
    study = optuna.create_study(direction='maximize')
    study.optimize(agent_opt, n_trials=5, n_jobs=1)    # Mais trials para melhorar
    with open('./opt/bestparams.txt', 'a') as f:
        f.write(str(study.best_params) + '\n' + str(study.best_trial))
        f.close()


def train(pesos):
    env = OtherGames()
    env = othergames.spaceinvader_discretizer(env)
    env = VecFrameStack(DummyVecEnv([lambda: env]), 3, channels_order='last')
    # Parâmetros obtigos pelo estudo do optuna
    model = PPO('CnnPolicy', env, tensorboard_log=LOG_DIR, device='cuda', verbose=1)
    if pesos is None:
        model.load('')
    model.learn(total_timesteps=1_000_000, callback=callback)
    return None


def avaliar(pesos):
    env = OtherGames()
    env = othergames.spaceinvader_discretizer(env)
    env = Monitor(env, LOG_DIR)
    env = VecFrameStack(DummyVecEnv([lambda: env]), 3, channels_order='last')
    model = PPO.load(pesos)
    mean_reward, desvio = evaluate_policy(model, env, render=True, n_eval_episodes=5)
    return [mean_reward, desvio]


# Apresenta um jogo de demonstração com ações aleatórias, não treina e não carrega o treinamento
def samplegame():
    env = OtherGames()
    env = othergames.spaceinvader_discretizer(env)
    done = False
    env.reset()
    while not done:
        env.render()
        # time.sleep(0.01)
        obs, reward, done, info = env.step(env.action_space.sample())   # Ações aleatórias
        if reward != 0:
            print(reward)
            print(info)
    env.close()
    return None


def main():
    # avaliar('')
    train(1)
    # estudar_ppo()


if __name__ == '__main__':
    main()


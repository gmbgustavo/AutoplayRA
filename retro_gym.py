# GYM-RETRO

import retro
from gym.wrappers import GrayScaleObservation
from stable_baselines3.common.vec_env import VecFrameStack, DummyVecEnv
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3 import PPO
import callback

# Variaveis globais
SAVE_DIR = './save'
LOG_DIR = './logs'
JOGO = 'Alleyway-GameBoy'
STATE_SAVE = 'Level1'
save = callback.TrainAndLoggingCallback(check_freq=50_000, save_path=SAVE_DIR)


# Criando o ambiente do jogo
# Preprocessamento dos frames para passar para a IA
# Escala de cinza
env = DummyVecEnv([lambda: GrayScaleObservation(retro.make(game=JOGO, state=STATE_SAVE), keep_dim=True)])

# Stack nos frames
env = VecFrameStack(env, 4, channels_order='last')

# Criando o modelo
model = PPO('CnnPolicy', env, verbose=1, tensorboard_log=LOG_DIR,
            learning_rate=0.0025, n_steps=4096, gamma=0.99, device='cuda')

# Carregar depois de treinado
model = PPO.load('./save/best_model_1900000.zip', env=env)


# Treinando
# model.learn(total_timesteps=4_000_000, callback=save)


# Fazer ele jogar com o treinamento carregado anteriormente
state = env.reset()
while True:
    action, _ = model.predict(state)
    state, reward, done, info = env.step(action)
    env.render()


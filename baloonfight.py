from PIL import Image, ImageGrab
import cv2
import numpy as np
import os
import pyautogui as gui
import time
import random


class BalloonTripEnvironment:

    def __init__(self):
        self._region = (10, 10, 300, 300)
        self._doneimage = cv2.imread('./opt/bf/gameover.png')
        self.obs = gui.screenshot(region=self._region)
        self.episode_start = time.time()
        self.steps = 0
        self.action_space = ['NOOP', 'z']

    @staticmethod
    def _press_key(key_to_press):
        gui.keyDown(key_to_press)
        gui.keyUp(key_to_press)

    def reset(self):
        keys_to_press = ['h', 'k', 'k', 'enter']    # Combinations to reset and restart
        for key_to_press in keys_to_press:
            self._press_key(key_to_press)
        self.episode_start = time.time()
        self.steps = 0

    def observe_state(self):
        img_obs = gui.screenshot(region=self._region)
        img_obs = cv2.cvtColor(np.array(img_obs), cv2.COLOR_BGR2GRAY)
        # resize = cv2.resize(img_obs, (112, 120), interpolation=cv2.INTER_CUBIC)
        return img_obs

    def close(self):
        pass

    def step(self, action):
        self.steps += 1
        if self.action_space[action] != 0:
            self._press_key(self.action_space[action])
        obs = self.observe_state()
        reward = self.episode_start - time.time()
        done = self.is_game_over()
        info = {'Time': reward, 'Steps': self.steps}
        return obs, reward, bool(done), dict(info)

    def is_game_over(self):
        img = ImageGrab.grab(bbox=self._region)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        res = cv2.matchTemplate(img, self._doneimage, eval('cv2.TM_CCOEFF_NORMED'))
        return (res >= 0.8).any()


def main():
    time.sleep(4)
    env = BalloonTripEnvironment()
    env.reset()
    done = False
    while not done:
        done = env.is_game_over()
        action = random.randrange(2)
        env.step(action)


if __name__ == "__main__":
    main()

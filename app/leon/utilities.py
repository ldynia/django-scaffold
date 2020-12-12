import os
import time

from leon.constants import ASCII_ART


def animate(sequence, delay=0.4):
    os.system('clear')
    for frame in sequence:
        print(f"\r{frame}", flush=True)
        time.sleep(delay)
        os.system('clear')
    print(ASCII_ART) 
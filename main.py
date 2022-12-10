from pygame import mixer
from datetime import datetime
from time import time


def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")


def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 40*60
    exsecs = 30*60
    eyessecs = 45*60

    while True:
        if time() - init_water > watersecs:
            print("Its time to Drink Water 🍹. Enter 'drank' to stop the alarm.")
            musiconloop('water.mp3.wav', 'drank')
            app_icon = "C:/Users/chand/Downloads/Icons.ico.ico",
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes > eyessecs:
            print("Eye exercise time. Enter 'EyDone' to stop the alarm.")
            musiconloop('water.mp3.wav', 'EyDone')
            app_icon = "C:/Users/chand/OneDrive/Desktop/Remind me/icons8-eye-64.png",
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exsecs:
            print("Physical Activity Time. Enter 'ExDone' to stop the alarm.")
            musiconloop('water.mp3.wav', 'ExDone')
            app_icon = "C:/Users/chand/OneDrive/Desktop/Remind me/icons8-cardio-exercises-64.png",
            init_exercise = time()
            log_now("Physical Activity done at")

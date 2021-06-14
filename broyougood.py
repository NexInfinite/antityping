from pynput import keyboard
from playsound import playsound
import time
import threading

total_presses = 0
has_played = False


def on_press(key):
    global total_presses, has_played
    total_presses += 1
    if total_presses >= 10 and not has_played:
        playsound("fart.mp3")
        has_played = True


def reset():
    global total_presses, has_played
    while True:
        time.sleep(1)
        print(f"reset {total_presses}")
        total_presses = 0
        has_played = False


reset = threading.Thread(target=reset)
reset.start()


# Collect events until released
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press)
listener.start()

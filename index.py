from pynput import keyboard
from playsound import playsound
import threading

def play_duck_sound():
    threading.Thread(target=playsound, args=("pato.mp3",), daemon=True).start()

def on_press(key):
    play_duck_sound()
    
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

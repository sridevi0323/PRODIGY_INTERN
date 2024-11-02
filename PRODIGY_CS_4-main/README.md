# Keylogger

Keylogger implementation in Python. It captures keystrokes and logs them into a file. As you mentioned, ethical considerations are crucial, so be sure to have proper permissions before deploying this kind of software.

How the Keylogger Works:
Key Press Logging:
The on_press function captures every key press and writes it to a text file (keylog.txt).
The str(key).replace("'", "") ensures that the key names are logged without extra quotation marks.
Key Release Handling:
The on_release function allows the user to stop the keylogger by pressing the Esc key.
Pynput Library:
This program uses the pynput library to listen to keyboard events.
Install it using:
***pip install pynput***

Log File:
The keys pressed are continuously logged in keylog.txt.



 """
    Function to handle key press events.
    Logs each key press to a text file.

   Parameters:
    - key: the key that was pressed
 """
    
        
  """
    Function to handle key release events.
    Stops the keylogger if the 'Esc' key is pressed.

  Parameters:
    - key: the key that was released
  """

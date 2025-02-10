from socket import *
import os
from datetime import datetime
import queue
import threading
import time


def receive_msg(client,buffer,lock):
    while True:
        msg_client=client.recv(1024).decode()
        if msg_client :
            with lock: # aspetta che il processo empty_buffer sia finito
                buffer.put(msg_client)


def write_file(buffer,fileName):
    '''
    Function used to write all the data inside the buffer 
    and write to the file. After empty the buffer 
    
    Parameters:
    buffer
    fileName
    '''
    # itera finchè il buffer è vuoto
    file=open(fileName,"a")
    while not buffer.empty():
        file.write(buffer.get())
    print("file update!")
    file.close()
    

if __name__ == '__main__':
    s=socket(AF_INET, SOCK_STREAM)
    PORT=50000

    s.bind(("",PORT))

    s.listen(1)

    # foreach host connected -> multithreads

    c,add=s.accept()
    print(add)
        
    name_client_file=f"{add[0]}.txt"
    f=open(name_client_file,"a")
    current_date_time=datetime.now()
    print(f"SESSION WITH {add} START {current_date_time}")
    f.write(f"\n\n---------SESSION START {current_date_time}---------\n")
    f.close()
    
    

    client_buffer=queue.Queue()
    
    # per la gestione del buffer 
    lock=threading.Lock()
    
    try :
        msg_receiver=threading.Thread(target=receive_msg,args=(c,client_buffer,lock))
        msg_receiver.daemon=True
        msg_receiver.start()
        while True: # finchè la connessione continua , il file si aggiorna ogni 3 secondi
            time.sleep(1)
            if not client_buffer.empty():
                
                with lock:
                    write_file(client_buffer,name_client_file)
    except:   
        # risolvere i problemi inerenti alla fine della connessione 
        # cntrl c stop file update
        if not client_buffer.empty() : write_file(client_buffer,name_client_file)
        current_date_time=datetime.now()
        print(f"SESSION WITH {add} FINISHED {current_date_time}")

        
    # Bug list
    # il server non riesce a verificare quando il client è
    # connesso o meno , keep alive(?)    
        
    # Todo list
    # criptare la connessione tcp
    # gestire tutti i casi della tastiera
    # gestire più client in contemporanea
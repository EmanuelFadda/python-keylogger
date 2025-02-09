from socket import *
import os
from datetime import datetime

s=socket(AF_INET, SOCK_STREAM)
PORT=50000

s.bind(("",PORT))

s.listen(1)



# foreach host connected -> multithreads

c,add=s.accept()
print(add)
    

f=open(f"{add[0]}.txt","a")
current_date_time=datetime.now()
print(f"SESSION WITH {add} START {current_date_time}")
f.write(f"\n\n---------SESSION START {current_date_time}---------\n")

is_conntected=True

while is_conntected:
    try:
        msg_client=c.recv(1024).decode()
        f.write(msg_client)
    except:
        f.close()
        print("file chiuso")
        current_date_time=datetime.now()
        print(f"SESSION WITH {add} FINISHED {current_date_time}")
        is_conntected=False

    
    
    
# Bug list
# il server non riesce a verificare quando il client è
# connesso o meno , keep alive(?)    
    
# Todo list
# criptare la connessione tcp
# gestire tutti i casi della tastiera
# gestire più client in contemporanea
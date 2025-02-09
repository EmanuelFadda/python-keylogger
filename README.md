# python-keylogger

## What is a keylogger? :tea:
<p>A keylogger is a software capable of monitoring every action happening in your keyboard, pressing, release etc.. and register these action in your computer (using a file) or can be shared directly with the attacker (for example opening a connection between your machine and the attacker machine). This type of malware is used by attackers to steal your information, every word pressed can be useful to give them access of your online research,passwords,email,cell numbers and other more.</p>  

## Description of *python-keylogger* :alien:
<p>
This project is used to simulate a keylogger attack in your local network. This can be useful to learn how keylogger's attacks works.
</p>


python-keylogger's attack have two actors: <br>
- the victim's machine (*KeyLoggerClient/client.py*) 
- the attacker's machine (*KeyLoggerServer/server.py*)

<br>

For obivious reason, this attack don't rappresent the reality, we have to create the scenario:
1. the server is active only to test the attack 
2. we're starting the client manually, in real life we don't know even if the keylogger is inside in our machine 
3. clients and server runs in the same machine (in fact the *IP* variable of the client is *localhost*)

<br> 

When *client.py* process starts, it creates a TCP connection with the server and starts to stream every key you press. The server when the TCP connection with the victim starts, if the ip of the victim is new (assuming by ip address), *server.py* creates a text file used to put all the data received. 

<br>

> *server.py* at the moment (v1.0) can handle a single tcp connection, and the connection is not encrypted.    

### Get started! 💥

Run the server first:
```
cd KeyLoggerServer
python server.py
```
..or directly
```
python KeyLoggerServer/server.py
```
Then run the client:

```
cd KeyLoggerClient
python client.py
```
..or directly
```
python KeyLoggerClient/client.py
```

Have fun! :smirk:

## How to prevents this type of attack :alien:
...

### :exclamation::exclamation::exclamation: WARNING :exclamation::exclamation::exclamation:
**Don't use this project to steal other's information without their consent. Use it only for educational porpuses!**

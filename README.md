# python-keylogger

## What is a keylogger? :tea:
A keylogger is a type of software capable of monitoring every action happening on your keyboard, presses, releases etc.. and records these actions on your computer (using a file) or can be shared directly with the attacker (for example opening a connection between your machine and the attacker machine). This type of malware is used by attackers to steal your information. Every word pressed can be useful to give them access to your online searches,passwords, your email and more.

## Description of *python-keylogger* :alien:
This project is used to simulate a keylogger attack in your local network. This can be useful to learn how keylogger attacks work.


The python-keylogger attack has two actors: <br>
- The victim's machine (*KeyLoggerClient/client.py*) 
- The attacker's machine (*KeyLoggerServer/server.py*)

<br>

For obvious reasons, this attack doesn't represent a real-world scenario:
1. The server is active only to test the attack 
2. We're starting the client manually, in real life we don't know even if the keylogger is inside our machine 
3. The clients and server run on the same machine (in fact the client's *IP* variable is set to "*localhost*")

<br> 

When the *client.py* process starts, it creates a TCP connection with the server and begins streaming every key you press. When the victim's TCP connection starts, if the IP of the victim is new (based on the ip address), *server.py* creates a text file to store all the data received. 

<br>

> *server.py* (v1.0) currently supports a single TCP connection and doesn't use encryption.    

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

## How to prevent this type of attack :alien:
### If you haven't been attacked before, please:

There are different way to install a keylogger in your device without your consent , so...  

- Don't download any file from unknown sources (like phishing emails, cracked software... etc)
- Use an antivirus
- Keep your devices protected with a strong password
- Update with the last version all your softwares and your operating system 

### Checking if *python-keylogger* was installed and is running... 

Actually (v1.0), *python-keylogger* doesn't encrypt the TCP connection, hide itself or restart when someone kills it. Assuming you didn't know if it's running or not, there's simple action you can take to keep you safe:

- Check the TCP connection using programs like Wireshark
- Check suspicious process on Task Manager 

### :exclamation::exclamation::exclamation: WARNING :exclamation::exclamation::exclamation:
**Don't use this project to steal other's information without their consent. Use it only for educational purposes!**

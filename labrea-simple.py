import sys
import socket
import select

def start (ignorePorts):

    host = ''
    maxCon = 5
    
    sockets = []
    
    for port in range(1000, 65535):
        if not port in ignorePorts:
            print("creating socket for port:", port)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # catch errors where port is already taken
            try:
                s.bind((host, port))
            except:
                continue
            s.listen(maxCon)
            sockets.append(s)

    run = True
    
    while run:
        readySockets,_,_ = select.select(sockets, [], [], 1)

        for s in readySockets:
            #data, addr = s.recvfrom(64)
            client,addr = s.accept()

    print("Quitting")

    for s in sockets:
        s.close()

    print("All sockets closed")


ignorePorts = []
for port in sys.argv[1:]:
    ignorePorts.append(int(port))

start(ignorePorts)

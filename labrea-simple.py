import sys
import socket
import select
import asyncio

async def listen_thread(reader, writer):
    while True:
        data = await reader.read(64)

async def start_servers(host, port):
    try:
        server = await asyncio.start_server(listen_thread, host, port)
    except:
        return
    await server.serve_forever()

def start (ignorePorts):

    host = ''
    
    loop = asyncio.get_event_loop()
    
    try:
        for port in range(1000, 65535):
            if not port in ignorePorts:
                print("creating socket for port:", port)
                #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # catch errors where port is already taken
                loop.create_task(start_servers(host, port))
        loop.run_forever()
    except Exception as exc:
        print(exc)
        

    print("Quitting")


ignorePorts = []
for port in sys.argv[1:]:
    ignorePorts.append(int(port))

start(ignorePorts)

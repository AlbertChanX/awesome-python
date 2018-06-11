import asyncio
import websockets


async def send(websocket, path):
    while True:
        if not websocket.open:
            return
        name = await websocket.recv()
        await websocket.send(f"{name}")
        print(f"{name}")
        
if __name__ == '__main__':
        # main()
    start_server = websockets.serve(send, 'localhost', 9999)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

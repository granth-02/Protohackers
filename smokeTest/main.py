import asyncio


HOST = "127.0.0.1"
PORT = 12345

async def echo_echo(reader, writer):
    client_addr = writer.get_extra_info("peername")
    print(f"Connect to {client_addr}")
    try:
        while True:
            msg = await reader.read(1024)
            if not msg:
                break

            writer.write(msg)
            await writer.drain()

    except Exception as e:
        print(e)
    finally:
        writer.close()
        await writer.wait_closed()
        print("Connection CLosed")

async def main():
    s = await asyncio.start_server(
        echo_echo, HOST, PORT
    )

    print(f"Serving on {HOST}:{PORT}")

    async with s:
        await s.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())


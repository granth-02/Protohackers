import asyncio


HOST = "127.0.0.1"
PORT = 12345

async def client(reader, writer):
    addr = writer.get_extra_info("peername")
    print(f"Connect to {addr}")
    try:
        while True:
            data = await reader.readline()
            if not data:
                break

            writer.write(data)
            await writer.drain()

    except Exception as e:
        print(e)
    finally:
        writer.close()
        await writer.wait_closed()
        print("Connection CLosed")

async def main():
    s = await asyncio.start_server(
        client, HOST, PORT
    )

    print(f"Serving on {HOST}:{PORT}")

    async with s:
        await s.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())


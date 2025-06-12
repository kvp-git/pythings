import asyncio
from bleak import BleakScanner

async def main():
    print('scanning for btle devices...')
    devices = await BleakScanner.discover()
    for device in devices:
        print(device)
    print('done.')

try:
    asyncio.run(main())
except Exception as e:
    print('Error: ' + str(e))

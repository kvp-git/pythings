# simple circuitcube runner by KVP in 2025
#
# CIRCUIT_CUBE_SERVICE_UUID = "6e400001-b5a3-f393-e0a9-e50e24dcca9e"
# CIRCUIT_CUBE_TX_CHRACTERISITCS_UUID = "6e400002-b5a3-f393-e0a9-e50e24dcca9e"
# CIRCUIT_CUBE_RX_CHRACTERISITCS_UUID = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"
# 
# ascii protocol:
# 
# output control:
#  +000a+000b+000c
#  +000a-255b+255c
#  +127a+042b-001c
# 
# battery level:
#  b -> 3.82

import asyncio
import time
from bleak import BleakClient

async def main():
    # circuit cube bluetooth low energy address
    ble_address = 'FC:58:FA:CF:62:70'
    # control characteristics
    characteristic_uuid_rx = '6e400003-b5a3-f393-e0a9-e50e24dcca9e'
    characteristic_uuid_tx = '6e400002-b5a3-f393-e0a9-e50e24dcca9e'
    print('connecting: ' + ble_address)
    async with BleakClient(ble_address) as client:
        print('Connected to BLE device: ' + str(client.is_connected))
        # get battery status
        data = b'b'
        await client.write_gatt_char(characteristic_uuid_tx, data)
        data = await client.read_gatt_char(characteristic_uuid_rx)
        print(data)
        # command
        data = b'+000a+000b+000c'
        print(data)
        await client.write_gatt_char(characteristic_uuid_tx, data)
        # wait
        time.sleep(0.5)
        # command
        data = b'+255a+128b-128c'
        print(data)
        await client.write_gatt_char(characteristic_uuid_tx, data)
        # wait
        time.sleep(2)
        # command
        data = b'-127a-128b+255c'
        print(data)
        await client.write_gatt_char(characteristic_uuid_tx, data)
        # wait
        time.sleep(4.5)
        # stop
        data = b'+000a+000b-000c'
        print(data)
        await client.write_gatt_char(characteristic_uuid_tx, data)
        print('done.');

try:
    asyncio.run(main())
except Exception as e:
    print('Error: ' + str(e))

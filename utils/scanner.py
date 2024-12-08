import asyncio
from bleak import BleakScanner, BleakClient
from rich.console import Console
from rich.table import Table

async def scan_devices():
    scanner = BleakScanner()
    await scanner.start()
    await asyncio.sleep(5)  # Scan for 5 seconds
    await scanner.stop()
    devices = scanner.discovered_devices
    return devices

def display_devices(devices):
    console = Console()
    table = Table(title="Bluetooth Devices")
    table.add_column("No.", justify="center", style="cyan")
    table.add_column("Device Name", style="magenta")
    table.add_column("MAC Address", style="green")

    for i, device in enumerate(devices, start=1):
        device_name = device.name or "Unknown"  # Handle devices with no name
        mac_address = device.address
        table.add_row(str(i), device_name, mac_address)

    console.print(table)

def select_option(devices):
    selection = input("Select an option (enter the number): ")
    try:
        index = int(selection) - 1
        if index >= 0 and index < len(devices):
            return devices[index].address
        else:
            raise ValueError()
    except ValueError:
        print("Invalid option. Please try again.")
        return select_option(devices)

async def connect_device(mac_address):
    try:
        async with BleakClient(mac_address) as client:
            if client.is_connected:
                print(f"Connected to {mac_address}")
            else:
                print("Failed to connect.")
    except Exception as e:
        print(f"Error connecting to {mac_address}: {e}")

async def main():
    # Starting Bluetooth Scan
    devices = await scan_devices()
    display_devices(devices)
    selected_device = select_option(devices)
    mac_address = selected_device
    return mac_address

if __name__ == "__main__":
    asyncio.run(main())
import asyncio
from bleak import BleakScanner, BleakClient
from rich.console import Console
from rich.table import Table

async def scan_devices():
    scanner = BleakScanner()
    await scanner.start()
    await asyncio.sleep(5)  # Scan for 5 seconds
    await scanner.stop()
    devices = scanner.discovered_devices
    return devices

def display_devices(devices):
    console = Console()
    table = Table(title="Bluetooth Devices")
    table.add_column("No.", justify="center", style="cyan")
    table.add_column("Device Name", style="magenta")
    table.add_column("MAC Address", style="green")

    for i, device in enumerate(devices, start=1):
        device_name = device.name or "Unknown"  # Handle devices with no name
        mac_address = device.address
        table.add_row(str(i), device_name, mac_address)

    console.print(table)

def select_option(devices):
    selection = input("Select an option (enter the number): ")
    try:
        index = int(selection) - 1
        if index >= 0 and index < len(devices):
            return devices[index].address
        else:
            raise ValueError()
    except ValueError:
        print("Invalid option. Please try again.")
        return select_option(devices)

async def connect_device(mac_address):
    try:
        async with BleakClient(mac_address) as client:
            if client.is_connected:
                print(f"Connected to {mac_address}")
            else:
                print("Failed to connect.")
    except Exception as e:
        print(f"Error connecting to {mac_address}: {e}")

async def main():
    # Starting Bluetooth Scan
    devices = await scan_devices()
    display_devices(devices)
    selected_device = select_option(devices)
    mac_address = selected_device
    return mac_address

if __name__ == "__main__":
    asyncio.run(main())

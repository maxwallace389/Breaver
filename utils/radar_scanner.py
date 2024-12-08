import asyncio
from bleak import BleakScanner
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

class RadarScanner:
    def __init__(self):
        self.devices = []
        self.figure, self.ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
        self.ax.set_ylim(0, 10)  # Set the range of the radar
        self.ax.set_title("Radar Scanner", color='green', fontsize=20, fontweight='bold')
        self.ax.grid(color='white', linestyle='--', linewidth=0.5)
        self.ax.set_facecolor('black')  # Background color

    async def scan_devices(self):
        scanner = BleakScanner()
        await scanner.start()
        await asyncio.sleep(5)  # Scan for 5 seconds
        await scanner.stop()
        self.devices = scanner.discovered_devices

    def update_radar(self, frame):
        self.ax.cla()  # Clear the previous radar
        self.ax.set_ylim(0, 10)  # Set the range of the radar
        self.ax.set_title("Radar Scanner", color='green', fontsize=20, fontweight='bold')
        self.ax.grid(color='white', linestyle='--', linewidth=0.5)
        self.ax.set_facecolor('black')  # Background color

        # Update the radar with device positions
        if self.devices:
            for device in self.devices:
                # Example: Place device at a random angle and distance (for demo purposes)
                angle = np.random.uniform(0, 2 * np.pi)
                distance = np.random.uniform(1, 10)  # Random distance
                self.ax.plot(angle, distance, 'ro', markersize=8)  # 'ro' = red circle

    async def run(self):
        while True:
            await self.scan_devices()
            self.update_radar()
            plt.pause(5)  # Pause to allow the plot to update
            self.ax.clear()  # Clear the axes for the next update

    def start_radar(self):
        ani = FuncAnimation(self.figure, self.update_radar, interval=1000)
        plt.show()

if __name__ == "__main__":
    radar = RadarScanner()
    radar.start_radar()

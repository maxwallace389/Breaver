
# Bluetooth Radar Scanner Tool

## About

**Breaver** is a powerful command-line interface (CLI) tool designed for Bluetooth device hacking. It allows users to scan for nearby Bluetooth devices, eject unwanted connections, and visualize detected devices in real-time using a radar-like interface. With a hacker-themed GUI, Breaver aims to provide both functionality and an engaging user experience.

## Features

- **Bluetooth Scanning**: Detects nearby Bluetooth devices within range.
- **Radar Visualization**: Displays devices on a radar-like interface with real-time updates.
- **Device Kicking**: Eject unwanted Bluetooth devices from your connection list.
- **Real-time Updates**: Continuously refresh the radar to track device movement and proximity.
- **Multi-Platform Support**: Designed to run on Windows, macOS, and Linux.

## Installation

### Prerequisites

- Python 3.7 or higher
- Required Python libraries (listed in `requirements.txt`)

### Steps to Install

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/BluetoothRadarScanner.git
   cd BluetoothRadarScanner
   ```

2. **Create a Virtual Environment (optional but recommended)**:
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS and Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Tool**:
   To start the application, run:
   ```bash
   # On Windows
   python Breaver.py

   # On macOS and Linux
   python3 Breaver.py
   ```

2. **Interact with the Menu**:
   Follow the on-screen prompts to scan for devices, kick unwanted devices, or connect to a device. The radar will visually display nearby devices in real-time.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Bleak](https://pypi.org/project/bleak/) for Bluetooth communication.
- [Matplotlib](https://matplotlib.org/) for visualization.
- [Rich](https://rich.readthedocs.io/en/stable/) for enhancing terminal output.
- Special thanks to the open-source community and contributors from various Bluetooth hacking tools, including the foundational ideas from the [Bluestrike project](https://github.com/StealthIQ/Bluestrike.git).

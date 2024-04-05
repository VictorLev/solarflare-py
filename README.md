# SolarFlarePy - 🔆 Light Therapy Lamp 🔆

## Overview
This project is a MicroPython-based light therapy lamp designed to mimic natural sunlight, helping to improve mood, sleep patterns, and overall mental health. Utilizing LEDs that can adjust in color temperature and brightness, this lamp simulates different times of the day, from the soft glow of sunrise to the bright light of noon. Ideal for individuals suffering from Seasonal Affective Disorder (SAD) or anyone looking to regulate their circadian rhythms, this lamp is a portable, energy-efficient solution to light therapy.

## Features
- **Adjustable Color Temperature:** Mimics various times of the day to match natural light.
- **Programmable Schedule:** Automates light intensity, gradually increasing or decreasing to simulate sunrise and sunset.
- **User Interface:** Offers manual controls for customization through physical buttons, touchscreen, or a web interface.
- **Energy Efficient:** Utilizes LEDs for long-lasting, cost-effective operation.

## Hardware Requirements
- Microcontroller compatible with MicroPython (e.g., ESP32, Pyboard)
- LED panel or strips capable of producing a broad spectrum of light
- Power supply suitable for the microcontroller and LEDs
- Optional: Touchscreen or buttons for manual control

## Software Requirements
- MicroPython firmware for your microcontroller
- Additional libraries may be required for specific hardware components (e.g., for LED control or networking)

## Installation
1. **Prepare the Microcontroller:**
   - Flash the MicroPython firmware onto your microcontroller following the [official MicroPython documentation](https://docs.micropython.org/en/latest/).

2. **Connect the Hardware:**
   - Attach the LED panel/strips and any user interface components to the microcontroller according to the wiring diagram included in the `/diagrams` folder.

3. **Deploy the Software:**
   - Clone this repository to your local machine.
   - Modify the configuration file (`config.json`) with your WiFi credentials and other settings.
   - Upload the scripts to the microcontroller using a tool like `ampy`, `rshell`, or through the WebREPL.

## Usage
- **Manual Control:** Use the physical buttons or touchscreen to turn on/off, adjust brightness, and change color temperature.
- **Automated Schedule:** The lamp follows a pre-programmed schedule to simulate natural daylight cycles, customizable through the web interface.

## Contributing
We welcome contributions to improve the MicroPython Light Therapy Lamp! Please consider the following ways to contribute:
- **Reporting Bugs:** Open an issue detailing the bug and steps to reproduce it.
- **Feature Suggestions:** Have an idea to improve the lamp? Submit it as an issue for discussion.
- **Code Contributions:** Submit a pull request with your proposed changes. Please ensure your code follows the project's coding conventions.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thanks to the MicroPython community for providing the resources and support to make this project possible.
- Special thanks to [contributors' names] for their invaluable contributions.

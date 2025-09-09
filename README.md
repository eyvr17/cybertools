# CyberControl Panel

CyberControl Panel is an interactive Python-based tool for Windows systems. It is designed for educational and academic use in cybersecurity training. The tool offers a simple interface and allows users to explore key concepts such as network scanning, password analysis, port monitoring, and system interaction using a command-line menu.

---

## Overview of Features

| Module                    | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| Keylogger (Demo)          | Simulates the activation of a keylogger for training purposes.              |
| Network Scanner           | Identifies active hosts in the local network subnet using socket scanning. |
| Password Strength Checker | Evaluates password strength based on character patterns and length.         |
| Screenshot Capturer       | Captures the current screen and stores the image in the system temp folder. |
| Port Monitor              | Lists open listening ports using system-level inspection.                   |
| Auto-Startup (Windows)    | Optionally adds the script to Windows Registry to run at system startup.    |
| Interactive Menu          | CLI interface navigable via keyboard arrows and Enter key.                  |

---

## Requirements

This tool installs the following libraries automatically if not found:

- psutil
- pyautogui
- tabulate
- colorama
- keyboard

Python 3.6 or higher is recommended.

---

## Installation and Execution

Clone the repository and run the script:

```bash
git clone https://github.com/eyvr17/cybertools.git
cd cybertools
python cybertools.py
```

Once started, navigate through the menu using:

- ↑ and ↓ to select options  
- ENTER to execute  
- CTRL + C to stop certain tools like the keylogger simulation

Note: Files such as screenshots and keylogs are saved in your system's temporary directory.

---

## Sample Output

### Menu Interface

```
➤ Keylogger (Active)
  Network Scanner
  Password Strength Checker
  Screenshot Capturer
  Port Monitor
  Exit
```

### Network Scan Result

```
+---------------+-----------------+------------+
| IP            | Hostname        | Status     |
+---------------+-----------------+------------+
| 192.168.1.10  | my-device.local | Active     |
+---------------+-----------------+------------+
```

---

## File Structure

```
cybertools/
├── cybertools.py         # Main script
├── README.md             # Documentation file
└── docs/
    └── assets/           # Place images or GIFs for documentation
```

---

## Development Roadmap

Planned improvements include:

- Implementation of a functional keylogger module  
- Webcam screenshot capture (with user permission)  
- Remote access dashboard using Flask  
- Encryption of logs and secure reporting  
- External API integration (e.g., VirusTotal, Shodan)  

---

## Legal Notice

This project is strictly for educational and ethical research use.  
Users are responsible for ensuring proper authorization before using any of the included tools on third-party systems.

---

## Author

- Maintainer: [@eyvr17](https://github.com/eyvr17)  
- Contact: eyvr17@proton.me

---

## Citation

If you use this tool in an academic setting, please cite the repository or mention the author in your materials.

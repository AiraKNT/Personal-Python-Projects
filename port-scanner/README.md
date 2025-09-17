# 🔍 Port Scanner in Python

This is a basic **TCP port scanner** written in Python. It allows users to input a target IP address and scans a range of ports (from 20 to 1024) to check whether each port is **open** or **closed**.

## 📌 Features

- Validates user input to ensure a correct IP address format.
- Scans ports in the range 20–1024.
- Uses socket connections to determine port status.
- Displays results in the terminal.

## 🧠 How It Works

1. Prompts the user to enter a valid IP address.
2. Iterates through a predefined range of ports.
3. Attempts to connect to each port using TCP.
4. Reports whether each port is open or closed.

## 🛠️ Requirements

- Python 3.x
- No external libraries required (uses built-in `socket` and `ipaddress` modules)

## 🚀 Usage

Run the script in your terminal:

```bash
python port_scanner.py

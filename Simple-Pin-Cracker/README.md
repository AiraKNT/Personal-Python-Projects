# Brute-Force PIN Cracker (Simulation)

This Python script simulates a brute-force attack on a randomly generated 4-digit PIN code. It demonstrates how quickly a computer can iterate through all possible combinations to find the correct PIN.

## 🔍 What It Does

- Generates a random 4-digit PIN (e.g., "0423").
- Attempts every possible 4-digit combination from "0000" to "9999".
- Stops when the correct PIN is found.
- Displays:
  - The found PIN
  - Number of attempts it took
  - Time taken to find the PIN

## 🧠 How It Works

- Uses `random.randint()` to generate a PIN between 0 and 9999.
- Formats the PIN using `.zfill(4)` to ensure it's always 4 digits.
- Uses a `while` loop to simulate brute-force guessing.
- Measures execution time using the `time` module.

## ▶️ How to Run

1. Make sure you have Python 3 installed.
2. Save the script as `brute_force_pin_cracker.py`.
3. Open a terminal or command prompt.
4. Run the script:

```bash
python brute_force_pin_cracker.py

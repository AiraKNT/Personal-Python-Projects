#Objective:
#Simulate a brute-force attack on a 4-digit PIN code using Python.

#Instructions:
#   The program should generate a random 4-digit PIN (e.g., "5732").
#   Then, it should simulate a brute-force attack by trying every possible 4-digit combination from 0000 to 9999.
#   When it finds the correct PIN, it should:
#   Print the number of attempts it took.
#   Show the correct PIN.
#   Optionally, show how long it took (bonus).

#Concepts You'll Practice:
#   random.randint()
#   str.zfill() to format numbers like 0001, 0002, etc.
#   for loops
#   Basic logic and comparison
#   (Optional) time module to measure duration

import random
import time

PIN = str(random.randint(0, 9999)).zfill(4)
Counter = int(0)
Start_Time = time.time()

while True:
    
    if str(Counter).zfill(4) == PIN:
        print(f"PIN found: {PIN}")
        print("Number of attempts:", str(Counter + 1))
        End_Time = time.time()
        print("Time taken:", round(End_Time - Start_Time, 10), "seconds")
        break

    else:
        Counter += 1
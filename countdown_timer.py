import time

try:
    my_time = int(input("Enter the time in seconds: "))
    if my_time < 0:
        raise ValueError("Time cannot be negative.")
except ValueError as e:
    print(f"Invalid input: {e}")
    exit(1)

for remaining_time in range(my_time, 0, -1):
    hours, remainder = divmod(remaining_time, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"\r{hours:02}:{minutes:02}:{seconds:02}", end="")
    time.sleep(1)

print("\nTIME'S UP!")

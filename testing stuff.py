import time

def count_up_to(desired_amount):
    current_number = 0
    while current_number <= desired_amount:
        print(current_number, end='\r')
        current_number += 1
        time.sleep(0.05)  # Adjust the delay to control the speed

# Example: counting up to 100
count_up_to(100)
print("\nDone!")
import time

# Try importing winsound (works only on Windows)
try:
    import winsound
    windows = True
except ImportError:
    windows = False

def alarm_clock():
    alarm_time = input("Enter the alarm time (HH:MM:SS format): ").strip()
    print(f"Alarm set for {alarm_time}...")
    while True:
        current_time = time.strftime("%H:%M:%S")
        print("Current Time: " + current_time, end="\r")
        if current_time == alarm_time:
            print("\nAlarm! Time to wake up!")
            if windows:
                # Beep sound for Windows
                winsound.Beep(1000, 2000)
            else:
                # Fallback for Linux/Mac
                print("\a")  
            break
        time.sleep(1)

if __name__ == "__main__":
    alarm_clock()

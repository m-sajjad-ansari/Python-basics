import time
import datetime

def main():
    print("Set time at which you wanted the alarm to ring.")
    while True:
        try:
            hours = int(input("Enter the hour (1-24): "))
            minutes = int(input("Enter the minute (1-60): "))
            if (hours > 0) & (hours < 25) & (minutes >= 0) & (minutes < 61):
                break
            elif (hours < 0) | (hours > 25):
                print("Out of range hours!")
            else:
                print("Out of range minutes!")
        except ValueError:
            print("Invalid input!")

    print(f"Your clock will ring at {hours:02}:{minutes:02}:00")
    time.sleep(2)
    is_running=True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)  # Example output: 14:30:45
        time.sleep(1)
        current_hours=int(datetime.datetime.now().strftime("%H"))
        current_minutes=int(datetime.datetime.now().strftime("%M"))
        if current_hours==hours and current_minutes==minutes:
            print("Alarm Ringing...")
            break


if __name__ == "__main__":
    main()

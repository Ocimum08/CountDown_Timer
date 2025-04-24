import time

def countdown_timer(seconds):
    print(f"⏳ Countdown started for {seconds} seconds:")
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")  # Print on same line
        time.sleep(1)
        seconds -= 1
    print("⏰ Time's up!")

def main():
    try:
        total_seconds = int(input("Enter time in seconds: "))
        countdown_timer(total_seconds)
    except ValueError:
        print("Please enter a valid number!")

main()

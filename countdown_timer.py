import time

def countdown_timer(seconds):
    while seconds >= 0:
        mins, secs = divmod(seconds, 60)
        timeformat = "{:02d}:{:02d}".format(mins, secs)
        print(f"Time left: {timeformat}", end='\r')
        time.sleep(1)
        seconds -= 1

    print("\nTime's up!")

if __name__ == "__main__":
    try:
        user_time = int(input("Enter countdown time in seconds: "))
        countdown_timer(user_time)
    except ValueError:
        print("Please enter a valid number of seconds.")
#Project 6: countdown Timer in Python
#Description: This is a count down timer that takes the time input from the user in seconds and then displays it into minutes:second format

import time
def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60) # minutes and seconds will be calculated
        time_format = '{:02d}:{:02d}'.format(mins, secs)  # MM:SS format  
        print(time_format, end='\r')
        time.sleep(1) # delay
print("00:00 \n Time's Up!")

#user input for time
total_seconds = int(input("Enter time in second for countdown"))
countdown_timer(total_seconds)

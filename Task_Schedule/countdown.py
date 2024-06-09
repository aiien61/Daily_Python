import time, subprocess

timeleft = 5
while timeleft > 0:
    print(timeleft, end='')
    time.sleep(1)
    timeleft -= 1

# At the end of the countdown, play a sound file.
subprocess.Popen(['open', 'alarm.wav'])
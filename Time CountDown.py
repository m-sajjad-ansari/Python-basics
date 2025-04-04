import time
import winsound
n=int(input("Total time in seconds : "))
for i in range(n,0,-1):
    seconds=i%60
    minutes=int(i/60)%60
    hours=int(i/3600)%60
    if i==n:
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        winsound.Beep(1000,500)
    else:
        winsound.Beep(1000, 500)
        time.sleep(1)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
time.sleep(1)
print("Time's up!")
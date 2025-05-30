import time 

t = input("Enter the time in seconds: ")

if t.isdigit():
    t=int(t)
else:
    print("Invalid input. Try again.")
    quit()

while t:
    minutes, seconds = divmod(t,60)
    timer = "{:02d}:{:02d}".format(minutes,seconds)
    time.sleep(1)
    print(timer, end='\r') 
    t = t - 1 

print("Time's up!")
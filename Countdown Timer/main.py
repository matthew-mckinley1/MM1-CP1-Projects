#Matthew McKinley Countdown Timer

import time 

# input time in seconds 
t = input("Enter the time in seconds: ") 
  
def countdown(t): 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = "{:02d}:{:02d}".format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
      
    print("TIMER DONE TIMER DONE BEEP BEEP BEEP BEEP BEEP") 
  

countdown(int(t)) 
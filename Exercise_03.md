Create a log file generator that appends time-stamped logs to a file.

```
import time
from datetime import datetime

def write_log(message,file_name = "log_file.txt"):
    timestamp = datetime.now().strftime("%y-%m-%d %H: %M: %S")
    log_message = f"[{timestamp}] {message}\n"
    with open(file_name, "a") as file :
        file.write(log_message)

if __name__ == "__main__" :
    for i in range(5):
        write_log(f"sample log message number {i+1}")
        print(f"Log {i+1} written.")
        time.sleep(2)
```

step 1 : imported the  time module for addinf a delay

step 2 : Used to get the time and date

step 3 : deffining the fuction as write_log with a varable (message and file name )

step 4 : the timestamp variable stores the current date and time and stores in the timestamp variable

step 5 : the log message variable stores the timestamp with a message

step 6 : ```with open(file_name, "a") as file :
        file.write(log_message)``` the file is opened if alreadey there it will execute inside it if not it will generate a new log file and write the log message inside it.
step 7 : ``` if __name__ = __main__ ``` is used to run the current code to execute without and existing module

step 8 : next it enters it to the log file and append the time stamp with log message 5 times

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
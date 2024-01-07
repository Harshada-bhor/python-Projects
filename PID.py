# To Find a PID (Process Id) and PPID (Parent Process Id) of Current Process.
# it change to every time.
import os

def main():
    print("PID of current process is : ",os.getpid())
    print("PID of parent process is : ",os.getppid())

if __name__ == "__main__":
    main()

    
    

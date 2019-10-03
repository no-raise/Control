from sys import argv
import os
import psutil

def isRunning(process):
    for proc in psutil.process_iter(attrs=['name', 'exe', 'cmdline']):
        
        if proc.info['name'] == process:
            return True
    
    return False
        
    
if __name__ == "__main__":
    process = argv[1] + '.exe'
    print(process)
    print(isRunning(process))


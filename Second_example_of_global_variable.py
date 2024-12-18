system_status = "Offline"

def start_system():
    global system_status    # Access the global variable
    system_status = "Online"
    print("System Started.")
    
def stop_system():
    global system_status    # Access the global variable
    system_status = "offline"
    print("System Stopped.")
    
def check_system_status():
    # Access the global variable without modification
    print(f"The system is currently: {system_status}")
    
# Using the global variable
check_system_status()       # Output: The system is currently: offline
start_system()              # Output: System Started.
check_system_status()       # Output: The system is currently: online
stop_system()               # Output: System Stopped.
check_system_status()       # Output: The system is currently: offline
import time

def stopwatch():
    print("Simple Stopwatch")
    print("Press 's' to start/stop the stopwatch.")
    print("Press 'r' to reset the stopwatch.")
    print("Press 'q' to quit the stopwatch.")

    running = False  # Flag to check if the stopwatch is running
    start_time = 0
    elapsed_time = 0

    while True:
        command = input("Enter command: ").lower()
        
        if command == 's':  # Start or stop the stopwatch
            if not running:
                start_time = time.time() - elapsed_time  # Resume from last time
                running = True
                print("Stopwatch started.")
            else:
                elapsed_time = time.time() - start_time  # Update elapsed time
                running = False
                print(f"Stopwatch stopped. Elapsed time: {elapsed_time:.2f} seconds.")
        
        elif command == 'r':  # Reset the stopwatch
            elapsed_time = 0
            if running:
                start_time = time.time()  # Reset the start time to now
            print("Stopwatch reset.")
        
        elif command == 'q':  # Quit the stopwatch
            if running:
                elapsed_time = time.time() - start_time
                print(f"Final time: {elapsed_time:.2f} seconds.")
            print("Exiting stopwatch.")
            break
        
        # Display the current time if stopwatch is running
        if running:
            elapsed_time = time.time() - start_time
            print(f"Current time: {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
    stopwatch()

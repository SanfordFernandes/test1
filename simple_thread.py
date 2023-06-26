import concurrent.futures

# Define a thread function


def print_numbers(num):
    for i in range(1, 11):
        print(f"Thread {num}: {i}")


# Create a ThreadPoolExecutor with maximum 2 threads
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    # Submit tasks to the thread pool
    task1 = executor.submit(print_numbers, 1)
    task2 = executor.submit(print_numbers, 2)

    # Wait for the tasks to complete
    task1.result()
    task2.result()

print("Threads have finished executing. TEST")

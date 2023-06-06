import concurrent.futures


def my_library_function(data, executor=None):
    # Define the worker function
    def worker_function(args):
        # Perform some computation or task
        # ...

        # Return the result
        return "result"

    # Create a default executor if none is provided
    if executor is None:
        executor = concurrent.futures.ThreadPoolExecutor()

    try:
        # Submit the tasks to the executor
        futures = [executor.submit(worker_function, args) for args in data]

        # Wait for the results
        results = [future.result() for future in concurrent.futures.as_completed(futures)]

        return results
    finally:
        # Shut down the executor (if created within the function)
        if executor is not None:
            executor.shutdown()

# Python - Exceptions

# Objectives

## What’s the difference between errors and exceptions?
## What are exceptions and how to use them?
## When do we need to use exceptions?
## How to correctly handle an exception?
## What’s the purpose of catching exceptions?
## How to raise a builtin exception?
## When do we need to implement a clean-up action after an exception?

1. **What’s the difference between errors and exceptions?**
   - **Error**: An error is a broad term that encapsulates any unexpected situation or anomalous condition in a program or system. Errors might be due to external reasons, like network issues, or internal ones like logic flaws.
   - **Exception**: An exception is a specific type of error that arises during the execution of a program. In many programming languages, exceptions are objects that represent these error conditions. They can often be "caught" and "handled" to prevent program termination.

2. **What are exceptions and how to use them?**
   - As mentioned, exceptions represent error conditions. In many programming languages like Python, Java, or C#, you use try-catch (or similar) blocks to handle them. Here's a simple example in Python:
     ```python
     try:
         result = 10 / 0
     except ZeroDivisionError:
         print("Cannot divide by zero!")
     ```

3. **When do we need to use exceptions?**
   - When you anticipate that a certain segment of code might fail under certain conditions and you want to handle that failure gracefully, rather than having your program crash or behave unpredictably.
   - When you want to capture error information and respond accordingly, e.g., logging the error or retrying a failed operation.

4. **How to correctly handle an exception?**
   - Identify the specific exception types you want to handle.
   - Only catch exceptions you know how to handle. Avoid catching general exceptions unless you're logging or performing some cleanup, then re-throwing or propagating them.
   - Don't use exceptions for regular control flow.
   - Provide informative error messages.
   - When in doubt, allow the exception to propagate to a higher level where it might be handled more appropriately.

5. **What’s the purpose of catching exceptions?**
   - **Graceful Degradation**: Your program can continue running or fail gracefully rather than abruptly crashing.
   - **User-Friendly Feedback**: You can provide more informative and user-friendly error messages.
   - **Error Logging and Diagnostics**: Capture and log error details for debugging or monitoring purposes.
   - **Resource Management**: Ensuring resources like files, network connections, or database connections are closed or cleaned up.

6. **How to raise a builtin exception?**
   - In many languages, you can use a keyword to raise (or throw) exceptions. In Python, for instance:
     ```python
     raise ValueError("This is a custom error message.")
     ```

7. **When do we need to implement a clean-up action after an exception?**
   - If your program allocates resources that aren't automatically managed by your programming environment (e.g., open files, database connections, manually allocated memory), you need to ensure they are released or cleaned up to prevent resource leaks.
   - Many languages provide mechanisms for this. In Python, for instance, there's the `finally` block:
     ```python
     try:
         # some code that might throw an exception
     except SomeException:
         # handle exception
     finally:
         # cleanup code that will run regardless of whether an exception occurred
     ```

Using and understanding exceptions is crucial for developing robust software that can handle unexpected situations gracefully.

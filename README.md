Question 1: Are Django signals executed synchronously or asynchronously by default? Provide a code snippet to support your answer.
Django signals act as event notifications within an application, allowing different parts of the code to communicate without tightly coupling components. When an event occurs—such as creating a new user—Django signals can trigger predefined functions.

These signals can operate in either synchronous or asynchronous mode.

Synchronous Execution: The signal runs immediately when triggered, halting further execution until it completes.
Asynchronous Execution: The signal runs in the background, allowing the main process to continue without waiting for completion.
By default, Django signals execute synchronously. This means that when a signal is triggered, the function associated with it is executed immediately before the caller proceeds.

Code Explanation
To demonstrate this, let's consider a security-related scenario inspired by real-world cybersecurity practices. The function analyze_network_traffic simulates monitoring network data for malicious activity. If suspicious data is detected, a signal is sent to notify the security team.

Steps:

The function analyze_network_traffic processes network packet data.
If malicious activity is detected, it triggers the suspicious_activity signal.
The receiver function alert_security_team executes immediately, printing an alert message.
The function alert_security_team completes execution before analyze_network_traffic resumes.
This behavior confirms that Django signals run synchronously by default since execution does not proceed until the signal-handling function completes.

Question 2: Do Django signals execute in the same thread as the caller? Provide a code snippet to support your answer.
Yes, Django signals execute in the same thread as the caller unless explicitly configured otherwise.

Code Explanation
To prove this, the following logic is used:

Import necessary libraries
Define a signal
Create a signal handler (alert_security_team) that prints the thread ID.
Analyze network traffic in analyze_network_traffic, sending a signal when malicious activity is detected.
Connect the signal to the handler
Trigger the signal and observe the thread IDs printed.
Conclusion
When the signal is executed, both the main function and the signal handler print the same thread ID. This confirms that Django signals run in the same thread as the caller by default.

Question 3: Do Django signals run within the same database transaction as the caller? Provide a code snippet to support your answer.
No, Django signals do not run in the same database transaction as the caller by default. Instead, they operate in autocommit mode, meaning database changes are committed immediately.

Code Explanation
Import necessary libraries
Define a User model
Create a signal handler to send a welcome email when a user is created.
Handle potential errors with a try-except block to prevent failures from affecting the database transaction.
Log errors instead of rolling back changes.
Conclusion
If an error occurs in the signal handler (e.g., email sending fails), the user account creation is not reversed. This confirms that Django signals do not run within the same database transaction by default.

Task: Implementing a Custom Iterable Class in Python
Requirements:
Create a Rectangle class requiring length and width as initialization parameters.
Enable iteration over an instance of Rectangle, first yielding { 'length': <value> }, then { 'width': <value> }.
Implementation Approach:
Define the Rectangle class, storing length and width as attributes.
Implement __iter__ to make instances iterable.
Implement __next__ to return dictionary representations of length and width.
Implement __repr__ for a readable string representation of the object.

Example Usage:
rect = Rectangle(50, 75)
for attribute in rect:
    print(attribute)
    
Output:
{'length': 50}
{'width': 75}

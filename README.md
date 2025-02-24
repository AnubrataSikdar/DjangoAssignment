1.Question:By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic

Answer:By default, Django signals are executed synchronously. This means that when a signal is triggered, the signal handlers are executed immediately in the same thread, blocking the execution of the following code until the signal handlers finish processing.

If you want signals to be handled asynchronously, you would need to integrate a task queue like Celery or use Django’s support for asynchronous signal handling introduced in later versions (Django 4.0 and above). However, without such configurations, Django signals are synchronous by default.

2.Question: By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Answer:Yes, by default, Django signals run within the same database transaction as the caller. If an exception is raised within a signal receiver during a transaction, the entire transaction, including the caller's database operations, will be rolled back. This demonstrates that the signal's execution is part of the caller's transaction context.

3.Question:Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Answer:Yes, Django signals run in the same thread as the caller.
This means that when a signal is sent, the signal handler is executed in the same thread as the code that sent the signal.As a result, the signal handler has access to the same database transaction, request context, and thread-local variables as the code that sent the signal.This behavior is a fundamental aspect of Django's signal system and is essential for many use cases, such as auditing, logging, and caching.

4.Question:Topic: Custom Classes in Python

Description: You are tasked with creating a Rectangle class with the following requirements:

An instance of the Rectangle class requires length:int and width:int to be initialized.
We can iterate over an instance of the Rectangle class 
When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}


Answer:Explanation:

__init__ Method: This method initializes the Rectangle object with the length and width provided during object creation.

__iter__ Method: This makes the Rectangle class iterable. It yields the length and width in the required format when the object is iterated over.

In the example, iterating over the rect object prints the dictionary representations of the length and width in sequence.
This implementation meets all the requirements of the task.

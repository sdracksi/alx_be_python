#SUMMARY:
This page will introduce you to modules and packages, fundamental building blocks for code organization and re-usability in Python. You’ll learn how to import and utilize modules from the standard library and external libraries.

Concept Overview
Topics
Understanding Modules and Packages
Working with Python Libraries
Learning Objectives
Understand the concepts of modules and packages in Python.
Be able to import and use modules from the standard library.
Explain how to create custom modules and packages.
Install and utilize external Python libraries using pip.
Introduction
Python programs can become complex as they grow in size and functionality. Modules and packages provide a way to organize code into reusable components. Imagine you’re building a large and intricate structure with Lego blocks. At first, you might build small sections independently, but as your creation grows, it becomes challenging to manage everything in one go. Modules and packages in Python are like containers that help you organize your code into manageable parts, just like sorting your Lego blocks into different boxes based on their types

Detailed Explanation
Understanding Modules and Packages
Modules
A module is a Python file (.py) containing functions, classes, and variables. You can import the functionalities of a module into your program for use. Think of a module as a single box containing related pieces of code. For example, if you’re working on a project related to math operations, you can create a math module to store functions like addition, subtraction, etc. Each module focuses on specific tasks, making your code easier to understand and maintain.

Module Creation (math_functions.py):

# math_functions.py (Module)

def add(x, y):
"""Returns the sum of two numbers."""
return x + y

def subtract(x, y):
"""Returns the difference of two numbers."""
return x - y
In this file, we define two functions add() and subtract() inside the math_functions module.
The add() function takes two parameters x and y, and it returns their sum using the + operator.
The subtract() function also takes two parameters x and y, and it returns their difference using the - operator.
Program Execution (main.py):

# main.py (Program)

import math_functions

result = math_functions.add(5, 3)
print(result) # Output: 8
In the main.py program, we import the math_functions module using the import statement.
We then use the add() function from the math_functions module to add two numbers (5 and 3) and store the result in the variable result.
Finally, we print the value of result, which should be the sum of 5 and 3, resulting in the output 8.
Packages
A package is a directory containing multiple modules and potentially subdirectories (more packages). It provides a hierarchical structure for organizing related code in a meaningful way. Just like how you organize files into folders on your computer, packages help organize Python code into logical units.

How to Use Packages

Create a Package:

To create a package, you simply create a directory (folder) and place an empty file named **init**.py inside it. This file indicates that the directory is a Python package. Add Modules:

Inside the package directory, you can add Python modules (.py files) that contain your code. Import Modules: You can import modules from packages into your Python scripts using the import statement, specifying the package name and module name.

Consider a simplified example

library_system/ <-- Package directory
**init**.py <-- Indicates it's a package
books.py <-- Module within the package
members.py <-- Another module

Use the import statement to import modules or specific functions/variables from a package

# Import modules from the package

from library_system import books
from library_system import members

# Use functions/classes from the imported modules

books.add_book('Python Programming', 'John Doe')
members.add_member('Alice')

Working with Python Libraries

Standard Library: Python comes with a rich collection of built-in modules called the standard library, covering various functionalities like file handling, networking, and data manipulation.
import os # Module for interacting with the operating system

# Get the current working directory

cwd = os.getcwd()
print(cwd)

External Libraries: Many powerful third-party libraries extend Python’s capabilities beyond the standard library. You can install them using the pip package manager.
Example Libraries

requests: Enables making HTTP requests to web APIs and servers.
numpy: Provides powerful tools for numerical computing and scientific data analysis.
pandas: Offers data structures and analysis tools for working with tabular data.

Practice Exercises
Exercise 1: Creating and Using Modules

Instructions:

Create a custom Python module named calculator.py that contains functions for basic arithmetic operations (addition, subtraction, multiplication, division).
Create functions add, subtract, multiply, and divide in the calculator.py module.
Import the calculator module into a separate Python script main.py and use its functions to perform arithmetic operations on numbers like 5 and 3.
Exercise 2: Exploring Python Libraries

Instruction:

Use the requests library to fetch weather information from an online weather API (e.g., weatherapi.
Install the requests library using pip if it’s not already installed pip install requests.
Write a Python script weather.py to use the requests.get method to fetch weather data from the API.
Print out relevant weather information (e.g., temperature, weather description) from the API response.

Additional Resources:

Python Documentation: Modules:
How to Install Python Packages with pip
The Python Standard Library

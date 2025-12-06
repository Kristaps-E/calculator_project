# Calculator Project

This project implements a simple command-line calculator in Python.\
It supports basic arithmetic operations, a custom square-root operator,
and memory-based calculations.\
The purpose of the project is to practice Python fundamentals, regular
expressions, error handling, unit testing,\
and writing clean, maintainable code.

------------------------------------------------------------------------

## Features

-   Basic arithmetic operations: addition, subtraction, multiplication,
    division\
-   Custom square-root operator using the symbol `V`
    -   Example: `V 49`\
    -   Example: `+ V 36` (adds the square root to memory)\
-   Memory-based operations such as `+ 5` or `* 2`\
-   Error handling for:
    -   division by zero\
    -   negative square roots\
    -   invalid input formats\
-   Clean docstrings and PEP8-compliant structure\
-   Unit tests with a pass/fail summary printed after execution

------------------------------------------------------------------------

## How the Calculator Works

The calculator processes user input by matching patterns using regular
expressions.\
It supports two main types of expressions:

### 1. Arithmetic Expressions

Examples:

    5 + 5
    10/2
    * 3

### 2. Square-Root Expressions

Examples:

    V 25
    + V 36

The program maintains a memory value representing the last computed
result.\
Typing `exit` terminates the calculator.

------------------------------------------------------------------------

## Project Structure

    calculator_project/
    │
    ├── calculator.py
    │
    ├── TEST/
    │   └── test_calculator.py
    │
    └── README.md

------------------------------------------------------------------------

## Running the Calculator

Run from the project directory:

    python3 calculator.py

Example session:

    Enter expression: 5 + 5
    The result is: 10.0

    Enter expression: * 2
    The result is: 20.0

    Enter expression: V 49
    The square root is: 7.0

    Enter expression: + V 36
    The result is: 13.0

------------------------------------------------------------------------

## Running the Unit Tests

Execute:

    python3 -m unittest TEST/test_calculator.py

At the end of the test run, a summary is printed:

    ----------------------------
    Test Summary:
    Total tests: X
    Passed:      X
    Failed:      X
    Errors:      X
    Skipped:     X
    ----------------------------

------------------------------------------------------------------------

## Code Style and Design

The project follows:

-   PEP8 formatting\
-   Type hints\
-   Docstrings based on PEP 257\
-   Object-oriented structure using a Calculator class\
-   Regex parsing for predictable input handling\
-   Separation between core logic and testing scripts

------------------------------------------------------------------------

## Future Improvements

-   Add exponentiation support\
-   Add parentheses and full expression parsing\
-   Save and load calculation history\
-   Add CLI arguments for expression evaluation\
-   Build a simple graphical interface

------------------------------------------------------------------------

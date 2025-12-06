import math
import re
from typing import Callable, Dict, Optional


class Calculator:
    """
    A simple calculator that supports arithmetic operations and square root.
    Stores the last computed result in memory.
    """

    def __init__(self) -> None:
        self.memory: float = 0.0
        self.operations: Dict[str, Callable[[float, float], float]] = {
            "+": self.add,
            "-": self.sub,
            "*": self.mul,
            "/": self.div,
        }

    def add(self, x: float, y: float) -> float:
        """Return x + y."""
        return x + y

    def sub(self, x: float, y: float) -> float:
        """Return x - y."""
        return x - y

    def mul(self, x: float, y: float) -> float:
        """Return x * y."""
        return x * y

    def div(self, x: float, y: float) -> float:
        """
        Return x / y.
        Raises ValueError if dividing by zero.
        """
        if y == 0:
            raise ValueError("Division by zero is not allowed.")
        return x / y

    def sqrt(self, x: float) -> float:
        """
        Return the square root of x.
        Raises ValueError if x is negative.
        """
        if x < 0:
            raise ValueError("Square root of a negative number is not allowed.")
        return math.sqrt(x)

    def handle_square_operations(self, expression: str) -> Optional[str]:
        """
        Handle square root expressions using the operator 'V'.
        Supports:
            'V 36'
            '+ V 36'
            '- V 49'
        """
        pattern = r"^\s*([+\-*/]?)\s*V\s*(-?\d+(\.\d+)?)\s*$"
        match = re.match(pattern, expression, flags=re.IGNORECASE)

        if not match:
            return None

        operator, num_str = match.group(1), match.group(2)
        value = float(num_str)
        root_result = self.sqrt(value)

        if operator:
            self.memory = self.operations[operator](self.memory, root_result)
            return f"The result is: {round(self.memory, 2)}"

        self.memory = root_result
        return f"The square root is: {round(self.memory, 2)}"

    def handle_arithmetic(self, expression: str) -> Optional[str]:
        """
        Handle arithmetic expressions:
            '5 + 5'
            '10/2'
            '+ 5'  (uses memory as the first operand)
        """
        full_pattern = r"^\s*(-?\d+(\.\d+)?)\s*([\+\-\*/])\s*(-?\d+(\.\d+)?)\s*$"
        match = re.match(full_pattern, expression)

        if match:
            x = float(match.group(1))
            operator = match.group(3)
            y = float(match.group(4))
            self.memory = self.operations[operator](x, y)
            return f"The result is: {round(self.memory, 2)}"

        memory_pattern = r"^\s*([\+\-\*/])\s*(-?\d+(\.\d+)?)\s*$"
        match = re.match(memory_pattern, expression)

        if match:
            operator = match.group(1)
            y = float(match.group(2))
            self.memory = self.operations[operator](self.memory, y)
            return f"The result is: {round(self.memory, 2)}"

        return None


def main() -> None:
    """Main program loop handling user interactions."""
    calculator = Calculator()

    while True:
        expression = input(
            "Enter expression (e.g., '5*5', '+5', 'V 49', '- V 36', or 'exit'): "
        ).strip()

        if expression.lower() == "exit":
            print("Exiting the calculator. Goodbye!")
            break

        try:
            response = calculator.handle_square_operations(expression)
            if response:
                print(response)
                continue

            response = calculator.handle_arithmetic(expression)
            if response:
                print(response)
                continue

            print("Invalid input. Please enter a valid expression.")

        except ValueError as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    main()

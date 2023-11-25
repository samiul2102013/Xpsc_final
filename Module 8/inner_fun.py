class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calculate(self, operation):
        def add():
            return self.num1 + self.num2

        def subtract():
            return self.num1 - self.num2

        def multiply():
            return self.num1 * self.num2

        def divide():
            if self.num2 != 0:
                return self.num1 / self.num2
            else:
                return "Division by zero is not allowed."

        operations = {
            'add': add,
            'subtract': subtract,
            'multiply': multiply,
            'divide': divide
        }

        if operation in operations:
            result = operations[operation]()
            return f"Result of {operation}: {result}"
        else:
            return f"Invalid operation: {operation}"

calculator = Calculator(5, 2)
print(calculator.calculate('add'))
print(calculator.calculate('divide'))
print(calculator.calculate('power'))

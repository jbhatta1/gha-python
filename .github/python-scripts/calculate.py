print("Hello world!")
import os

input_FIRST_num = int(os.environ.get("FIRST_NUM"))
input_SECOND_num = int(os.environ.get("SECOND_NUM"))
func_needed = os.environ.get("FUNC_NEEDED")

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

func_list = {"add": add, "subtract": subtract, "multiply": multiply, "divide": divide}

def calculate(n1, n2, func):
  for key in func_list:
      if key == func:
        return func_list[key](n1, n2)


print(f"{input_FIRST_num} {func_needed} {input_SECOND_num} = {calculate(input_FIRST_num, input_SECOND_num, func_needed)}")

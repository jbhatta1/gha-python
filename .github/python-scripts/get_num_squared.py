print("Hello world!")
import os

input_num = int(os.environ.get("INPUT_NUM"))
print(f"Input number provided {input_num}")
def square(num):
    return num * num

print(square(input_num))
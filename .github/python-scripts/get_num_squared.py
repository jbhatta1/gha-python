print("Hello world!")
import os

input_num = os.environ.get("GITHUB_ENV")
print(input_num)
def square(num):
    return num * num

square(11)
print("Hello world!")
import os

input_num = os.environ.get("GITHUB_ENV")
print(f"Input number provided ${input_num}")
def square(num):
    return num * num

print(square(11))
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("numbers", type=int, nargs='+' )
numbers = vars(parser.parse_args()).get("numbers")

def custom_sum(numbers):
    if len(numbers) == 1:
        return numbers.pop(len(numbers) - 1)
    else:
        return numbers.pop(len(numbers) - 1) + custom_sum(numbers)

_time = time.time()
print(custom_sum(numbers.copy()))
custom_sum_time = time.time() - _time

_time = time.time()
print(numbers)
print(sum(numbers))
sum_time = time.time() - _time

print(f"custom sum takes {custom_sum_time}; sum takes {sum_time}\n")

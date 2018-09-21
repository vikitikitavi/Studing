from timeit import timeit
import random

numbers = random.sample(range(0, 1000000), 10000)

rec_time = timeit(stmt="qsort(numbers)", setup="from rec import qsort\nfrom __main__ import numbers", number=1)
simple_time = timeit(stmt="qsort(numbers)", setup="from non_rec import qsort\nfrom __main__ import numbers", number=1)
standart_time = timeit(stmt="numbers.sort()", setup="from __main__ import numbers", number=1)
print(f"Recursive sort: {rec_time}\n"
      f"Not recursive sort: {simple_time}\n"
      f"Standart sort: {standart_time}\n"
)
import cProfile
from non_rec import qsort
cProfile.run(f"qsort({repr(numbers)})")
from collections import deque
from typing      import Union, List, Deque, Tuple, Any

from datascience import NumberFormatter

from testing_performance import performance, output, type_name, test

def main():
  sample_sizes = [10**5, 2*10**5]
  lst: List[str] = []
  my_stack: Deque[str] = deque()

  table = test([lst, my_stack], sample_sizes)
  table.set_format([1, 2, 3], NumberFormatter)
  print(table)

if __name__ == '__main__':
  main()
